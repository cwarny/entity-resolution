# -*- coding: utf-8 -*-

###############################################################################
#
# GetCensusIDByTypeAndName
# Retrieve the U.S. census ID for a specified geography type and name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetCensusIDByTypeAndName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCensusIDByTypeAndName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetCensusIDByTypeAndName')


    def new_input_set(self):
        return GetCensusIDByTypeAndNameInputSet()

    def _make_result_set(self, result, path):
        return GetCensusIDByTypeAndNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCensusIDByTypeAndNameChoreographyExecution(session, exec_id, path)

class GetCensusIDByTypeAndNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCensusIDByTypeAndName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_GeographyName(self, value):
        """
        Set the value of the GeographyName input for this Choreo. ((required, string) Specify the geography name for the correspnding type, with at least three leading characters. For example, for the geography type "state" you could enter "ore" for Oregon.)
        """
        InputSet._set_input(self, 'GeographyName', value)
    def set_GeographyType(self, value):
        """
        Set the value of the GeographyType input for this Choreo. ((required, string) Specify one of the following geography type values: "state", "county", "tract", "block", "congdistrict", "statehouse", "statesenate", "censusplace", or "msa" (metropolitan statistical area).)
        """
        InputSet._set_input(self, 'GeographyType', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((required, integer) Specify the maximum number of results to return. Defaults to 50.)
        """
        InputSet._set_input(self, 'MaxResults', value)

class GetCensusIDByTypeAndNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCensusIDByTypeAndName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_CensusID(self):
        """
        Retrieve the value for the "CensusID" output from this Choreo execution. ((integer) The ID retrieved from the API call.)
        """
        return self._output.get('CensusID', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from the API.)
        """
        return self._output.get('Response', None)

class GetCensusIDByTypeAndNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCensusIDByTypeAndNameResultSet(response, path)
