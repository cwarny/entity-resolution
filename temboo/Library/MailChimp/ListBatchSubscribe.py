# -*- coding: utf-8 -*-

###############################################################################
#
# ListBatchSubscribe
# Adds or updates multiple Mailchimp list subscribers.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListBatchSubscribe(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListBatchSubscribe Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListBatchSubscribe')


    def new_input_set(self):
        return ListBatchSubscribeInputSet()

    def _make_result_set(self, result, path):
        return ListBatchSubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBatchSubscribeChoreographyExecution(session, exec_id, path)

class ListBatchSubscribeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListBatchSubscribe
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DoubleOptIn(self, value):
        """
        Set the value of the DoubleOptIn input for this Choreo. ((optional, boolean) Flag to control whether a double opt-in confirmation message is sent. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'DoubleOptIn', value)
    def set_EmailType(self, value):
        """
        Set the value of the EmailType input for this Choreo. ((optional, string) Must be one of 'text', 'html', or 'mobile'. Defaults to html.)
        """
        InputSet._set_input(self, 'EmailType', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the Mailchimp list the subscribers will be added to.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_ReplaceInterests(self, value):
        """
        Set the value of the ReplaceInterests input for this Choreo. ((optional, boolean) A flag to determine whether to replace the interest groups with the groups provided or add the provided groups to the member's interest groups. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        InputSet._set_input(self, 'ReplaceInterests', value)
    def set_SendWelcome(self, value):
        """
        Set the value of the SendWelcome input for this Choreo. ((optional, boolean) If double_optin is false and this flag is true, a welcome email will be sent. Note that this does not apply when updating records. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'SendWelcome', value)
    def set_Subscribers(self, value):
        """
        Set the value of the Subscribers input for this Choreo. ((required, json) An array of JSON objects containing the subscribers to insert. See Choreo documentation for the specific format for this JSON input.)
        """
        InputSet._set_input(self, 'Subscribers', value)
    def set_SupressErrors(self, value):
        """
        Set the value of the SupressErrors input for this Choreo. ((optional, boolean) Whether or not to suppress errors that arise from attempting to add/update a subscriber. Defaults to 0 (false). Set to 1 (true) to supress errors.)
        """
        InputSet._set_input(self, 'SupressErrors', value)
    def set_UpdateExisting(self, value):
        """
        Set the value of the UpdateExisting input for this Choreo. ((optional, boolean) Indicates that if the email already exists, this request will perform an update instead of an insert. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        InputSet._set_input(self, 'UpdateExisting', value)

class ListBatchSubscribeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListBatchSubscribe Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ErrorList(self):
        """
        Retrieve the value for the "ErrorList" output from this Choreo execution. ((json) A list of emails that were not successfully subscribed.)
        """
        return self._output.get('ErrorList', None)
    def get_SuccessList(self):
        """
        Retrieve the value for the "SuccessList" output from this Choreo execution. ((json) A list of email successfully subscribed.)
        """
        return self._output.get('SuccessList', None)

class ListBatchSubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListBatchSubscribeResultSet(response, path)
