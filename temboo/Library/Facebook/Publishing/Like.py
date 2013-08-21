# -*- coding: utf-8 -*-

###############################################################################
#
# Like
# Allows a user to "like" a Graph API object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Like(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Like Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/Like')


    def new_input_set(self):
        return LikeInputSet()

    def _make_result_set(self, result, path):
        return LikeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LikeChoreographyExecution(session, exec_id, path)

class LikeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Like
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The id of a graph api object to like.)
        """
        InputSet._set_input(self, 'ObjectID', value)

class LikeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Like Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        return self._output.get('Response', None)

class LikeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LikeResultSet(response, path)
