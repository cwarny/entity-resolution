# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveActivity
# Retrieves a page of a user’s activity history or information for a past activity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/FitnessActivities/RetrieveActivity')


    def new_input_set(self):
        return RetrieveActivityInputSet()

    def _make_result_set(self, result, path):
        return RetrieveActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveActivityChoreographyExecution(session, exec_id, path)

class RetrieveActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ActivityID(self, value):
        """
        Set the value of the ActivityID input for this Choreo. ((required, string) This can be the individual id of the activity, or you can pass the full uri for the activity as returned from the RetrieveActivites Choreo (i.e. /fitnessActivities/125927913).)
        """
        InputSet._set_input(self, 'ActivityID', value)

class RetrieveActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class RetrieveActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveActivityResultSet(response, path)
