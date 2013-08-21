# -*- coding: utf-8 -*-

###############################################################################
#
# ListUnsubscribe
# Remove a subscriber from a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListUnsubscribe(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListUnsubscribe Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListUnsubscribe')


    def new_input_set(self):
        return ListUnsubscribeInputSet()

    def _make_result_set(self, result, path):
        return ListUnsubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUnsubscribeChoreographyExecution(session, exec_id, path)

class ListUnsubscribeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListUnsubscribe
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DeleteMember(self, value):
        """
        Set the value of the DeleteMember input for this Choreo. ((optional, boolean) A flag used to completely delete the member from your list instead of just unsubscribing. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'DeleteMember', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address to unsubscribe.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the list that contains the email address you want to unsubscribe.)
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

class ListUnsubscribeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListUnsubscribe Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        return self._output.get('Response', None)

class ListUnsubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListUnsubscribeResultSet(response, path)
