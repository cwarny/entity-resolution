# -*- coding: utf-8 -*-

###############################################################################
#
# ValidateAddress
# Validates and supplements incomplete address information.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ValidateAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ValidateAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/USPS/AddressInformationAPI/ValidateAddress')


    def new_input_set(self):
        return ValidateAddressInputSet()

    def _make_result_set(self, result, path):
        return ValidateAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ValidateAddressChoreographyExecution(session, exec_id, path)

class ValidateAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ValidateAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AptOrSuite(self, value):
        """
        Set the value of the AptOrSuite input for this Choreo. ((optional, string) Used to provide an apartment or suite number, if applicable. Maximum characters allowed: 38.)
        """
        InputSet._set_input(self, 'AptOrSuite', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) Maximum characters allowed: 15. Either City and State or Zip are required.)
        """
        InputSet._set_input(self, 'City', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_FirmName(self, value):
        """
        Set the value of the FirmName input for this Choreo. ((optional, string) Maximum characters allowed: 38.)
        """
        InputSet._set_input(self, 'FirmName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password assigned by USPS)
        """
        InputSet._set_input(self, 'Password', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Maximum characters allowed: 2. Either City and State or Zip are required.)
        """
        InputSet._set_input(self, 'State', value)
    def set_StreetAddress(self, value):
        """
        Set the value of the StreetAddress input for this Choreo. ((required, string) Street address. Maximum characters allowed: 38.)
        """
        InputSet._set_input(self, 'StreetAddress', value)
    def set_Urbanization(self, value):
        """
        Set the value of the Urbanization input for this Choreo. ((optional, string) Maximum characters allowed: 28. For Puerto Rico addresses only.)
        """
        InputSet._set_input(self, 'Urbanization', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((required, string) Alphanumeric ID assigned by USPS)
        """
        InputSet._set_input(self, 'UserId', value)
    def set_Zip4DigitCode(self, value):
        """
        Set the value of the Zip4DigitCode input for this Choreo. ((optional, integer) Maximum characters allowed: 4)
        """
        InputSet._set_input(self, 'Zip4DigitCode', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, integer) Maximum characters allowed: 5. Either City and State or Zip are required.)
        """
        InputSet._set_input(self, 'Zip', value)

class ValidateAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ValidateAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from USPS Web Service)
        """
        return self._output.get('Response', None)

class ValidateAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ValidateAddressResultSet(response, path)
