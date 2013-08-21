# -*- coding: utf-8 -*-

###############################################################################
#
# Civic
# Retrieves a host of information about the district and representatives of a specified location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Civic(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Civic Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/GoodCitizen/Civic')


    def new_input_set(self):
        return CivicInputSet()

    def _make_result_set(self, result, path):
        return CivicResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CivicChoreographyExecution(session, exec_id, path)

class CivicInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Civic
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((optional, json) The JSON dictionary for the Sulight Labs credentials required to operate this choreo. LittleSis credentials are optional. See docs for the format of this input.)
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate of your location.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Set the number of records to return for the bills, votes, and relationships of each legislator. Defaults to 5.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate of your locaion.)
        """
        InputSet._set_input(self, 'Longitude', value)

class CivicResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Civic Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from the Civic Choreo.)
        """
        return self._output.get('Response', None)

class CivicChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CivicResultSet(response, path)
