# -*- coding: utf-8 -*-

###############################################################################
#
# TollFreeList
# Returns a list of toll-free available phone numbers that match the specified filters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TollFreeList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TollFreeList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/AvailablePhoneNumbers/TollFreeList')


    def new_input_set(self):
        return TollFreeListInputSet()

    def _make_result_set(self, result, path):
        return TollFreeListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TollFreeListChoreographyExecution(session, exec_id, path)

class TollFreeListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TollFreeList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AccountSID', value)
    def set_AreaCode(self, value):
        """
        Set the value of the AreaCode input for this Choreo. ((optional, integer) Find phone numbers in the specified area code. (US and Canada only).)
        """
        InputSet._set_input(self, 'AreaCode', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AuthToken', value)
    def set_Contains(self, value):
        """
        Set the value of the Contains input for this Choreo. ((optional, string) A pattern to match phone numbers on. Valid characters are '*' and [0-9a-zA-Z]. The '*' character will match any single digit.)
        """
        InputSet._set_input(self, 'Contains', value)
    def set_IsoCountryCode(self, value):
        """
        Set the value of the IsoCountryCode input for this Choreo. ((optional, string) The country code to search within. Defaults to US.)
        """
        InputSet._set_input(self, 'IsoCountryCode', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        InputSet._set_input(self, 'PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class TollFreeListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TollFreeList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class TollFreeListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TollFreeListResultSet(response, path)
