# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAuthenticatedPost
# Create a new post for the authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateAuthenticatedPost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAuthenticatedPost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/CreateAuthenticatedPost')


    def new_input_set(self):
        return CreateAuthenticatedPostInputSet()

    def _make_result_set(self, result, path):
        return CreateAuthenticatedPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAuthenticatedPostChoreographyExecution(session, exec_id, path)

class CreateAuthenticatedPostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAuthenticatedPost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) The date of the post, either in Unix timestamp format, or ISO datetime standard. You must be a moderator to do this.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_IPAddress(self, value):
        """
        Set the value of the IPAddress input for this Choreo. ((optional, string) The author's IP address. You must be a moderator to do this.)
        """
        InputSet._set_input(self, 'IPAddress', value)
    def set_ParentPost(self, value):
        """
        Set the value of the ParentPost input for this Choreo. ((conditional, string) The ID of a parent post to which the new post will be responding to. Either ParentPost, or Thread must be set, or both.)
        """
        InputSet._set_input(self, 'ParentPost', value)
    def set_PostContent(self, value):
        """
        Set the value of the PostContent input for this Choreo. ((required, string) The text of this post.)
        """
        InputSet._set_input(self, 'PostContent', value)
    def set_PostState(self, value):
        """
        Set the value of the PostState input for this Choreo. ((optional, string) Specify the state of the post (comment). Available options include: unapproved, approved, spam, killed. You must be a moderator to do this. If set, pre-approval validation will be skipped.)
        """
        InputSet._set_input(self, 'PostState', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Thread(self, value):
        """
        Set the value of the Thread input for this Choreo. ((conditional, string) The thread ID to attach the new post to. Either ParentPost, or Thread must be set, or both.)
        """
        InputSet._set_input(self, 'Thread', value)


class CreateAuthenticatedPostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAuthenticatedPost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class CreateAuthenticatedPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAuthenticatedPostResultSet(response, path)
