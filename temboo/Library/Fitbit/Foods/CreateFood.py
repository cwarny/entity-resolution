# -*- coding: utf-8 -*-

###############################################################################
#
# CreateFood
# Create new private food for a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateFood(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateFood Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/Foods/CreateFood')


    def new_input_set(self):
        return CreateFoodInputSet()

    def _make_result_set(self, result, path):
        return CreateFoodResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateFoodChoreographyExecution(session, exec_id, path)

class CreateFoodInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateFood
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Calories(self, value):
        """
        Set the value of the Calories input for this Choreo. ((required, integer) The number of calories per serving size.)
        """
        InputSet._set_input(self, 'Calories', value)
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
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description for the food entry.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_FormType(self, value):
        """
        Set the value of the FormType input for this Choreo. ((optional, string) Form type; (LIQUID or DRY).)
        """
        InputSet._set_input(self, 'FormType', value)
    def set_MeasurementUnitID(self, value):
        """
        Set the value of the MeasurementUnitID input for this Choreo. ((required, integer) The default measurement unit.)
        """
        InputSet._set_input(self, 'MeasurementUnitID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the food.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ServingSize(self, value):
        """
        Set the value of the ServingSize input for this Choreo. ((required, integer) The default serving size.)
        """
        InputSet._set_input(self, 'ServingSize', value)

class CreateFoodResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateFood Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class CreateFoodChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateFoodResultSet(response, path)
