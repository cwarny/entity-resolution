# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDevice
# Creates a new device in a product batch for each serial number provided. When created, each device will be in a pre-registered state awaiting activation. Creating a non-product-affiliated device is not available through the Xively API, and can only be done through the browser-only Xively Developer Workbench.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateDevice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDevice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Devices/CreateDevice')


    def new_input_set(self):
        return CreateDeviceInputSet()

    def _make_result_set(self, result, path):
        return CreateDeviceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDeviceChoreographyExecution(session, exec_id, path)

class CreateDeviceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDevice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The product ID for the device you would like to add.)
        """
        InputSet._set_input(self, 'ProductID', value)
    def set_SerialNumbers(self, value):
        """
        Set the value of the SerialNumbers input for this Choreo. ((required, string) Comma-separated list of device serial numbers to add. Allowed characters: case-sensitive alphanumeric characters (Ab3) and the following characters: "+", "-", "_", and ":". Ex: abc:123,aBc-124.)
        """
        InputSet._set_input(self, 'SerialNumbers', value)

class CreateDeviceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDevice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful device creation, the code should be 201.)
        """
        return self._output.get('ResponseStatusCode', None)

class CreateDeviceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDeviceResultSet(response, path)
