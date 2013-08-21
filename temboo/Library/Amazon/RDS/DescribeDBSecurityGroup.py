# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeDBSecurityGroup
# Returns a list of DBSecurityGroup descriptions. The list will can be filtered by specifying a DBSecurityGroupName.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DescribeDBSecurityGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeDBSecurityGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/DescribeDBSecurityGroup')


    def new_input_set(self):
        return DescribeDBSecurityGroupInputSet()

    def _make_result_set(self, result, path):
        return DescribeDBSecurityGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeDBSecurityGroupChoreographyExecution(session, exec_id, path)

class DescribeDBSecurityGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeDBSecurityGroup
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
    def set_DBSecurityGroupName(self, value):
        """
        Set the value of the DBSecurityGroupName input for this Choreo. ((optional, string) The name for the security group you want to retrieve information for.)
        """
        InputSet._set_input(self, 'DBSecurityGroupName', value)
    def set_Marker(self, value):
        """
        Set the value of the Marker input for this Choreo. ((optional, integer) If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.)
        """
        InputSet._set_input(self, 'Marker', value)
    def set_MaxRecords(self, value):
        """
        Set the value of the MaxRecords input for this Choreo. ((optional, integer) The max number of results to return in the response. Defaults to 100. Minimum is 20.)
        """
        InputSet._set_input(self, 'MaxRecords', value)

class DescribeDBSecurityGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeDBSecurityGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeDBSecurityGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeDBSecurityGroupResultSet(response, path)
