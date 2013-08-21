# -*- coding: utf-8 -*-

###############################################################################
#
# GetNearbyContacts
# Searches Foursquare recent check-ins and the Facebook social graph with a given set of Geo coordinates
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetNearbyContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNearbyContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/Social/GetNearbyContacts')


    def new_input_set(self):
        return GetNearbyContactsInputSet()

    def _make_result_set(self, result, path):
        return GetNearbyContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNearbyContactsChoreographyExecution(session, exec_id, path)

class GetNearbyContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNearbyContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((required, json) A JSON dictionary containing Facebook and Foursquare credentials.)
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_AfterTimestamp(self, value):
        """
        Set the value of the AfterTimestamp input for this Choreo. ((optional, date) Seconds after which to look for checkins, e.g. for looking for new checkins since the last fetch.)
        """
        InputSet._set_input(self, 'AfterTimestamp', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate of the location to search for.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Used to page through results. Limits the number of records returned in the API responses.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) The longitude coordinate of the location to search for.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through Facebook results. Returns results starting from the specified number.)
        """
        InputSet._set_input(self, 'Offset', value)

class GetNearbyContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNearbyContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) A merged result of Foursquare and Facebook location based searches.)
        """
        return self._output.get('Response', None)

class GetNearbyContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNearbyContactsResultSet(response, path)
