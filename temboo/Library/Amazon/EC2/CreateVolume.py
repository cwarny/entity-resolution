# -*- coding: utf-8 -*-

###############################################################################
#
# CreateVolume
# Creates a new EBS volume that your EC2 instance can attach to.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateVolume(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateVolume Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/CreateVolume')


    def new_input_set(self):
        return CreateVolumeInputSet()

    def _make_result_set(self, result, path):
        return CreateVolumeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateVolumeChoreographyExecution(session, exec_id, path)

class CreateVolumeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateVolume
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
    def set_AvailabilityZone(self, value):
        """
        Set the value of the AvailabilityZone input for this Choreo. ((required, string) The Availability Zone to use when creating thew new volume (i.e us-east-1a).)
        """
        InputSet._set_input(self, 'AvailabilityZone', value)
    def set_Iops(self, value):
        """
        Set the value of the Iops input for this Choreo. ((optional, integer) The number of I/O operations per second (IOPS) that the volume supports. Valid range is 100 to 2000. Required when the volume type is io1.)
        """
        InputSet._set_input(self, 'Iops', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Size(self, value):
        """
        Set the value of the Size input for this Choreo. ((conditional, integer) The size for the volume (in gigabytes) that you are creating. Valid Values are 1-1024. Required if you're not creating a volume from a snapshot. If the volume type is io1, the min size is 10 GiB.)
        """
        InputSet._set_input(self, 'Size', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((conditional, string) The snapshot from which to create the new volume. Required if you are creating a volume from a snapshot.)
        """
        InputSet._set_input(self, 'SnapshotId', value)
    def set_VolumeType(self, value):
        """
        Set the value of the VolumeType input for this Choreo. ((optional, string) The volume type.Valid values are: "standard" (the default) and "io1".)
        """
        InputSet._set_input(self, 'VolumeType', value)

class CreateVolumeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateVolume Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateVolumeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateVolumeResultSet(response, path)
