# -*- coding: utf-8 -*-

###############################################################################
#
# ListBatchUnsubscribe
# Unsubscribes one or more members from a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListBatchUnsubscribe(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListBatchUnsubscribe Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListBatchUnsubscribe')


    def new_input_set(self):
        return ListBatchUnsubscribeInputSet()

    def _make_result_set(self, result, path):
        return ListBatchUnsubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBatchUnsubscribeChoreographyExecution(session, exec_id, path)

class ListBatchUnsubscribeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListBatchUnsubscribe
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DeleteMember(self, value):
        """
        Set the value of the DeleteMember input for this Choreo. ((optional, boolean) A flag used to completely delete the member from your list instead of just unsubscribing. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'DeleteMember', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address to unsubscribe from a Mailchimp list . Multiple emails can be supplied separated by commas.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The Mailchimp List ID)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_SendGoodbye(self, value):
        """
        Set the value of the SendGoodbye input for this Choreo. ((optional, boolean) A flag used to send the goodbye email to the email address. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'SendGoodbye', value)
    def set_SendNotify(self, value):
        """
        Set the value of the SendNotify input for this Choreo. ((optional, boolean) A flag used to send the unsubscribe notification email to the address defined in the list email notification settings. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'SendNotify', value)
    def set_SupressErrors(self, value):
        """
        Set the value of the SupressErrors input for this Choreo. ((optional, boolean) Whether or not to suppress errors that arise from attempting to unsubscribe an email address. Defaults to 0 (false). Set to 1 (true) to supress errors.)
        """
        InputSet._set_input(self, 'SupressErrors', value)

class ListBatchUnsubscribeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListBatchUnsubscribe Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ErrorList(self):
        """
        Retrieve the value for the "ErrorList" output from this Choreo execution. ((json) A list of emails that were not successfully unsubscribed.)
        """
        return self._output.get('ErrorList', None)
    def get_SuccessList(self):
        """
        Retrieve the value for the "SuccessList" output from this Choreo execution. ((json) A list of email successfully unsubscribed.)
        """
        return self._output.get('SuccessList', None)

class ListBatchUnsubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListBatchUnsubscribeResultSet(response, path)
