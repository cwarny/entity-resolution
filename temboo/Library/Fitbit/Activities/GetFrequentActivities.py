# -*- coding: utf-8 -*-

###############################################################################
#
# GetFrequentActivities
# Gets a list of a user's frequent activities.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetFrequentActivities(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetFrequentActivities Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/Activities/GetFrequentActivities')


    def new_input_set(self):
        return GetFrequentActivitiesInputSet()

    def _make_result_set(self, result, path):
        return GetFrequentActivitiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFrequentActivitiesChoreographyExecution(session, exec_id, path)

class GetFrequentActivitiesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetFrequentActivities
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

class GetFrequentActivitiesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFrequentActivities Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class GetFrequentActivitiesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFrequentActivitiesResultSet(response, path)
