# -*- coding: utf-8 -*-

###############################################################################
#
# DistrictSearch
# Returns a list of school profiles and related school information for a zip code, city, state, or other criteria in the search parameters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DistrictSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DistrictSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SchoolFinder/DistrictSearch')


    def new_input_set(self):
        return DistrictSearchInputSet()

    def _make_result_set(self, result, path):
        return DistrictSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DistrictSearchChoreographyExecution(session, exec_id, path)

class DistrictSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DistrictSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your School Finder API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((conditional, string) The name of a city. City requests must also be accompanied by the corresponding state parameter.)
        """
        InputSet._set_input(self, 'City', value)
    def set_DistrictID(self, value):
        """
        Set the value of the DistrictID input for this Choreo. ((conditional, string) The internal Education.com id of a school district.)
        """
        InputSet._set_input(self, 'DistrictID', value)
    def set_DistrictLEA(self, value):
        """
        Set the value of the DistrictLEA input for this Choreo. ((conditional, string) The NCES Local Education Agency (LEA) id of a school district.)
        """
        InputSet._set_input(self, 'DistrictLEA', value)
    def set_DistrictName(self, value):
        """
        Set the value of the DistrictName input for this Choreo. ((conditional, string) The name of the district.)
        """
        InputSet._set_input(self, 'DistrictName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by Education.com. Defaluts to XML. JSON is also possible.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((conditional, string) The two letter abbreviation of a state e.g. South Caroline should be formatted “SC”.)
        """
        InputSet._set_input(self, 'State', value)

class DistrictSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DistrictSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Education.com.)
        """
        return self._output.get('Response', None)

class DistrictSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DistrictSearchResultSet(response, path)
