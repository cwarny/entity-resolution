# -*- coding: utf-8 -*-

###############################################################################
#
# GetPhotoLocation
# Retrieves geo data (including latitude and longitude coordinates) for a specified photo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPhotoLocation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPhotoLocation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Geo/GetPhotoLocation')


    def new_input_set(self):
        return GetPhotoLocationInputSet()

    def _make_result_set(self, result, path):
        return GetPhotoLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPhotoLocationChoreographyExecution(session, exec_id, path)

class GetPhotoLocationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPhotoLocation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id of the photo that you want to get the location for.)
        """
        InputSet._set_input(self, 'PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetPhotoLocationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPhotoLocation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class GetPhotoLocationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPhotoLocationResultSet(response, path)
