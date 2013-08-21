# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateInstallation
# Updates an existing installation object on Parse.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateInstallation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateInstallation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Parse/PushNotifications/UpdateInstallation')


    def new_input_set(self):
        return UpdateInstallationInputSet()

    def _make_result_set(self, result, path):
        return UpdateInstallationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateInstallationChoreographyExecution(session, exec_id, path)

class UpdateInstallationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateInstallation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Installation(self, value):
        """
        Set the value of the Installation input for this Choreo. ((required, json) A JSON string containing the installation data. See documentation for syntax examples.)
        """
        InputSet._set_input(self, 'Installation', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        InputSet._set_input(self, 'ApplicationID', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the installation to update.)
        """
        InputSet._set_input(self, 'ObjectID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        InputSet._set_input(self, 'RESTAPIKey', value)

class UpdateInstallationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateInstallation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class UpdateInstallationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateInstallationResultSet(response, path)
