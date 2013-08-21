# -*- coding: utf-8 -*-

###############################################################################
#
# UserPlaceReports
# Add a new Place to Google Places.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UserPlaceReports(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserPlaceReports Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Places/UserPlaceReports')


    def new_input_set(self):
        return UserPlaceReportsInputSet()

    def _make_result_set(self, result, path):
        return UserPlaceReportsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserPlaceReportsChoreographyExecution(session, exec_id, path)

class UserPlaceReportsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserPlaceReports
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_POSTForm(self, value):
        """
        Set the value of the POSTForm input for this Choreo. ((required, any) Enter the required POST parameter, reference in the body of this JSON form.)
        """
        InputSet._set_input(self, 'POSTForm', value)
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) Enter your Google API key.)
        """
        InputSet._set_input(self, 'Key', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'Sensor', value)

class UserPlaceReportsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserPlaceReports Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)

class UserPlaceReportsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserPlaceReportsResultSet(response, path)
