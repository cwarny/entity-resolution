# -*- coding: utf-8 -*-

###############################################################################
#
# ByFoursquare
# Retrieves weather and UV index data based on coordinates returned from a Foursquare recent check-in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ByFoursquare(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByFoursquare Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/GetWeather/ByFoursquare')


    def new_input_set(self):
        return ByFoursquareInputSet()

    def _make_result_set(self, result, path):
        return ByFoursquareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByFoursquareChoreographyExecution(session, exec_id, path)

class ByFoursquareInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByFoursquare
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((required, json) A JSON dictionary containing your Foursquare and Yahoo credentials. See Choreo documentation for formatting examples.)
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_Shout(self, value):
        """
        Set the value of the Shout input for this Choreo. ((optional, string) A message about your check-in. The maximum length of this field is 140 characters.)
        """
        InputSet._set_input(self, 'Shout', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((optional, string) The venue where the user is checking in. Required if creating a Foursquare checkin.)
        """
        InputSet._set_input(self, 'VenueID', value)

class ByFoursquareResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByFoursquare Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) Contains weather information based on the coordinates returned from the Foursquare checkin.)
        """
        return self._output.get('Response', None)

class ByFoursquareChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByFoursquareResultSet(response, path)
