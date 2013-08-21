# -*- coding: utf-8 -*-

###############################################################################
#
# RegisterImage
# Registers a new AMI with Amazon EC2.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RegisterImage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RegisterImage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/RegisterImage')


    def new_input_set(self):
        return RegisterImageInputSet()

    def _make_result_set(self, result, path):
        return RegisterImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RegisterImageChoreographyExecution(session, exec_id, path)

class RegisterImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RegisterImage
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
    def set_Architecture(self, value):
        """
        Set the value of the Architecture input for this Choreo. ((optional, string) The architecture of the image. Valid values are: i386 or x86_64. Defaults to i386.)
        """
        InputSet._set_input(self, 'Architecture', value)
    def set_DeleteOnTermination(self, value):
        """
        Set the value of the DeleteOnTermination input for this Choreo. ((optional, boolean) Whether the Amazon EBS volume is deleted on instance termination. Defaults to true.)
        """
        InputSet._set_input(self, 'DeleteOnTermination', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The description of the AMI.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_DeviceName(self, value):
        """
        Set the value of the DeviceName input for this Choreo. ((conditional, string) If registering an Amazon EBS-backed AMI from a snapshot, specify this input with the root device name (e.g., /dev/sda1, or xvda), and SnapshotId.)
        """
        InputSet._set_input(self, 'DeviceName', value)
    def set_ImageLocation(self, value):
        """
        Set the value of the ImageLocation input for this Choreo. ((conditional, string) Full path to your AMI manifest in Amazon S3 storage. Required if registering an Amazon-S3 backed AMI.)
        """
        InputSet._set_input(self, 'ImageLocation', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((conditional, integer) The number of I/O operations per second (IOPS) that the volume supports. A valid range is: 100 to 2000.)
        """
        InputSet._set_input(self, 'Iops', value)
    def set_KernelId(self, value):
        """
        Set the value of the KernelId input for this Choreo. ((optional, string) The ID of the kernel to select.)
        """
        InputSet._set_input(self, 'KernelId', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) A name for your AMI.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_NoDevice(self, value):
        """
        Set the value of the NoDevice input for this Choreo. ((optional, boolean) Specifies that no device should be mapped. Defaults to 1 (true).)
        """
        InputSet._set_input(self, 'NoDevice', value)
    def set_RamdiskId(self, value):
        """
        Set the value of the RamdiskId input for this Choreo. ((optional, string) The ID of the RAM disk to select.)
        """
        InputSet._set_input(self, 'RamdiskId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_RootDeviceName(self, value):
        """
        Set the value of the RootDeviceName input for this Choreo. ((conditional, string) The root device name (e.g., /dev/sda1, or xvda). Required if registering an Amazon EBS-backed AMI.)
        """
        InputSet._set_input(self, 'RootDeviceName', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((conditional, string) If registering an Amazon EBS-backed AMI from a snapshot, you must at least specify this input with the snapshot ID, and DeviceName with the root device name.)
        """
        InputSet._set_input(self, 'SnapshotId', value)
    def set_VirtualName(self, value):
        """
        Set the value of the VirtualName input for this Choreo. ((optional, string) The virtual device name.)
        """
        InputSet._set_input(self, 'VirtualName', value)
    def set_VolumeSize(self, value):
        """
        Set the value of the VolumeSize input for this Choreo. ((conditional, integer) The size of the volume, in GiBs. Required if you are not creating a volume from a snapshot.)
        """
        InputSet._set_input(self, 'VolumeSize', value)
    def set_VolumeType(self, value):
        """
        Set the value of the VolumeType input for this Choreo. ((optional, string) The volume type. Valid values are: standard and io.)
        """
        InputSet._set_input(self, 'VolumeType', value)

class RegisterImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RegisterImage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class RegisterImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RegisterImageResultSet(response, path)
