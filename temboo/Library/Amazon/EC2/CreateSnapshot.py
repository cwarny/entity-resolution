# -*- coding: utf-8 -*-

###############################################################################
#
# CreateSnapshot
# Create a snapshot from a specified EBS volume.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateSnapshot(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateSnapshot Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/CreateSnapshot')


    def new_input_set(self):
        return CreateSnapshotInputSet()

    def _make_result_set(self, result, path):
        return CreateSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSnapshotChoreographyExecution(session, exec_id, path)

class CreateSnapshotInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateSnapshot
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
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description for the volume that you want to create.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_VolumeId(self, value):
        """
        Set the value of the VolumeId input for this Choreo. ((required, string) The id of the EBS volume to snapshot.)
        """
        InputSet._set_input(self, 'VolumeId', value)

class CreateSnapshotResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateSnapshot Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateSnapshotChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateSnapshotResultSet(response, path)
