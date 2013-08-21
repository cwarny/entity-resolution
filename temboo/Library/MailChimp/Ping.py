# -*- coding: utf-8 -*-

###############################################################################
#
# Ping
# Test connection to MailChimp services.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Ping(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Ping Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/Ping')


    def new_input_set(self):
        return PingInputSet()

    def _make_result_set(self, result, path):
        return PingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PingChoreographyExecution(session, exec_id, path)

class PingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Ping
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp)
        """
        InputSet._set_input(self, 'APIKey', value)

class PingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Ping Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from Mailchimp.)
        """
        return self._output.get('Response', None)

class PingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PingResultSet(response, path)
