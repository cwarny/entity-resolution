# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCity
# Retrieve businesses by city.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByCity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByCity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByCity')


    def new_input_set(self):
        return SearchByCityInputSet()

    def _make_result_set(self, result, path):
        return SearchByCityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCityChoreographyExecution(session, exec_id, path)

class SearchByCityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByCity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BusinessType(self, value):
        """
        Set the value of the BusinessType input for this Choreo. ((optional, string) A term to narrow the search, such as "wine" or "restaurants". Leave blank to search for all business types.)
        """
        InputSet._set_input(self, 'BusinessType', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) The name of the city in which to search for businesses.)
        """
        InputSet._set_input(self, 'City', value)
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
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, multiline) The format of the response from Yelp, either XML or JSON (the default).)
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

class SearchByCityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByCity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        return self._output.get('Response', None)

class SearchByCityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCityResultSet(response, path)
