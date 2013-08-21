# -*- coding: utf-8 -*-

###############################################################################
#
# SetupApp
# Sets up a previously activated app.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SetupApp(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetupApp Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/FilterCommands/SetupApp')


    def new_input_set(self):
        return SetupAppInputSet()

    def _make_result_set(self, result, path):
        return SetupAppResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetupAppChoreographyExecution(session, exec_id, path)

class SetupAppInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetupApp
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        InputSet._set_input(self, 'APIUser', value)
    def set_AppName(self, value):
        """
        Set the value of the AppName input for this Choreo. ((required, string) The name of the app to be activated.  A list of available apps can be obtained by running the ListAvailableApps Choreo.)
        """
        InputSet._set_input(self, 'AppName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) Enter the password for the app that is being setup.  For example, if setting up a Twitter app, enter a valid Twitter account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The username for the app that is being setup. For example, if setting up a Twitter app, enter a valid Twitter account username.)
        """
        InputSet._set_input(self, 'Username', value)


class SetupAppResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetupApp Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class SetupAppChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetupAppResultSet(response, path)
