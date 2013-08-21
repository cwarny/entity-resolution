# -*- coding: utf-8 -*-

###############################################################################
#
# GetTimeOfUseGroup
# Returns a particular Time of Use Group with a given touGroupId and lseId.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTimeOfUseGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTimeOfUseGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetTimeOfUseGroup')


    def new_input_set(self):
        return GetTimeOfUseGroupInputSet()

    def _make_result_set(self, result, path):
        return GetTimeOfUseGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimeOfUseGroupChoreographyExecution(session, exec_id, path)

class GetTimeOfUseGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTimeOfUseGroup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The App ID provided by Genability.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_EndsWith(self, value):
        """
        Set the value of the EndsWith input for this Choreo. ((optional, string) When true, the search will only return results that end with the specified search string. Otherwise, any match of the search string will be returned as a result.)
        """
        InputSet._set_input(self, 'EndsWith', value)
    def set_IsRegex(self, value):
        """
        Set the value of the IsRegex input for this Choreo. ((optional, boolean) When true, the provided search string will be regarded as a regular expression and the search will return results matching the regular expression.)
        """
        InputSet._set_input(self, 'IsRegex', value)
    def set_LSEID(self, value):
        """
        Set the value of the LSEID input for this Choreo. ((conditional, integer) Used to retrieve a TOU Group for a specific LSE.)
        """
        InputSet._set_input(self, 'LSEID', value)
    def set_PageCount(self, value):
        """
        Set the value of the PageCount input for this Choreo. ((optional, integer) The number of results to return. Defaults to 25.)
        """
        InputSet._set_input(self, 'PageCount', value)
    def set_PageStart(self, value):
        """
        Set the value of the PageStart input for this Choreo. ((optional, integer) The page number to begin the result set from. Defaults to 1.)
        """
        InputSet._set_input(self, 'PageStart', value)
    def set_SearchOn(self, value):
        """
        Set the value of the SearchOn input for this Choreo. ((optional, string) Comma separated list of fields to query on. When searchOn is specified, the text provided in the search string field will be searched within these fields.)
        """
        InputSet._set_input(self, 'SearchOn', value)
    def set_Search(self, value):
        """
        Set the value of the Search input for this Choreo. ((optional, string) The string of text to search on. This can also be a regular expression, in which case you should set the 'isRegex' flag to true.)
        """
        InputSet._set_input(self, 'Search', value)
    def set_SortOn(self, value):
        """
        Set the value of the SortOn input for this Choreo. ((optional, string) Comma separated list of fields to sort on.)
        """
        InputSet._set_input(self, 'SortOn', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Comma separated list of ordering. Possible values are 'ASC' and 'DESC'. Default is 'ASC'. This list corresponds to the field list used in the SortOn input.)
        """
        InputSet._set_input(self, 'SortOrder', value)
    def set_StartsWith(self, value):
        """
        Set the value of the StartsWith input for this Choreo. ((optional, boolean) When true, the search will only return results that begin with the specified search string. Otherwise, any match of the search string will be returned as a result.)
        """
        InputSet._set_input(self, 'StartsWith', value)
    def set_TOUGroupID(self, value):
        """
        Set the value of the TOUGroupID input for this Choreo. ((conditional, integer) Used to retrieve a TOU Group by its ID (required when LSE ID is provided).)
        """
        InputSet._set_input(self, 'TOUGroupID', value)

class GetTimeOfUseGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTimeOfUseGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTimeOfUseGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTimeOfUseGroupResultSet(response, path)
