# -*- coding: utf-8 -*-

###############################################################################
#
# GetComps
# Returns a list of comparable recent sales for a specified property.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetComps(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetComps Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetComps')


    def new_input_set(self):
        return GetCompsInputSet()

    def _make_result_set(self, result, path):
        return GetCompsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCompsChoreographyExecution(session, exec_id, path)

class GetCompsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetComps
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((required, integer) Enter the number of comparable recent sales to retrieve. Choose a value between 1 and 25.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_RentEstimate(self, value):
        """
        Set the value of the RentEstimate input for this Choreo. ((optional, boolean) Set to 1 (true) to enable. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'RentEstimate', value)
    def set_ZPID(self, value):
        """
        Set the value of the ZPID input for this Choreo. ((required, integer) Enter a Zillow Property ID for the property being queried.)
        """
        InputSet._set_input(self, 'ZPID', value)
    def set_ZWSID(self, value):
        """
        Set the value of the ZWSID input for this Choreo. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        InputSet._set_input(self, 'ZWSID', value)

class GetCompsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetComps Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Zillow.)
        """
        return self._output.get('Response', None)

class GetCompsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCompsResultSet(response, path)
