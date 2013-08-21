# -*- coding: utf-8 -*-

###############################################################################
#
# ListCalls
# Retrieves a list of phone calls made to and from the specified account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListCalls(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListCalls Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/Calls/ListCalls')


    def new_input_set(self):
        return ListCallsInputSet()

    def _make_result_set(self, result, path):
        return ListCallsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCallsChoreographyExecution(session, exec_id, path)

class ListCallsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListCalls
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
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((optional, string) Fillters results for calls from this phone number or Client identifier.)
        """
        InputSet._set_input(self, 'From', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        InputSet._set_input(self, 'PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_ParentCallSID(self, value):
        """
        Set the value of the ParentCallSID input for this Choreo. ((optional, string) Filters results for calls spawned by the call with this Sid.)
        """
        InputSet._set_input(self, 'ParentCallSID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((optional, string) Filters results for calls that started on this date, given as YYYY-MM-DD. Also supports operators such as >= or <=.)
        """
        InputSet._set_input(self, 'StartTime', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) Fillters results for calls currently in this status. Valid values are: queued, ringing, in-progress, completed, failed, busy, or no-answer.)
        """
        InputSet._set_input(self, 'Status', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount to retrieve calls for. If not specified, the main AccountSID used to authenticate is used in request.)
        """
        InputSet._set_input(self, 'SubAccountSID', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((optional, string) Fillters results for calls to this phone number or Client identifier.)
        """
        InputSet._set_input(self, 'To', value)

class ListCallsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListCalls Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListCallsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListCallsResultSet(response, path)
