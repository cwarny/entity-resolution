# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeDBSnapshot
# Returns information about DB Snapshots.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DescribeDBSnapshot(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeDBSnapshot Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/DescribeDBSnapshot')


    def new_input_set(self):
        return DescribeDBSnapshotInputSet()

    def _make_result_set(self, result, path):
        return DescribeDBSnapshotResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeDBSnapshotChoreographyExecution(session, exec_id, path)

class DescribeDBSnapshotInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeDBSnapshot
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
    def set_DBInstanceIdentifier(self, value):
        """
        Set the value of the DBInstanceIdentifier input for this Choreo. ((optional, string) The DB Instance identifier. Should be in all lowercase.)
        """
        InputSet._set_input(self, 'DBInstanceIdentifier', value)
    def set_DBSnapshotIdentifier(self, value):
        """
        Set the value of the DBSnapshotIdentifier input for this Choreo. ((optional, string) The unique identifier for the db snapshot you're retrieving information for.)
        """
        InputSet._set_input(self, 'DBSnapshotIdentifier', value)
    def set_MaxRecords(self, value):
        """
        Set the value of the MaxRecords input for this Choreo. ((optional, integer) The max number of results to return in the response. Defaults to 100. Minimum is 20.)
        """
        InputSet._set_input(self, 'MaxRecords', value)

class DescribeDBSnapshotResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeDBSnapshot Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeDBSnapshotChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeDBSnapshotResultSet(response, path)
