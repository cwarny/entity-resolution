# -*- coding: utf-8 -*-

###############################################################################
#
# ListThreads
# Returns a list of trending threads.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListThreads(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListThreads Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Trends/ListThreads')


    def new_input_set(self):
        return ListThreadsInputSet()

    def _make_result_set(self, result, path):
        return ListThreadsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListThreadsChoreographyExecution(session, exec_id, path)

class ListThreadsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListThreads
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid OAuth 2.0 access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) The name of a callback function to wrap the respone in. Used when setting ResponseFormat to "jsonp".)
        """
        InputSet._set_input(self, 'Callback', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, string) Allows you to look up a forum by ID (aka the short name).)
        """
        InputSet._set_input(self, 'Forum', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of records to return. Defaults to 10.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_Related(self, value):
        """
        Set the value of the Related input for this Choreo. ((optional, string) Indicates the relations to include with your response. Valid values are: forum, author, category.)
        """
        InputSet._set_input(self, 'Related', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListThreadsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListThreads Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class ListThreadsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListThreadsResultSet(response, path)
