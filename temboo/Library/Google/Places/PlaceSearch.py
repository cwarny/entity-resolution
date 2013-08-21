# -*- coding: utf-8 -*-

###############################################################################
#
# PlaceSearch
# Search for places based on latitude/longitude coordinates, keywords, and distance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PlaceSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PlaceSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Places/PlaceSearch')


    def new_input_set(self):
        return PlaceSearchInputSet()

    def _make_result_set(self, result, path):
        return PlaceSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PlaceSearchChoreographyExecution(session, exec_id, path)

class PlaceSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PlaceSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) Enter your Google API key.)
        """
        InputSet._set_input(self, 'Key', value)
    def set_Keyword(self, value):
        """
        Set the value of the Keyword input for this Choreo. ((optional, string) Enter a keyword (term, address, type, customer review, etc.) to be matched against all results retrieved for this Place.)
        """
        InputSet._set_input(self, 'Keyword', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Set the language in which to return restults.  A list of supported languages is available here: https://spreadsheets.google.com/pub?key=p9pdwsai2hDMsLkXsoM05KQ&gid=1)
        """
        InputSet._set_input(self, 'Language', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, string) Specify a latitude point around which Places results will be retrieved.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, string) Specify a longitude point around which Places results will be retrieved.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) Enter a name to be matched when results are retrieved for this specified Place.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) Specify the radius in meters, for which Places results will be returned. Maximum radius is limited to 50,000 meters. If rankby=distance, then radius must not be specified.)
        """
        InputSet._set_input(self, 'Radius', value)
    def set_RankBy(self, value):
        """
        Set the value of the RankBy input for this Choreo. ((optional, string) Specify how results are listed. Values include: prominence (default); distance - sorts results by distance from specified location. Radius must not be used, and Keyword, Name, or Types are required).)
        """
        InputSet._set_input(self, 'RankBy', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'Sensor', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((optional, string) Filter results by types, such as: bar, dentist.  Multiple types must be separated by the pipe ("|") symbol: bar|dentist||airport.)
        """
        InputSet._set_input(self, 'Types', value)

class PlaceSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PlaceSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)

class PlaceSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PlaceSearchResultSet(response, path)
