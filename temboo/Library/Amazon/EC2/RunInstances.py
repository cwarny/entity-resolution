# -*- coding: utf-8 -*-

###############################################################################
#
# RunInstances
# Launches the specified number of instances of an AMI for which you have permissions.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RunInstances(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RunInstances Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/RunInstances')


    def new_input_set(self):
        return RunInstancesInputSet()

    def _make_result_set(self, result, path):
        return RunInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RunInstancesChoreographyExecution(session, exec_id, path)

class RunInstancesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RunInstances
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
        Set the value of the DeleteOnTermination input for this Choreo. ((optional, boolean) Sets whether the volume is deleted on instance termination. Defaults to "true".)
        """
        InputSet._set_input(self, 'DeleteOnTermination', value)
    def set_DeviceName(self, value):
        """
        Set the value of the DeviceName input for this Choreo. ((optional, string) The device name exposed to the instance (i.e. /dev/sdh or xvdh).)
        """
        InputSet._set_input(self, 'DeviceName', value)
    def set_ImageId(self, value):
        """
        Set the value of the ImageId input for this Choreo. ((required, string) The ID of the AMI.)
        """
        InputSet._set_input(self, 'ImageId', value)
    def set_InstanceType(self, value):
        """
        Set the value of the InstanceType input for this Choreo. ((optional, string) The instance type (i.e. t1.micro, m1.small, m1.medium, m1.large, m1.xlarge). Default is m1.small.)
        """
        InputSet._set_input(self, 'InstanceType', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((optional, integer) The number of I/O operations per second (IOPS) that the volume supports. Valid range is 100 to 2000.)
        """
        InputSet._set_input(self, 'Iops', value)
    def set_KernelId(self, value):
        """
        Set the value of the KernelId input for this Choreo. ((optional, string) The ID of the kernel with which to launch the instance.)
        """
        InputSet._set_input(self, 'KernelId', value)
    def set_KeyName(self, value):
        """
        Set the value of the KeyName input for this Choreo. ((optional, string) The name of the key pair to use.)
        """
        InputSet._set_input(self, 'KeyName', value)
    def set_MaxCount(self, value):
        """
        Set the value of the MaxCount input for this Choreo. ((required, integer) The maximum number of instances to launch. If the value is more than Amazon EC2 can launch, the largest possible number above MinCount will be launched instead.)
        """
        InputSet._set_input(self, 'MaxCount', value)
    def set_MinCount(self, value):
        """
        Set the value of the MinCount input for this Choreo. ((required, integer) The minimum number of instances to launch. If the value is more than Amazon EC2 can launch, no instances are launched at all.)
        """
        InputSet._set_input(self, 'MinCount', value)
    def set_MonitoringEnabled(self, value):
        """
        Set the value of the MonitoringEnabled input for this Choreo. ((optional, boolean) Enables monitoring for the instance. Defaults to false.)
        """
        InputSet._set_input(self, 'MonitoringEnabled', value)
    def set_NoDevice(self, value):
        """
        Set the value of the NoDevice input for this Choreo. ((optional, boolean) Suppresses a device mapping.)
        """
        InputSet._set_input(self, 'NoDevice', value)
    def set_PlacementAvailabilityZone(self, value):
        """
        Set the value of the PlacementAvailabilityZone input for this Choreo. ((optional, string) The Availability Zone to launch the instance into.)
        """
        InputSet._set_input(self, 'PlacementAvailabilityZone', value)
    def set_PlacementGroupName(self, value):
        """
        Set the value of the PlacementGroupName input for this Choreo. ((optional, string) The name of an existing placement group you want to launch the instance into (for cluster instances).)
        """
        InputSet._set_input(self, 'PlacementGroupName', value)
    def set_PlacementTenancy(self, value):
        """
        Set the value of the PlacementTenancy input for this Choreo. ((optional, string) The tenancy of the instance. When set to "dedicated", the instance will run on single-tenant hardware and can only be launched into a VPC.)
        """
        InputSet._set_input(self, 'PlacementTenancy', value)
    def set_RamdiskId(self, value):
        """
        Set the value of the RamdiskId input for this Choreo. ((optional, string) The ID of the RAM disk.)
        """
        InputSet._set_input(self, 'RamdiskId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SecurityGroupId(self, value):
        """
        Set the value of the SecurityGroupId input for this Choreo. ((optional, string) One or more security group IDs. This can be a comma-separated list of up to 10 security group ids.)
        """
        InputSet._set_input(self, 'SecurityGroupId', value)
    def set_SecurityGroup(self, value):
        """
        Set the value of the SecurityGroup input for this Choreo. ((optional, string) One or more security group names. This can be a comma-separated list of up to 10 security group names.)
        """
        InputSet._set_input(self, 'SecurityGroup', value)
    def set_ShutdownBehavior(self, value):
        """
        Set the value of the ShutdownBehavior input for this Choreo. ((optional, string) Whether the instance stops or terminates on instance-initiated shutdown. Valid values are: stop and terminate.)
        """
        InputSet._set_input(self, 'ShutdownBehavior', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((optional, string) The ID of the snapshot.)
        """
        InputSet._set_input(self, 'SnapshotId', value)
    def set_SubnetId(self, value):
        """
        Set the value of the SubnetId input for this Choreo. ((optional, string) The ID of the subnet to launch the instance into (i.e. subnet-dea63cb7).)
        """
        InputSet._set_input(self, 'SubnetId', value)
    def set_UserData(self, value):
        """
        Set the value of the UserData input for this Choreo. ((optional, string) The Base64-encoded MIME user data to be made available to the instance(s).)
        """
        InputSet._set_input(self, 'UserData', value)
    def set_VirtualName(self, value):
        """
        Set the value of the VirtualName input for this Choreo. ((optional, string) The name of the virtual device.)
        """
        InputSet._set_input(self, 'VirtualName', value)
    def set_VolumeSize(self, value):
        """
        Set the value of the VolumeSize input for this Choreo. ((optional, string) The size of the volume, in GiBs. Required unless you're creating the volume from a snapshot which indicates that the size will be the size of the snapshot.)
        """
        InputSet._set_input(self, 'VolumeSize', value)
    def set_VolumeType(self, value):
        """
        Set the value of the VolumeType input for this Choreo. ((optional, string) The volume type. Valid values are: standard (the default) and io1.)
        """
        InputSet._set_input(self, 'VolumeType', value)

class RunInstancesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RunInstances Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class RunInstancesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RunInstancesResultSet(response, path)
