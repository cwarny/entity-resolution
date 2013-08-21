# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteApplication
# Deletes an application from your Twilio account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteApplication(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteApplication Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/Applications/DeleteApplication')


    def new_input_set(self):
        return DeleteApplicationInputSet()

    def _make_result_set(self, result, path):
        return DeleteApplicationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteApplicationChoreographyExecution(session, exec_id, path)

class DeleteApplicationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteApplication
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AccountSID', value)
    def set_ApplicationSID(self, value):
        """
        Set the value of the ApplicationSID input for this Choreo. ((required, string) The id of the application to retrieve.)
        """
        InputSet._set_input(self, 'ApplicationSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AuthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class DeleteApplicationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteApplication Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class DeleteApplicationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteApplicationResultSet(response, path)
