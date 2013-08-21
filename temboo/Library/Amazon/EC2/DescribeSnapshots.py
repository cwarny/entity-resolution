# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeSnapshots
# Returns information on available Amazon EBS snapshots.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DescribeSnapshots(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeSnapshots Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DescribeSnapshots')


    def new_input_set(self):
        return DescribeSnapshotsInputSet()

    def _make_result_set(self, result, path):
        return DescribeSnapshotsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeSnapshotsChoreographyExecution(session, exec_id, path)

class DescribeSnapshotsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeSnapshots
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
    def set_FilterName(self, value):
        """
        Set the value of the FilterName input for this Choreo. ((optional, string) The name of a supported filter to narrow results with.)
        """
        InputSet._set_input(self, 'FilterName', value)
    def set_FilterValue(self, value):
        """
        Set the value of the FilterValue input for this Choreo. ((optional, string) A value for the specified filter.)
        """
        InputSet._set_input(self, 'FilterValue', value)
    def set_Owner(self, value):
        """
        Set the value of the Owner input for this Choreo. ((conditional, string) Returns the snapshots owned by the specified owner. Valid values are: "self" (the default), "amazon", or an AWS Account ID.)
        """
        InputSet._set_input(self, 'Owner', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_RestorableBy(self, value):
        """
        Set the value of the RestorableBy input for this Choreo. ((optional, string) AWS accounts ID that can create volumes from the snapshot.)
        """
        InputSet._set_input(self, 'RestorableBy', value)
    def set_SnapshotId(self, value):
        """
        Set the value of the SnapshotId input for this Choreo. ((optional, string) The ID of the snapshot you want to retrieve. Returns all snapshots if not specified.)
        """
        InputSet._set_input(self, 'SnapshotId', value)

class DescribeSnapshotsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeSnapshots Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeSnapshotsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeSnapshotsResultSet(response, path)
