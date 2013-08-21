# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAnonymousPost
# Creates an anonymous post.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateAnonymousPost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAnonymousPost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/CreateAnonymousPost')


    def new_input_set(self):
        return CreateAnonymousPostInputSet()

    def _make_result_set(self, result, path):
        return CreateAnonymousPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAnonymousPostChoreographyExecution(session, exec_id, path)

class CreateAnonymousPostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAnonymousPost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AuthorEmail(self, value):
        """
        Set the value of the AuthorEmail input for this Choreo. ((required, string) The email address of the post author.)
        """
        InputSet._set_input(self, 'AuthorEmail', value)
    def set_AuthorName(self, value):
        """
        Set the value of the AuthorName input for this Choreo. ((optional, string) The name of the post author.)
        """
        InputSet._set_input(self, 'AuthorName', value)
    def set_AuthorURL(self, value):
        """
        Set the value of the AuthorURL input for this Choreo. ((optional, string) The URL of the author's Disqus profile.)
        """
        InputSet._set_input(self, 'AuthorURL', value)
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


class CreateAnonymousPostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAnonymousPost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class CreateAnonymousPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAnonymousPostResultSet(response, path)
