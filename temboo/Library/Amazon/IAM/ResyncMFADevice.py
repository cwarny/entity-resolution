# -*- coding: utf-8 -*-

###############################################################################
#
# ResyncMFADevice
# Synchronizes the specified MFA device with AWS servers.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ResyncMFADevice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ResyncMFADevice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/ResyncMFADevice')


    def new_input_set(self):
        return ResyncMFADeviceInputSet()

    def _make_result_set(self, result, path):
        return ResyncMFADeviceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ResyncMFADeviceChoreographyExecution(session, exec_id, path)

class ResyncMFADeviceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ResyncMFADevice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_AuthenticationCode1(self, value):
        """
        Set the value of the AuthenticationCode1 input for this Choreo. ((required, string) An authentication code emitted by the device.)
        """
        InputSet._set_input(self, 'AuthenticationCode1', value)
    def set_AuthenticationCode2(self, value):
        """
        Set the value of the AuthenticationCode2 input for this Choreo. ((required, string) A subsequent authentication code emitted by the device.)
        """
        InputSet._set_input(self, 'AuthenticationCode2', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SerialNumber(self, value):
        """
        Set the value of the SerialNumber input for this Choreo. ((required, string) The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the same as the ARN.)
        """
        InputSet._set_input(self, 'SerialNumber', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Name of the user for whom you want to enable the MFA device.)
        """
        InputSet._set_input(self, 'UserName', value)

class ResyncMFADeviceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ResyncMFADevice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ResyncMFADeviceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ResyncMFADeviceResultSet(response, path)
