# -*- coding: utf-8 -*-

###############################################################################
#
# CreateMediaComment
# Creates a comment on a specified media object. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateMediaComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateMediaComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/CreateMediaComment')


    def new_input_set(self):
        return CreateMediaCommentInputSet()

    def _make_result_set(self, result, path):
        return CreateMediaCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateMediaCommentChoreographyExecution(session, exec_id, path)

class CreateMediaCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateMediaComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_MediaID(self, value):
        """
        Set the value of the MediaID input for this Choreo. ((required, integer) The ID of the media object that you want to get comments for. For example, a valid MediaID could be 3.)
        """
        InputSet._set_input(self, 'MediaID', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text to post as a comment on the media.)
        """
        InputSet._set_input(self, 'Text', value)

class CreateMediaCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateMediaComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class CreateMediaCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateMediaCommentResultSet(response, path)
