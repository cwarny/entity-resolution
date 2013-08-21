# -*- coding: utf-8 -*-

###############################################################################
#
# ListSubscribe
# Adds a subscriber to a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListSubscribe(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListSubscribe Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListSubscribe')


    def new_input_set(self):
        return ListSubscribeInputSet()

    def _make_result_set(self, result, path):
        return ListSubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListSubscribeChoreographyExecution(session, exec_id, path)

class ListSubscribeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListSubscribe
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DoubleOptIn(self, value):
        """
        Set the value of the DoubleOptIn input for this Choreo. ((optional, boolean) Flag to control whether a double opt-in confirmation message is sent. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        InputSet._set_input(self, 'DoubleOptIn', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((conditional, string) The email address for the subscriber you want to create. Required unless the email address is included in the MergeVars input as part of your JSON object.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_EmailType(self, value):
        """
        Set the value of the EmailType input for this Choreo. ((optional, string) Must be one of 'text', 'html', or 'mobile'. Defaults to html.)
        """
        InputSet._set_input(self, 'EmailType', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the list that the subsbriber will be added to.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_MergeVars(self, value):
        """
        Set the value of the MergeVars input for this Choreo. ((conditional, json) A JSON object of the merge fields for this subscriber. If the subscriber email address is not provided for the EmailAddress input, it must be specified here.)
        """
        InputSet._set_input(self, 'MergeVars', value)
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
    def set_UpdateExisting(self, value):
        """
        Set the value of the UpdateExisting input for this Choreo. ((optional, boolean) Indicates that if the email already exists, this request will perform an update instead of an insert. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        InputSet._set_input(self, 'UpdateExisting', value)

class ListSubscribeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListSubscribe Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        return self._output.get('Response', None)

class ListSubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListSubscribeResultSet(response, path)
