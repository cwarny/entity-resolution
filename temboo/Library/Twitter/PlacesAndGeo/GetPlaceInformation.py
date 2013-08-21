# -*- coding: utf-8 -*-

###############################################################################
#
# GetPlaceInformation
# Searches for places that can be attached to a statuses/update using a latitude and a longitude pair, an IP address, or a name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPlaceInformation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPlaceInformation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/PlacesAndGeo/GetPlaceInformation')


    def new_input_set(self):
        return GetPlaceInformationInputSet()

    def _make_result_set(self, result, path):
        return GetPlaceInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPlaceInformationChoreographyExecution(session, exec_id, path)

class GetPlaceInformationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPlaceInformation
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
    def set_PlaceId(self, value):
        """
        Set the value of the PlaceId input for this Choreo. ((required, string) The id for a place in the world. These IDs can be retrieved from the ReverseGeocode Choreo.)
        """
        InputSet._set_input(self, 'PlaceId', value)

class GetPlaceInformationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPlaceInformation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class GetPlaceInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPlaceInformationResultSet(response, path)
