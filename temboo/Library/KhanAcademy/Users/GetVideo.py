# -*- coding: utf-8 -*-

###############################################################################
#
# GetVideo
# Retrieves user data about a specific video, such as amount of video watched, points received, etc.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetVideo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetVideo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Users/GetVideo')


    def new_input_set(self):
        return GetVideoInputSet()

    def _make_result_set(self, result, path):
        return GetVideoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetVideoChoreographyExecution(session, exec_id, path)

class GetVideoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetVideo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Khan Academy.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The OAuth Consumer Secret provided by Khan Academy.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email address (coach or student ID) of user. If not provided, defaults to currently logged in user.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_OAuthTokenSecret(self, value):
        """
        Set the value of the OAuthTokenSecret input for this Choreo. ((required, string) The OAuth Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'OAuthTokenSecret', value)
    def set_OAuthToken(self, value):
        """
        Set the value of the OAuthToken input for this Choreo. ((required, string) The OAuth Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'OAuthToken', value)
    def set_YouTubeID(self, value):
        """
        Set the value of the YouTubeID input for this Choreo. ((required, string) The YouTube ID of the video for which you want to retrieve information.)
        """
        InputSet._set_input(self, 'YouTubeID', value)

class GetVideoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetVideo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class GetVideoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetVideoResultSet(response, path)
