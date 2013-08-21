# -*- coding: utf-8 -*-

###############################################################################
#
# Lists
# Get all lists from a MailChimp account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Lists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Lists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/Lists')


    def new_input_set(self):
        return ListsInputSet()

    def _make_result_set(self, result, path):
        return ListsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListsChoreographyExecution(session, exec_id, path)

class ListsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Lists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Indicates the desired format for the response. Accepted values are "json" or "xml" (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Lists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Corresponds to the format specified in the ResponseFormat parameter. Defaults to "xml".)
        """
        return self._output.get('Response', None)

class ListsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListsResultSet(response, path)
