# -*- coding: utf-8 -*-

###############################################################################
#
# CreateImage
# Creates an Amazon Machine Image from an Amazon EBS-backed instance. The image can be used later to launch other identical servers.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateImage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateImage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/CreateImage')


    def new_input_set(self):
        return CreateImageInputSet()

    def _make_result_set(self, result, path):
        return CreateImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateImageChoreographyExecution(session, exec_id, path)

class CreateImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateImage
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
    def set_DeleteOnTermination(self, value):
        """
        Set the value of the DeleteOnTermination input for this Choreo. ((optional, boolean) Whether the volume is deleted on instance termination. Defaults to "true".)
        """
        InputSet._set_input(self, 'DeleteOnTermination', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description for the image you want to create.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_DeviceName(self, value):
        """
        Set the value of the DeviceName input for this Choreo. ((conditional, string) The device name exposed to the instance (i.e. /dev/sdh or xvdh). When registering an AMI from a snapshot, DiviceName is required as well as SnapshotId.)
        """
        InputSet._set_input(self, 'DeviceName', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((required, string) The ID of the instance to create the image on.)
        """
        InputSet._set_input(self, 'InstanceId', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((conditional, integer) The number of I/O operations per second (IOPS) that the volume supports. Valid range is 100 to 2000.)
        """
        InputSet._set_input(self, 'Iops', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name for the image you are creating.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_NoDevice(self, value):
        """
        Set the value of the NoDevice input for this Choreo. ((optional, boolean) Suppresses a device mapping. Defaults to "true".)
        """
        InputSet._set_input(self, 'NoDevice', value)
    def set_NoReboot(self, value):
        """
        Set the value of the NoReboot input for this Choreo. ((optional, boolean) Defaults to "false". Amazon EC2 will attempt to shut down the instance before and after creating the image. Set to "true" for NoReboot.)
        """
        InputSet._set_input(self, 'NoReboot', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((conditional, string) The ID of the snapshot. Required when registering from a snapshot. You must also specify DeviceName with the root device name.)
        """
        InputSet._set_input(self, 'SnapshotId', value)
    def set_VirtualName(self, value):
        """
        Set the value of the VirtualName input for this Choreo. ((optional, string) The name of the virtual device.)
        """
        InputSet._set_input(self, 'VirtualName', value)
    def set_VolumeSize(self, value):
        """
        Set the value of the VolumeSize input for this Choreo. ((conditional, string) The size of the volume, in GiBs. Required unless you're creating the volume from a snapshot which indicates that the size will be the size of the snapshot.)
        """
        InputSet._set_input(self, 'VolumeSize', value)
    def set_VolumeType(self, value):
        """
        Set the value of the VolumeType input for this Choreo. ((optional, string) The volume type. Valid values are: standard (the default) and io1.)
        """
        InputSet._set_input(self, 'VolumeType', value)

class CreateImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateImage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateImageResultSet(response, path)
