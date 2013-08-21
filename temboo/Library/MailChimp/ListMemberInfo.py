# -*- coding: utf-8 -*-

###############################################################################
#
# ListMemberInfo
# Get information for a member of a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListMemberInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMemberInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListMemberInfo')


    def new_input_set(self):
        return ListMemberInfoInputSet()

    def _make_result_set(self, result, path):
        return ListMemberInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMemberInfoChoreographyExecution(session, exec_id, path)

class ListMemberInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMemberInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address to use when searching for a Mailchimp member.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the Mailchimp list associated with the member you want to retrieve.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Indicates the desired format for the response. Accepted values are "json" or "xml" (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListMemberInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMemberInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Corresponds to the format specified in the ResponseFormat parameter. Defaults to "xml".)
        """
        return self._output.get('Response', None)

class ListMemberInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListMemberInfoResultSet(response, path)
