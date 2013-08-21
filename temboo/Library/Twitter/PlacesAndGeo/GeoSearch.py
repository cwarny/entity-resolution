# -*- coding: utf-8 -*-

###############################################################################
#
# GeoSearch
# Searches for places that can be attached to a status update using a latitude and a longitude pair, an IP address, or a name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GeoSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GeoSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/PlacesAndGeo/GeoSearch')


    def new_input_set(self):
        return GeoSearchInputSet()

    def _make_result_set(self, result, path):
        return GeoSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GeoSearchChoreographyExecution(session, exec_id, path)

class GeoSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GeoSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, string) A hint on the "region" in which to search. If a number, then this is a radius in meters. You can also specify feet by using the ft suffix (i.e. 5ft).)
        """
        InputSet._set_input(self, 'Accuracy', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) If supplied, the response will use the JSONP format with a callback of the given name.)
        """
        InputSet._set_input(self, 'Callback', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_ContainedWithin(self, value):
        """
        Set the value of the ContainedWithin input for this Choreo. ((optional, string) This is the place_id which you would like to restrict the search results to. This id can be retrieved with the GetPlaceInformation Choreo.)
        """
        InputSet._set_input(self, 'ContainedWithin', value)
    def set_Granularity(self, value):
        """
        Set the value of the Granularity input for this Choreo. ((optional, string) This is the minimal granularity of place types to return and must be one of: poi, neighborhood, city, admin or country. Defaults to neighborhood.)
        """
        InputSet._set_input(self, 'Granularity', value)
    def set_IP(self, value):
        """
        Set the value of the IP input for this Choreo. ((conditional, string) An IP address. Used when attempting to fix geolocation based off of the user's IP address. You must provide Latitude and Longitude, IP, or Query.)
        """
        InputSet._set_input(self, 'IP', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) The latitude to search around. You must provide Latitude and Longitude, IP, or Query.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) The longitude to search around. You must provide Latitude and Longitude, IP, or Query.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        InputSet._set_input(self, 'MaxResults', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) Free-form text to match against while executing a geo-based query. You must provide Latitude and Longitude, IP, or Query.)
        """
        InputSet._set_input(self, 'Query', value)

class GeoSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GeoSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class GeoSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GeoSearchResultSet(response, path)
