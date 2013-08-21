# -*- coding: utf-8 -*-

###############################################################################
#
# LogActivity
# Log a new activity for a particular date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class LogActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LogActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/Activities/LogActivity')


    def new_input_set(self):
        return LogActivityInputSet()

    def _make_result_set(self, result, path):
        return LogActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogActivityChoreographyExecution(session, exec_id, path)

class LogActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LogActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ActivityID(self, value):
        """
        Set the value of the ActivityID input for this Choreo. ((conditional, integer) This can be the id of the activity, directory activity, or intensity level activity.)
        """
        InputSet._set_input(self, 'ActivityID', value)
    def set_ActivityName(self, value):
        """
        Set the value of the ActivityName input for this Choreo. ((conditional, string) Custom activity name; either activityId or activityName should be provided.)
        """
        InputSet._set_input(self, 'ActivityName', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Fitbit.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) The date that corresponds with the new log entry (in the format yyyy-MM-dd).)
        """
        InputSet._set_input(self, 'Date', value)
    def set_DistanceUnit(self, value):
        """
        Set the value of the DistanceUnit input for this Choreo. ((conditional, string) Corresponds with the Distance parameter (i.e. Mile). See Choreo documentation for links to unit charts.)
        """
        InputSet._set_input(self, 'DistanceUnit', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((conditional, decimal) The activity distance. Used when activityId corresponds to 'Running'  or 'Walking' for example.)
        """
        InputSet._set_input(self, 'Distance', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((required, integer) The duration of the activity in milliseconds.)
        """
        InputSet._set_input(self, 'Duration', value)
    def set_ManualCalories(self, value):
        """
        Set the value of the ManualCalories input for this Choreo. ((conditional, integer) The amount of calories defined manually; required when using the ActivityName parameter, otherwise optional.)
        """
        InputSet._set_input(self, 'ManualCalories', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in: xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_StartTime(self, value):
        """
        Set the value of the StartTime input for this Choreo. ((required, string) The hour and minutes for the start of the activity formatted like HH:mm.)
        """
        InputSet._set_input(self, 'StartTime', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided.)
        """
        InputSet._set_input(self, 'UserID', value)

class LogActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LogActivity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Fitbit.)
        """
        return self._output.get('Response', None)

class LogActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LogActivityResultSet(response, path)
