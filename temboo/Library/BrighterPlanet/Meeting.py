# -*- coding: utf-8 -*-

###############################################################################
#
# Meeting
# Returns facility operations emissions analysis for corporate and cultural events.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Meeting(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Meeting Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Meeting')


    def new_input_set(self):
        return MeetingInputSet()

    def _make_result_set(self, result, path):
        return MeetingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MeetingChoreographyExecution(session, exec_id, path)

class MeetingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Meeting
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Area(self, value):
        """
        Set the value of the Area input for this Choreo. ((optional, integer) Area of event venue in square meters.)
        """
        InputSet._set_input(self, 'Area', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) Date of event in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((optional, integer) Event duration in total seconds.)
        """
        InputSet._set_input(self, 'Duration', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Two-letter postal abbreviation for the state in which the meeting takes place (e.g. NY).)
        """
        InputSet._set_input(self, 'State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, integer) Five digit zip code in which the meeting takes place.)
        """
        InputSet._set_input(self, 'Zip', value)

class MeetingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Meeting Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class MeetingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MeetingResultSet(response, path)
