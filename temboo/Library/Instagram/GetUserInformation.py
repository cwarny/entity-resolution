# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserInformation
# Retrieves basic information about a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetUserInformation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUserInformation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetUserInformation')


    def new_input_set(self):
        return GetUserInformationInputSet()

    def _make_result_set(self, result, path):
        return GetUserInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserInformationChoreographyExecution(session, exec_id, path)

class GetUserInformationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUserInformation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user that you want to retrieve. Defaults to 'self' which will return the user associated with the access token.)
        """
        InputSet._set_input(self, 'UserID', value)

class GetUserInformationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUserInformation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetUserInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUserInformationResultSet(response, path)
