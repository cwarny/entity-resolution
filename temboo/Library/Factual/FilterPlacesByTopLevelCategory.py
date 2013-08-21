# -*- coding: utf-8 -*-

###############################################################################
#
# FilterPlacesByTopLevelCategory
# Find places by top-level category and near specified latitude, longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FilterPlacesByTopLevelCategory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FilterPlacesByTopLevelCategory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Factual/FilterPlacesByTopLevelCategory')


    def new_input_set(self):
        return FilterPlacesByTopLevelCategoryInputSet()

    def _make_result_set(self, result, path):
        return FilterPlacesByTopLevelCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterPlacesByTopLevelCategoryChoreographyExecution(session, exec_id, path)

class FilterPlacesByTopLevelCategoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FilterPlacesByTopLevelCategory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Factual (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((optional, string) The API Secret provided by Factual (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((required, string) Enter a Factual top-level category to narrow the search results. See Choreo doc for a list of Factual top-level categories.)
        """
        InputSet._set_input(self, 'Category', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Enter latitude coordinates of the location defining the center of the search radius.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Enter longitude coordinates of the location defining the center of the search radius.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search string (i.e. Starbucks))
        """
        InputSet._set_input(self, 'Query', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((required, integer) Provide the radius (in meters, and centered on the latitude-longitude coordinates specified) for which search results will be returned.)
        """
        InputSet._set_input(self, 'Radius', value)

class FilterPlacesByTopLevelCategoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FilterPlacesByTopLevelCategory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Factual.)
        """
        return self._output.get('Response', None)

class FilterPlacesByTopLevelCategoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FilterPlacesByTopLevelCategoryResultSet(response, path)
