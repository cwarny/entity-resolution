# -*- coding: utf-8 -*-

###############################################################################
#
# DetachVolume
# Detaches an Amazon EBS volume from an instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DetachVolume(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DetachVolume Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DetachVolume')


    def new_input_set(self):
        return DetachVolumeInputSet()

    def _make_result_set(self, result, path):
        return DetachVolumeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DetachVolumeChoreographyExecution(session, exec_id, path)

class DetachVolumeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DetachVolume
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
    def set_Device(self, value):
        """
        Set the value of the Device input for this Choreo. ((optional, string) The device name.)
        """
        InputSet._set_input(self, 'Device', value)
    def set_Force(self, value):
        """
        Set the value of the Force input for this Choreo. ((required, boolean) Forces detachment if the previous detachment attempt did not occur cleanly. Use this option only as a last resort to detach a volume from a failed instance. Defaults to false.)
        """
        InputSet._set_input(self, 'Force', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((optional, string) The ID of the instance.)
        """
        InputSet._set_input(self, 'InstanceId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_VolumeId(self, value):
        """
        Set the value of the VolumeId input for this Choreo. ((required, string) The ID of the volume.)
        """
        InputSet._set_input(self, 'VolumeId', value)

class DetachVolumeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DetachVolume Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DetachVolumeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DetachVolumeResultSet(response, path)
