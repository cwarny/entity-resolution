# -*- coding: utf-8 -*-

###############################################################################
#
# GetDemographicsByTypeAndID
# Retrieve demographic data for a specified geography type and geography ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetDemographicsByTypeAndID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDemographicsByTypeAndID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetDemographicsByTypeAndID')


    def new_input_set(self):
        return GetDemographicsByTypeAndIDInputSet()

    def _make_result_set(self, result, path):
        return GetDemographicsByTypeAndIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDemographicsByTypeAndIDChoreographyExecution(session, exec_id, path)

class GetDemographicsByTypeAndIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDemographicsByTypeAndID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DataVersion(self, value):
        """
        Set the value of the DataVersion input for this Choreo. ((optional, string) Specify the census data version to search, such as "jun2011" (the default).)
        """
        InputSet._set_input(self, 'DataVersion', value)
    def set_GeographyIDs(self, value):
        """
        Set the value of the GeographyIDs input for this Choreo. ((conditional, integer) The geography IDs to search for. Separate multiple IDs by commas; a maximum of 10 IDs are allowed.)
        """
        InputSet._set_input(self, 'GeographyIDs', value)
    def set_GeographyType(self, value):
        """
        Set the value of the GeographyType input for this Choreo. ((required, string) Specify one of the following geography type values: "state", "county", "tract", "block", "congdistrict", "statehouse", "statesenate", "censusplace", or "msa" (metropolitan statistical area).)
        """
        InputSet._set_input(self, 'GeographyType', value)

class GetDemographicsByTypeAndIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDemographicsByTypeAndID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from the API.)
        """
        return self._output.get('Response', None)

class GetDemographicsByTypeAndIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDemographicsByTypeAndIDResultSet(response, path)
