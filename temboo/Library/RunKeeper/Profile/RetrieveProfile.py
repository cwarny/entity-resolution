# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveProfile
# Returns a user's profile information including the user’s identity, geographical location, and fitness goals.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Profile/RetrieveProfile')


    def new_input_set(self):
        return RetrieveProfileInputSet()

    def _make_result_set(self, result, path):
        return RetrieveProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveProfileChoreographyExecution(session, exec_id, path)

class RetrieveProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)

class RetrieveProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class RetrieveProfileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveProfileResultSet(response, path)
