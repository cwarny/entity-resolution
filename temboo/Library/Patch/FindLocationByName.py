# -*- coding: utf-8 -*-

###############################################################################
#
# FindLocationByName
# Return Patch location information for a specified U.S. region.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindLocationByName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindLocationByName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Patch/FindLocationByName')


    def new_input_set(self):
        return FindLocationByNameInputSet()

    def _make_result_set(self, result, path):
        return FindLocationByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindLocationByNameChoreographyExecution(session, exec_id, path)

class FindLocationByNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindLocationByName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) A valid API key provided by Patch.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API shared secret provided by Patch.)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Specify a maximum number of locations to return, between 1 and 100. The default is 10.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_RegionName(self, value):
        """
        Set the value of the RegionName input for this Choreo. ((required, string) Enter a state, city, neighborhood, district (county), locality (borough), or metro area name; a place name, such as a business, landmark, or park; or a ZIP code. Separate multiple names with commas.)
        """
        InputSet._set_input(self, 'RegionName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify "xml" to convert the Patch JSON response to XML, or "json" (the default) to not convert.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class FindLocationByNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindLocationByName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Coordinates(self):
        """
        Retrieve the value for the "Coordinates" output from this Choreo execution. ((string) The concatenated location latitude and longitude returned by Patch.)
        """
        return self._output.get('Coordinates', None)
    def get_Latitude(self):
        """
        Retrieve the value for the "Latitude" output from this Choreo execution. ((decimal) The latitude for the location returned by Patch.)
        """
        return self._output.get('Latitude', None)
    def get_LocationID(self):
        """
        Retrieve the value for the "LocationID" output from this Choreo execution. ((string) )
        """
        return self._output.get('LocationID', None)
    def get_Longitude(self):
        """
        Retrieve the value for the "Longitude" output from this Choreo execution. ((decimal) The longitude for the location returned by Patch.)
        """
        return self._output.get('Longitude', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response returned from Patch.)
        """
        return self._output.get('Response', None)

class FindLocationByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindLocationByNameResultSet(response, path)
