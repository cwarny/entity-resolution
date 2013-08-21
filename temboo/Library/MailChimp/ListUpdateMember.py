# -*- coding: utf-8 -*-

###############################################################################
#
# ListUpdateMember
# Update information for a member of a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListUpdateMember(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListUpdateMember Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListUpdateMember')


    def new_input_set(self):
        return ListUpdateMemberInputSet()

    def _make_result_set(self, result, path):
        return ListUpdateMemberResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUpdateMemberChoreographyExecution(session, exec_id, path)

class ListUpdateMemberInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListUpdateMember
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The current email address for the subscriber you want to update.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_EmailType(self, value):
        """
        Set the value of the EmailType input for this Choreo. ((optional, string) Must be one of 'text', 'html', or 'mobile'. Defaults to html.)
        """
        InputSet._set_input(self, 'EmailType', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the list that the existing subsbriber belongs to.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_Merge1(self, value):
        """
        Set the value of the Merge1 input for this Choreo. ((optional, string) Corresponds to the first merge var field defined in your account.)
        """
        InputSet._set_input(self, 'Merge1', value)
    def set_Merge2(self, value):
        """
        Set the value of the Merge2 input for this Choreo. ((optional, string) Corresponds to the second merge var field defined in your account.)
        """
        InputSet._set_input(self, 'Merge2', value)
    def set_Merge3(self, value):
        """
        Set the value of the Merge3 input for this Choreo. ((optional, string) Corresponds to the third merge var field defined in your account.)
        """
        InputSet._set_input(self, 'Merge3', value)
    def set_Merge4(self, value):
        """
        Set the value of the Merge4 input for this Choreo. ((optional, string) Corresponds to the fourth merge var field defined in your account.)
        """
        InputSet._set_input(self, 'Merge4', value)
    def set_NewEmail(self, value):
        """
        Set the value of the NewEmail input for this Choreo. ((optional, multiline) Set this to update the email address of a subscriber.)
        """
        InputSet._set_input(self, 'NewEmail', value)
    def set_ReplaceInterests(self, value):
        """
        Set the value of the ReplaceInterests input for this Choreo. ((optional, boolean) A flag to determine whether to replace the interest groups with the groups provided or add the provided groups to the member's interest groups. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        InputSet._set_input(self, 'ReplaceInterests', value)

class ListUpdateMemberResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListUpdateMember Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        return self._output.get('Response', None)

class ListUpdateMemberChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListUpdateMemberResultSet(response, path)
