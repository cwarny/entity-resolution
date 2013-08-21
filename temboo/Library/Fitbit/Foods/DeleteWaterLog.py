# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteWaterLog
# Deletes a specified water log entry.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteWaterLog(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteWaterLog Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/Foods/DeleteWaterLog')


    def new_input_set(self):
        return DeleteWaterLogInputSet()

    def _make_result_set(self, result, path):
        return DeleteWaterLogResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteWaterLogChoreographyExecution(session, exec_id, path)

class DeleteWaterLogInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteWaterLog
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
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        InputSet._set_input(self, 'UserID', value)
    def set_WaterLogID(self, value):
        """
        Set the value of the WaterLogID input for this Choreo. ((required, integer) The id of the water log you want to delete. The Id is returned in the LogWater response.)
        """
        InputSet._set_input(self, 'WaterLogID', value)

class DeleteWaterLogResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteWaterLog Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class DeleteWaterLogChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteWaterLogResultSet(response, path)
