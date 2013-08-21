# -*- coding: utf-8 -*-

###############################################################################
#
# ListRecordings
# Returns a list of recordings generated during a call.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListRecordings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListRecordings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/Calls/ListRecordings')


    def new_input_set(self):
        return ListRecordingsInputSet()

    def _make_result_set(self, result, path):
        return ListRecordingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListRecordingsChoreographyExecution(session, exec_id, path)

class ListRecordingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListRecordings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AuthToken', value)
    def set_CallSID(self, value):
        """
        Set the value of the CallSID input for this Choreo. ((required, string) The unique id of the call to retrieve a list of recordings for.)
        """
        InputSet._set_input(self, 'CallSID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with the call. If not specified, the main AccountSID used to authenticate is used in request.)
        """
        InputSet._set_input(self, 'SubAccountSID', value)

class ListRecordingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListRecordings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListRecordingsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListRecordingsResultSet(response, path)
