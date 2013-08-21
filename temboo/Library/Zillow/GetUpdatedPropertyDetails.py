# -*- coding: utf-8 -*-

###############################################################################
#
# GetUpdatedPropertyDetails
# Retrieve detailed property information that has been edited by the home's owner or agent.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetUpdatedPropertyDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUpdatedPropertyDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetUpdatedPropertyDetails')


    def new_input_set(self):
        return GetUpdatedPropertyDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetUpdatedPropertyDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUpdatedPropertyDetailsChoreographyExecution(session, exec_id, path)

class GetUpdatedPropertyDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUpdatedPropertyDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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

class GetUpdatedPropertyDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUpdatedPropertyDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Zillow.)
        """
        return self._output.get('Response', None)

class GetUpdatedPropertyDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUpdatedPropertyDetailsResultSet(response, path)
