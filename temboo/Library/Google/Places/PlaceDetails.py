# -*- coding: utf-8 -*-

###############################################################################
#
# PlaceDetails
# Retrieve detailed information about places retrieved by the PlaceSearch Choreo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PlaceDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PlaceDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Places/PlaceDetails')


    def new_input_set(self):
        return PlaceDetailsInputSet()

    def _make_result_set(self, result, path):
        return PlaceDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PlaceDetailsChoreographyExecution(session, exec_id, path)

class PlaceDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PlaceDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) Enter your Google API key.)
        """
        InputSet._set_input(self, 'Key', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Set the language in which to return restults.  A list of supported languages is available here: https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
        """
        InputSet._set_input(self, 'Language', value)
    def set_Reference(self, value):
        """
        Set the value of the Reference input for this Choreo. ((required, string) Enter a textual identifier that uniquely identidies a place obtained from the PlaceSearch Choreo.)
        """
        InputSet._set_input(self, 'Reference', value)
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

class PlaceDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PlaceDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)

class PlaceDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PlaceDetailsResultSet(response, path)
