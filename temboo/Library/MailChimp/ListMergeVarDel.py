# -*- coding: utf-8 -*-

###############################################################################
#
# ListMergeVarDel
# Remove a field name from a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListMergeVarDel(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMergeVarDel Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListMergeVarDel')


    def new_input_set(self):
        return ListMergeVarDelInputSet()

    def _make_result_set(self, result, path):
        return ListMergeVarDelResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMergeVarDelChoreographyExecution(session, exec_id, path)

class ListMergeVarDelInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMergeVarDel
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the Mailchimp list associated with the merge var you want to delete.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((required, string) Provide a valid merge var tag. A merge var tag can be retrieved by calling listMergeVars() or by logging in to your account.)
        """
        InputSet._set_input(self, 'Tag', value)

class ListMergeVarDelResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMergeVarDel Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Returns the string "true" for success and an error description for failures.)
        """
        return self._output.get('Response', None)

class ListMergeVarDelChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListMergeVarDelResultSet(response, path)
