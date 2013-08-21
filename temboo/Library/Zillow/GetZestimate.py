# -*- coding: utf-8 -*-

###############################################################################
#
# GetZestimate
# Retrieve estimate information for a specified property.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetZestimate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetZestimate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetZestimate')


    def new_input_set(self):
        return GetZestimateInputSet()

    def _make_result_set(self, result, path):
        return GetZestimateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetZestimateChoreographyExecution(session, exec_id, path)

class GetZestimateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetZestimate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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

class GetZestimateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetZestimate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Zillow.)
        """
        return self._output.get('Response', None)

class GetZestimateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetZestimateResultSet(response, path)
