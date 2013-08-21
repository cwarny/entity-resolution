# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByAddress
# Retrieve businesses within a specific range of a specified address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yelp/SearchByAddress')


    def new_input_set(self):
        return SearchByAddressInputSet()

    def _make_result_set(self, result, path):
        return SearchByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByAddressChoreographyExecution(session, exec_id, path)

class SearchByAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The street address of the business to search for.)
        """
        InputSet._set_input(self, 'Address', value)
    def set_BusinessType(self, value):
        """
        Set the value of the BusinessType input for this Choreo. ((optional, string) A term to narrow the search, such as "shoes" or "restaurants". Leave blank to search for all business types.)
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
    def set_Range(self, value):
        """
        Set the value of the Range input for this Choreo. ((required, integer) Narrow or expand a search by specifying a range in either feet, meters, miles, or kilometers, depending on the value of the Units input. The default is 200 feet, and the maximum is 2,500 square miles.)
        """
        InputSet._set_input(self, 'Range', value)
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
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((required, string) Specify "feet" (the default), "meters", "miles", or "kilometers". Units apply to the Range input value.)
        """
        InputSet._set_input(self, 'Units', value)

class SearchByAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yelp. Corresponds to the input value for ResponseFormat (defaults to JSON).)
        """
        return self._output.get('Response', None)

class SearchByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByAddressResultSet(response, path)
