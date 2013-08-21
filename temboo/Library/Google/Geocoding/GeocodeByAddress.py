# -*- coding: utf-8 -*-

###############################################################################
#
# GeocodeByAddress
# Converts a human-readable address into geographic coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GeocodeByAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GeocodeByAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Geocoding/GeocodeByAddress')


    def new_input_set(self):
        return GeocodeByAddressInputSet()

    def _make_result_set(self, result, path):
        return GeocodeByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GeocodeByAddressChoreographyExecution(session, exec_id, path)

class GeocodeByAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GeocodeByAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The address that you want to geocode.)
        """
        InputSet._set_input(self, 'Address', value)
    def set_Bounds(self, value):
        """
        Set the value of the Bounds input for this Choreo. ((optional, string) The bounding box of the viewport within which to bias geocode results more prominently.)
        """
        InputSet._set_input(self, 'Bounds', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) The language in which to return results. Defaults to 'en' (English).)
        """
        InputSet._set_input(self, 'Language', value)
    def set_Region(self, value):
        """
        Set the value of the Region input for this Choreo. ((optional, string) The region code, specified as a ccTLD ("top-level domain") two-character value. Defaults to 'us' (United States).)
        """
        InputSet._set_input(self, 'Region', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the geocoding request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'Sensor', value)

class GeocodeByAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GeocodeByAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Latitude(self):
        """
        Retrieve the value for the "Latitude" output from this Choreo execution. ((decimal) The latitude coordinate associated with the address provided.)
        """
        return self._output.get('Latitude', None)
    def get_Longitude(self):
        """
        Retrieve the value for the "Longitude" output from this Choreo execution. ((decimal) The longitude coordinate associated with the address provided.)
        """
        return self._output.get('Longitude', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)

class GeocodeByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GeocodeByAddressResultSet(response, path)
