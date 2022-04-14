import re
import deepy.cfg
import deepy.deepui
import deepy.dimensions.util
import deepy.log as log

import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json

# Define Regex paterns to extract query-fields
# pattern to extract the boundary fields from a boundary dimension 
boundarydim_regex = re.compile(r"boundary\.([\w.-]*)\.(\w*)")


class Context():

    def __init__(self, contextList, reEvaluate = False, callingProgram = 'user_query_summary'):
        if not os.path.exists('context.json') or (not os.path.exists('dashboards.json') and callingProgram=='get_dashboards'):
            reEvaluate = True
        self.contextsToEvaluate = contextList
        self.boundaryMap = self.getBoundaryMap()
        if not reEvaluate:
            with open('context.json') as f:
                self.allContextViewInfo = json.load(f)
                for context in contextList:
                     if context not in self.allContextViewInfo.keys():
                         reEvaluate = True
                         return
            log.info("Loaded context, view, and dimension info from local file 'context.json', use --no-cache if you want fresher info.")
            if callingProgram == 'get_dashboards':
                log.info("Loading dashboard definitions from local file 'dashboards.json', use --no-cache if you want fresher info.")
                with open('dashboards.json') as f:
                    self.dashboardInfo = json.load(f)
        if reEvaluate:
            log.info("Loading context, view, and dimension info from Deepfield API, please wait...")
            self.ddb = deepy.dimensions.ddb.get_local_ddb()
            self.allContextViewInfo = self.storeAllContextViewInfo(self.contextsToEvaluate)
            log.info("Storing context, view, and dimension info into local file 'context.json' for future caching")
            with open('context.json', 'w') as f:
                json.dump(self.allContextViewInfo, f)
            if callingProgram == 'get_dashboards':
                log.info("Loading dashboard definitions from Deepfield API")
                self.dashboardInfo = self.getDashboardInfo()
                log.info("Storing dashboard definitions into local file 'dashboards.json' for future caching")
                with open('dashboards.json', 'w') as f:
                    json.dump(self.dashboardInfo, f)

    def storeAllContextViewInfo(self, contextsToEvaluate):
        allTheThings = {}
        # Get the pipedream version
        pipedreamVersion = str(deepy.cfg.slice_config.get("build_updates", {}).get("revision"))
        if pipedreamVersion.startswith("5"):
            lookForViewsInMysql = True
        else:
            lookForViewsInMysql = False
    
        for context in contextsToEvaluate:
            if lookForViewsInMysql:
                allTheThings[context] = self.getSqlViews(context)
            else:
                allTheThings[context] = self.getOldViews(context)
        return allTheThings
    
    def getViewDimensionsAndBoundaries(self, view, context):
        named_dimensions = []
        named_boundaries = []
        view_type = 'simple'
        dimensions = view.get("dimensions")
        if dimensions is None:
            dimensions = context.get("dimensions")
        if dimensions is None:
            dimensions = []
        for dim in dimensions:
            named_dim = deepy.dimensions.util.dim_id_to_name(self.ddb, dim)
            mo = boundarydim_regex.search(named_dim)
            if mo:
                view_type = 'explicit_boundary'
                named_boundary = ''
                if type(mo.group(1)) == 'int':
                    named_boundary = 'boundary.' + self.boundaryMap[int(mo.group(1))] + '.' + mo.group(2)
                else:
                    named_boundary = 'boundary.' + mo.group(1) + '.' + mo.group(2)
                named_boundaries.append(named_boundary)
            elif named_dim == 'all_boundary_columns_macro':
                for boundary in self.boundaryMap.values():
                    split_boundary = [ 'boundary.' + boundary + '.input', 'boundary.' + boundary + '.output' ] 
                    named_boundaries = named_boundaries + split_boundary
            else:
                named_dimensions.append(deepy.dimensions.util.dim_id_to_name(self.ddb, dim))
    
        view_properties = dict()
        view_properties['dimensions'] = sorted(named_dimensions)
        view_properties['boundaries'] = sorted(named_boundaries)
        view_properties['type'] = view_type
        
        return view_properties
    
    
    def getSqlViews(self, context_id):
        from deepy.context import sql_context_util
        listOfViews = {}
        context_json = sql_context_util.get_merged_contexts(context=context_id)
        for view in context_json[context_id].get("views", []):
            viewDimensionsAndBoundaries = self.getViewDimensionsAndBoundaries(view, context_json)
            listOfViews[view.get("uuid", view.get("name"))] = {
                "dimensions": viewDimensionsAndBoundaries['dimensions'],
                "boundaries": viewDimensionsAndBoundaries['boundaries'],
                "type": viewDimensionsAndBoundaries['type'],
                "timesteps": view.get("timesteps"),
                "retention": view.get("retention"),
                "name": view.get("name")
            }
        return listOfViews
    
    
    def getOldViews(self, context_id):
        listOfViews = {}
        local_path = deepy.cfg.context_dir + "/%s.json" % context_id
        context_json = deepy.cfg.connector_store.simple_load_json(local_path)
        if not context_json:
            return
    
        for view in context_json[context_id].get("views", []):
            viewDimensionsAndBoundaries = self.getViewDimensionsAndBoundaries(view, context_json)
            listOfViews[view.get("uuid")] = {
                "dimensions": viewDimensionsAndBoundaries['dimensions'],
                "boundaries": viewDimensionsAndBoundaries['boundaries'],
                "type": viewDimensionsAndBoundaries['boundaries'],
                "timesteps": view.get("timesteps"),
                "retention": view.get("retention")
            }
        return listOfViews
    
    def getBoundaryMap(self):
        apiKey = deepy.deepui.get_root_api_keys()[0]
        total_size = None
        url = 'https://localhost/api/boundaries?api_key=' + apiKey
        response = requests.get(url, verify=False)
        boundaryMap = dict()
        for boundary in response.json():
            boundaryMap[boundary['id']] = boundary['name'].lower()
        return boundaryMap

    def getDashboardInfo(self):
        apiKey = deepy.deepui.get_root_api_keys()[0]
        url = 'https://localhost/api/dashboards?api_key=' + apiKey
        response = requests.get(url, verify=False)
        dashboards = response.json()
        all_dashboards = list()
        for dashboard in dashboards:
            url = 'https://localhost/api/dashboards/' + dashboard['slug'] + '?api_key=' + apiKey
            response = requests.get(url, verify=False)
            dashboard_info = response.json()
            all_dashboards.append(dashboard_info)
        return all_dashboards

    def view_uuid(self, row):
        viewCandidate = {"name": "No_Match", "uuid": "-99", "precision": 99000, "dimensions_and_boundaries": ''}
        for aView in self.allContextViewInfo[row['context']]:
            viewDimensionsSet = set(map(lambda x:x.lower(), self.allContextViewInfo[row['context']][aView].get("dimensions", [])))
            queriesDimensionsSet = set(map(lambda x:x.lower(), row['dimensions']))
            viewBoundariesSet = set(map(lambda x:x.lower(), self.allContextViewInfo[row['context']][aView].get("boundaries", [])))
            queriesBoundariesSet = set(map(lambda x:x.lower(), row['boundaries']))
            viewType = self.allContextViewInfo[row['context']][aView].get("type")
            if (viewDimensionsSet|viewBoundariesSet).issuperset(queriesDimensionsSet) and viewBoundariesSet.issuperset(queriesBoundariesSet):
                if viewType == 'explicit_boundary':
                    if len(queriesBoundariesSet) == 0: continue
                dimensionsDifference = len(viewDimensionsSet.difference(queriesDimensionsSet))
                boundariesDifference = len(viewBoundariesSet.difference(queriesBoundariesSet))
                difference = 1000 * dimensionsDifference + boundariesDifference
                if difference < viewCandidate['precision']:
                    viewCandidate['uuid'] = aView
                    viewCandidate['name'] = self.allContextViewInfo[row['context']][aView].get("name", "None")
                    viewCandidate['precision'] = difference
                    viewCandidate['dimensions_and_boundaries'] = sorted(tuple(viewDimensionsSet | viewBoundariesSet))
        row['uuid'] = viewCandidate['uuid']
        row['name'] = viewCandidate['name'] 
        row['matching_view_dimensions'] = viewCandidate['dimensions_and_boundaries']
        return row
