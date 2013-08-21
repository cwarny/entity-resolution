# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveUserDashboard
# Retrieves the dashboard of the user that corresponds to the OAuth credentials provided.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveUserDashboard(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveUserDashboard Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/User/RetrieveUserDashboard')


    def new_input_set(self):
        return RetrieveUserDashboardInputSet()

    def _make_result_set(self, result, path):
        return RetrieveUserDashboardResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveUserDashboardChoreographyExecution(session, exec_id, path)

class RetrieveUserDashboardInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveUserDashboard
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
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
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to return: 1 - 20. Defaults to 20.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_NotesInfo(self, value):
        """
        Set the value of the NotesInfo input for this Choreo. ((optional, boolean) Indicates whether to return notes information. Specify 1(true) or 0 (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'NotesInfo', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The result to start at. Defaults to 0.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_ReblogInfo(self, value):
        """
        Set the value of the ReblogInfo input for this Choreo. ((optional, boolean) Indicates whether to return reblog information. Specify 1(true) or 0 (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'ReblogInfo', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)
    def set_SinceId(self, value):
        """
        Set the value of the SinceId input for this Choreo. ((optional, integer) Return posts that have appeared after this ID. Used to page through results.)
        """
        InputSet._set_input(self, 'SinceId', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of post to return. Specify one of the following:  text, photo, quote, link, chat, audio, video, answer.)
        """
        InputSet._set_input(self, 'Type', value)

class RetrieveUserDashboardResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveUserDashboard Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class RetrieveUserDashboardChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveUserDashboardResultSet(response, path)
