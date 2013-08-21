# -*- coding: utf-8 -*-

###############################################################################
#
# VoteOnPost
# Register a vote on a post.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class VoteOnPost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VoteOnPost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/VoteOnPost')


    def new_input_set(self):
        return VoteOnPostInputSet()

    def _make_result_set(self, result, path):
        return VoteOnPostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VoteOnPostChoreographyExecution(session, exec_id, path)

class VoteOnPostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VoteOnPost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_PostID(self, value):
        """
        Set the value of the PostID input for this Choreo. ((required, integer) The post ID for which a vote is being registered.)
        """
        InputSet._set_input(self, 'PostID', value)
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
    def set_Vote(self, value):
        """
        Set the value of the Vote input for this Choreo. ((required, integer) A numeric value for your vote. Valid choices are: -1, 0, or 1.)
        """
        InputSet._set_input(self, 'Vote', value)


class VoteOnPostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VoteOnPost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class VoteOnPostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VoteOnPostResultSet(response, path)
