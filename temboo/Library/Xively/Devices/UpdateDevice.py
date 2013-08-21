# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateDevice
# Updates a single device's serial number. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateDevice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateDevice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Devices/UpdateDevice')


    def new_input_set(self):
        return UpdateDeviceInputSet()

    def _make_result_set(self, result, path):
        return UpdateDeviceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateDeviceChoreographyExecution(session, exec_id, path)

class UpdateDeviceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateDevice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_NewSerialNumber(self, value):
        """
        Set the value of the NewSerialNumber input for this Choreo. ((required, string) The new serial number you want to update the existing device to. Allowed characters: case-sensitive alphanumeric characters (Ab3) and certain characters: "+", "-", "_", and ":". Ex: abc:123,aBc-124.)
        """
        InputSet._set_input(self, 'NewSerialNumber', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The product ID for the device you would like to update.)
        """
        InputSet._set_input(self, 'ProductID', value)
    def set_SerialNumber(self, value):
        """
        Set the value of the SerialNumber input for this Choreo. ((required, string) The existing serial number for the device you would like to update.)
        """
        InputSet._set_input(self, 'SerialNumber', value)

class UpdateDeviceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateDevice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful device update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class UpdateDeviceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateDeviceResultSet(response, path)
