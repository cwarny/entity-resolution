# -*- coding: utf-8 -*-

###############################################################################
#
# WriteLocationData
# Allows you to easily update the location data of your feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class WriteLocationData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WriteLocationData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/WriteLocationData')


    def new_input_set(self):
        return WriteLocationDataInputSet()

    def _make_result_set(self, result, path):
        return WriteLocationDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WriteLocationDataChoreographyExecution(session, exec_id, path)

class WriteLocationDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WriteLocationData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Disposition(self, value):
        """
        Set the value of the Disposition input for this Choreo. ((optional, string) Can be set to "mobile" to enable creating waypoints (lat, lon and elevation with timestamp), or "fixed" (default) for a single location. Leave empty to keep existing settings.)
        """
        InputSet._set_input(self, 'Disposition', value)
    def set_Domain(self, value):
        """
        Set the value of the Domain input for this Choreo. ((optional, string) The domain of the location, i.e. physical or virtual. Leave empty to keep existing Domain. Type "BLANK" to clear existing Domain. Ex: "physical".)
        """
        InputSet._set_input(self, 'Domain', value)
    def set_Elevation(self, value):
        """
        Set the value of the Elevation input for this Choreo. ((optional, decimal) Elevation in meters. Leave empty to keep previously existing Elevation. Type "BLANK" to clear existing Elevation. Ex: 20.5.)
        """
        InputSet._set_input(self, 'Elevation', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID for the feed that you would like to update.)
        """
        InputSet._set_input(self, 'FeedID', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) Latitude coordinates. Leave empty to keep previously existing Latitude. Type "BLANK" to clear existing Latitude. Ex: 40.728194.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) Longitude coordinates. Leave empty to keep previously existing Location. Type "BLANK" to clear existing settings. Ex: -73.957316.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) Name of Location. Leave empty to keep existing Location. Type "BLANK" to clear existing settings. Ex.: "My Fitbit Tracker".)
        """
        InputSet._set_input(self, 'Name', value)

class WriteLocationDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WriteLocationData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful feed location update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class WriteLocationDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WriteLocationDataResultSet(response, path)
