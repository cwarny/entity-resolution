# -*- coding: utf-8 -*-

###############################################################################
#
# SearchLocations
# Searches for locations by geographic coordinates. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchLocations(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchLocations Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/SearchLocations')


    def new_input_set(self):
        return SearchLocationsInputSet()

    def _make_result_set(self, result, path):
        return SearchLocationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchLocationsChoreographyExecution(session, exec_id, path)

class SearchLocationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchLocations
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, integer) The distance to search. Default is 1000m (distance=1000), max distance is 5000.)
        """
        InputSet._set_input(self, 'Distance', value)
    def set_FoursquareID(self, value):
        """
        Set the value of the FoursquareID input for this Choreo. ((conditional, string) Returns a location mapped off of a foursquare v2 api location id. If used, you are not required to provide values for Latitude or Longitude.)
        """
        InputSet._set_input(self, 'FoursquareID', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) Latitude of the center search coordinate. If used, Longitude is required.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) Longitude of the center search coordinate. If used, Latitude is required.)
        """
        InputSet._set_input(self, 'Longitude', value)

class SearchLocationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchLocations Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class SearchLocationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchLocationsResultSet(response, path)
