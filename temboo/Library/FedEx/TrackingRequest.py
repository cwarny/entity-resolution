# -*- coding: utf-8 -*-

###############################################################################
#
# TrackingRequest
# Retrieves package information for a specified tracking number.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TrackingRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TrackingRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/FedEx/TrackingRequest')


    def new_input_set(self):
        return TrackingRequestInputSet()

    def _make_result_set(self, result, path):
        return TrackingRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrackingRequestChoreographyExecution(session, exec_id, path)

class TrackingRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TrackingRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountNumber(self, value):
        """
        Set the value of the AccountNumber input for this Choreo. ((required, string) Your FedEx Account Number)
        """
        InputSet._set_input(self, 'AccountNumber', value)
    def set_AuthenticationKey(self, value):
        """
        Set the value of the AuthenticationKey input for this Choreo. ((required, string) The Production Authentication Key provided by FedEx Web Services)
        """
        InputSet._set_input(self, 'AuthenticationKey', value)
    def set_MeterNumber(self, value):
        """
        Set the value of the MeterNumber input for this Choreo. ((required, string) The Production Meter Number provided by FedEx Web Services)
        """
        InputSet._set_input(self, 'MeterNumber', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Production Password provided by FedEx Web Services)
        """
        InputSet._set_input(self, 'Password', value)
    def set_TrackingNumber(self, value):
        """
        Set the value of the TrackingNumber input for this Choreo. ((required, string) The package tracking number to use in the request)
        """
        InputSet._set_input(self, 'TrackingNumber', value)

class TrackingRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TrackingRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FedEx)
        """
        return self._output.get('Response', None)
    def get_StatusDescription(self):
        """
        Retrieve the value for the "StatusDescription" output from this Choreo execution. ((string) The status description for the package which is parsed from the FedEx response)
        """
        return self._output.get('StatusDescription', None)

class TrackingRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TrackingRequestResultSet(response, path)
