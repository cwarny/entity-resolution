# -*- coding: utf-8 -*-

###############################################################################
#
# RecordActivity
# Records a newly-completed strength training activity, or begins recording an activity still in progress.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RecordActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RecordActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/StrengthTrainingActivities/RecordActivity')


    def new_input_set(self):
        return RecordActivityInputSet()

    def _make_result_set(self, result, path):
        return RecordActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecordActivityChoreographyExecution(session, exec_id, path)

class RecordActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RecordActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Activity(self, value):
        """
        Set the value of the Activity input for this Choreo. ((required, json) A JSON string containing the key/value pairs for the activity to create. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'Activity', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)

class RecordActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RecordActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) Contains the string "true" when an activity is created successfully.)
        """
        return self._output.get('Response', None)
    def get_URI(self):
        """
        Retrieve the value for the "URI" output from this Choreo execution. ((string) The activity uri that was created.)
        """
        return self._output.get('URI', None)

class RecordActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RecordActivityResultSet(response, path)
