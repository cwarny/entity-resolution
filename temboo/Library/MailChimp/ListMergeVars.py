# -*- coding: utf-8 -*-

###############################################################################
#
# ListMergeVars
# Get field names from a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListMergeVars(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMergeVars Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListMergeVars')


    def new_input_set(self):
        return ListMergeVarsInputSet()

    def _make_result_set(self, result, path):
        return ListMergeVarsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMergeVarsChoreographyExecution(session, exec_id, path)

class ListMergeVarsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMergeVars
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the Mailchimp list associated with the merge vars to retrieve.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Indicates the desired format for the response. Accepted values are "json" or "xml" (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListMergeVarsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMergeVars Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Corresponds to the format specified in the ResponseFormat parameter. Defaults to "xml".)
        """
        return self._output.get('Response', None)

class ListMergeVarsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListMergeVarsResultSet(response, path)
