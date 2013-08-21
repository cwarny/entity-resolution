# -*- coding: utf-8 -*-

###############################################################################
#
# InsertPastLocation
# Updates or creates an entry in an authenticated user's location history.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class InsertPastLocation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the InsertPastLocation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Latitude/InsertPastLocation')


    def new_input_set(self):
        return InsertPastLocationInputSet()

    def _make_result_set(self, result, path):
        return InsertPastLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertPastLocationChoreographyExecution(session, exec_id, path)

class InsertPastLocationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the InsertPastLocation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Latitide(self, value):
        """
        Set the value of the Latitide input for this Choreo. ((required, decimal) Enter latitude coordinates. For example: 37.420352.)
        """
        InputSet._set_input(self, 'Latitide', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Enter longitude coordinates.  For example: -122.083389.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_TimestampMs(self, value):
        """
        Set the value of the TimestampMs input for this Choreo. ((required, date) Enter a timestamp value (in epoch time).  Example: 1325715558.)
        """
        InputSet._set_input(self, 'TimestampMs', value)

class InsertPastLocationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the InsertPastLocation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) )
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class InsertPastLocationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InsertPastLocationResultSet(response, path)
