# -*- coding: utf-8 -*-

###############################################################################
#
# ActivateDevice
# Activates (or reactivates) a device given an authorization code. Returns the device API Key and Feed ID. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ActivateDevice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ActivateDevice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Devices/ActivateDevice')


    def new_input_set(self):
        return ActivateDeviceInputSet()

    def _make_result_set(self, result, path):
        return ActivateDeviceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ActivateDeviceChoreographyExecution(session, exec_id, path)

class ActivateDeviceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ActivateDevice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) Not required for first activation. If re-activating a device, either the original device APIKey returned from the first activation or the master APIKey is required.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ActivationCode(self, value):
        """
        Set the value of the ActivationCode input for this Choreo. ((required, string) Activation code provided when pre-registering a device with a serial number.)
        """
        InputSet._set_input(self, 'ActivationCode', value)

class ActivateDeviceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ActivateDevice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Xively. Upon successful activation, it returns a JSON array containing the device APIKey, FeedID and Datastreams.)
        """
        return self._output.get('Response', None)

class ActivateDeviceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ActivateDeviceResultSet(response, path)
