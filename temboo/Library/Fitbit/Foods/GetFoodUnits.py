# -*- coding: utf-8 -*-

###############################################################################
#
# GetFoodUnits
# Get a list of all valid Fitbit food units.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetFoodUnits(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetFoodUnits Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/Foods/GetFoodUnits')


    def new_input_set(self):
        return GetFoodUnitsInputSet()

    def _make_result_set(self, result, path):
        return GetFoodUnitsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFoodUnitsChoreographyExecution(session, exec_id, path)

class GetFoodUnitsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetFoodUnits
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((optional, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetFoodUnitsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFoodUnits Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class GetFoodUnitsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFoodUnitsResultSet(response, path)
