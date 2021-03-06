# -*- coding: utf-8 -*-

###############################################################################
#
# ByGoogleLat
# Retrieves weather and UV index data based on coordinates returned from Google Latitude.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ByGoogleLat(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByGoogleLat Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/GetWeather/ByGoogleLat')


    def new_input_set(self):
        return ByGoogleLatInputSet()

    def _make_result_set(self, result, path):
        return ByGoogleLatResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByGoogleLatChoreographyExecution(session, exec_id, path)

class ByGoogleLatInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByGoogleLat
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((required, json) A JSON dictionary containing your Google Latitude and Yahoo credentials. See Choreo documentation for formatting examples.)
        """
        InputSet._set_input(self, 'APICredentials', value)

class ByGoogleLatResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByGoogleLat Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) Contains weather information based on the coordinates returned from Google Latitude.)
        """
        return self._output.get('Response', None)

class ByGoogleLatChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByGoogleLatResultSet(response, path)
