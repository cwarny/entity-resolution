# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveBlogInfo
# Returns general information about the blog, such as the title, number of posts, and other high-level data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveBlogInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveBlogInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/Blog/RetrieveBlogInfo')


    def new_input_set(self):
        return RetrieveBlogInfoInputSet()

    def _make_result_set(self, result, path):
        return RetrieveBlogInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveBlogInfoChoreographyExecution(session, exec_id, path)

class RetrieveBlogInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveBlogInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        InputSet._set_input(self, 'BaseHostname', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class RetrieveBlogInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveBlogInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class RetrieveBlogInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveBlogInfoResultSet(response, path)
