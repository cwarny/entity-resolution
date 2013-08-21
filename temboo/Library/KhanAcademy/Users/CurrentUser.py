# -*- coding: utf-8 -*-

###############################################################################
#
# CurrentUser
# Retrieves user data about a specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CurrentUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CurrentUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Users/CurrentUser')


    def new_input_set(self):
        return CurrentUserInputSet()

    def _make_result_set(self, result, path):
        return CurrentUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CurrentUserChoreographyExecution(session, exec_id, path)

class CurrentUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CurrentUser
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

class CurrentUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CurrentUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class CurrentUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CurrentUserResultSet(response, path)
