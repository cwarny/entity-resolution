# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByNeighborhood
# Retrieve businesses by neighborhood.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByNeighborhood(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByNeighborhood Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByNeighborhood')


    def new_input_set(self):
        return SearchByNeighborhoodInputSet()

    def _make_result_set(self, result, path):
        return SearchByNeighborhoodResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByNeighborhoodChoreographyExecution(session, exec_id, path)

class SearchByNeighborhoodInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByNeighborhood
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BusinessType(self, value):
        """
        Set the value of the BusinessType input for this Choreo. ((optional, string) A term to narrow the search, such as "wine" or "restaurants". Leave blank to search for all business types.)
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
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of businesses to return. The default is 15.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_Neighborhood(self, value):
        """
        Set the value of the Neighborhood input for this Choreo. ((required, string) The neighborhood in which to search for businesses. See the Yelp API documentation for a list of supported neighborhoods.)
        """
        InputSet._set_input(self, 'Neighborhood', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from Yelp, either XML or JSON (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
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

class SearchByNeighborhoodResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByNeighborhood Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        return self._output.get('Response', None)

class SearchByNeighborhoodChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByNeighborhoodResultSet(response, path)
