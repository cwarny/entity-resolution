# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByBoundingBox
# Retrieve businesses in a geographic bounding box.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByBoundingBox(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByBoundingBox Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByBoundingBox')


    def new_input_set(self):
        return SearchByBoundingBoxInputSet()

    def _make_result_set(self, result, path):
        return SearchByBoundingBoxResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByBoundingBoxChoreographyExecution(session, exec_id, path)

class SearchByBoundingBoxInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByBoundingBox
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BusinessType(self, value):
        """
        Set the value of the BusinessType input for this Choreo. ((optional, string) A term to narrow the search, such as "comic books" or "restaurants". Leave blank to search for all business types.)
        """
        InputSet._set_input(self, 'BusinessType', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Yelp.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Yelp.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_NortheastLatitude(self, value):
        """
        Set the value of the NortheastLatitude input for this Choreo. ((required, decimal) The northeastern latitude of the bounding box to search, such as "37.788022".)
        """
        InputSet._set_input(self, 'NortheastLatitude', value)
    def set_NortheastLongitude(self, value):
        """
        Set the value of the NortheastLongitude input for this Choreo. ((required, decimal) The northeastern longitude of the bounding box to search, such as "-122.399797".)
        """
        InputSet._set_input(self, 'NortheastLongitude', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from Yelp, either XML or JSON (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SouthwestLatitude(self, value):
        """
        Set the value of the SouthwestLatitude input for this Choreo. ((required, decimal) The southwestern latitude of the bounding box to search, such as "37.900000".)
        """
        InputSet._set_input(self, 'SouthwestLatitude', value)
    def set_SouthwestLongitude(self, value):
        """
        Set the value of the SouthwestLongitude input for this Choreo. ((required, decimal) The southwestern longitude of the bounding box to search, such as "-122.500000".)
        """
        InputSet._set_input(self, 'SouthwestLongitude', value)
    def set_TokenSecret(self, value):
        """
        Set the value of the TokenSecret input for this Choreo. ((required, string) The Token Secret provided by Yelp.)
        """
        InputSet._set_input(self, 'TokenSecret', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The Token provided by Yelp.)
        """
        InputSet._set_input(self, 'Token', value)

class SearchByBoundingBoxResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByBoundingBox Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        return self._output.get('Response', None)

class SearchByBoundingBoxChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByBoundingBoxResultSet(response, path)
