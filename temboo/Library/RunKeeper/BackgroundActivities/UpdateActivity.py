# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateActivity
# Updates a background activity in a user's feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/BackgroundActivities/UpdateActivity')


    def new_input_set(self):
        return UpdateActivityInputSet()

    def _make_result_set(self, result, path):
        return UpdateActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateActivityChoreographyExecution(session, exec_id, path)

class UpdateActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Activity(self, value):
        """
        Set the value of the Activity input for this Choreo. ((required, json) A JSON string containing the key/value pairs for the activity to update. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'Activity', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ActivityID(self, value):
        """
        Set the value of the ActivityID input for this Choreo. ((required, string) This can be the individual id of the activity, or you can pass the full uri for the activity as returned from the RetrieveActivities Choreo (i.e. /backgroundActivities/-12985593-1351022400000).)
        """
        InputSet._set_input(self, 'ActivityID', value)

class UpdateActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class UpdateActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateActivityResultSet(response, path)
