# -*- coding: utf-8 -*-

###############################################################################
#
# GetRateSummary
# Retrieve current interest rates for a specified loan type.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetRateSummary(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRateSummary Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetRateSummary')


    def new_input_set(self):
        return GetRateSummaryInputSet()

    def _make_result_set(self, result, path):
        return GetRateSummaryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRateSummaryChoreographyExecution(session, exec_id, path)

class GetRateSummaryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRateSummary
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_OutputFormat(self, value):
        """
        Set the value of the OutputFormat input for this Choreo. ((optional, string) Enter the desired query output format.  Enter: xml, or json.  Default output is set to: xml.)
        """
        InputSet._set_input(self, 'OutputFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Enter a U.S. state abbreviation for which to retrieve mortgage rates.  If null, the national average rate is returned.)
        """
        InputSet._set_input(self, 'State', value)
    def set_ZWSID(self, value):
        """
        Set the value of the ZWSID input for this Choreo. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        InputSet._set_input(self, 'ZWSID', value)

class GetRateSummaryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRateSummary Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Zillow.)
        """
        return self._output.get('Response', None)

class GetRateSummaryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRateSummaryResultSet(response, path)
