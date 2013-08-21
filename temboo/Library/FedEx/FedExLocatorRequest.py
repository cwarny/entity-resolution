# -*- coding: utf-8 -*-

###############################################################################
#
# FedExLocatorRequest
# Retrieves the nearest FedEx locations for a specified address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FedExLocatorRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FedExLocatorRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/FedEx/FedExLocatorRequest')


    def new_input_set(self):
        return FedExLocatorRequestInputSet()

    def _make_result_set(self, result, path):
        return FedExLocatorRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FedExLocatorRequestChoreographyExecution(session, exec_id, path)

class FedExLocatorRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FedExLocatorRequest
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
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) The city to use in the locator request)
        """
        InputSet._set_input(self, 'City', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((required, string) The country code to use in the locator request)
        """
        InputSet._set_input(self, 'CountryCode', value)
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
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((required, string) The postal code to use in the locator request)
        """
        InputSet._set_input(self, 'PostalCode', value)
    def set_StateOrProvinceCode(self, value):
        """
        Set the value of the StateOrProvinceCode input for this Choreo. ((required, string) The state or province code to use in the locator request)
        """
        InputSet._set_input(self, 'StateOrProvinceCode', value)
    def set_Street(self, value):
        """
        Set the value of the Street input for this Choreo. ((required, string) The street to use in the locator request)
        """
        InputSet._set_input(self, 'Street', value)

class FedExLocatorRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FedExLocatorRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_BusinessAddress(self):
        """
        Retrieve the value for the "BusinessAddress" output from this Choreo execution. ((string) The Business Address parsed from the FedEx response)
        """
        return self._output.get('BusinessAddress', None)
    def get_BusinessName(self):
        """
        Retrieve the value for the "BusinessName" output from this Choreo execution. ((string) The Business Name parsed from the FedEx response)
        """
        return self._output.get('BusinessName', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FedEx)
        """
        return self._output.get('Response', None)

class FedExLocatorRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FedExLocatorRequestResultSet(response, path)
