# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCategory
# Retrieve businesses in a specific location by business category.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByCategory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByCategory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByCategory')


    def new_input_set(self):
        return SearchByCategoryInputSet()

    def _make_result_set(self, result, path):
        return SearchByCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCategoryChoreographyExecution(session, exec_id, path)

class SearchByCategoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByCategory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((required, string) Yelp categories to search in, separated by commas but no spaces, such as "hiking,climbing". See the Yelp API docimentation for a list of categories.)
        """
        InputSet._set_input(self, 'Category', value)
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
    def set_Location(self, value):
        """
        Set the value of the Location input for this Choreo. ((required, string) An address, neighborhood, city, state, or ZIP code in which to search for the category.)
        """
        InputSet._set_input(self, 'Location', value)
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

class SearchByCategoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByCategory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        return self._output.get('Response', None)

class SearchByCategoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCategoryResultSet(response, path)
