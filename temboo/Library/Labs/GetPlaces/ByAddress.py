# -*- coding: utf-8 -*-

###############################################################################
#
# ByAddress
# Retrieves information from multiple APIs about places near a specified street address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ByAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/GetPlaces/ByAddress')


    def new_input_set(self):
        return ByAddressInputSet()

    def _make_result_set(self, result, path):
        return ByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByAddressChoreographyExecution(session, exec_id, path)

class ByAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((conditional, json) )
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The street address to use in the search. This can be a single address, or an array of addresses. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'Address', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limits the number of Foursquare venues results.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) This keyword input can be used to narrow search results for Google Places and Foursquare.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Filters results by type of place, such as: bar, dentist, etc. This is used to filter results for Google Places and Yelp.)
        """
        InputSet._set_input(self, 'Type', value)

class ByAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Contains the merged results for search.)
        """
        return self._output.get('Response', None)

class ByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByAddressResultSet(response, path)
