# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeAddresses
# Describes one or more of your Elastic IP addresses.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DescribeAddresses(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeAddresses Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DescribeAddresses')


    def new_input_set(self):
        return DescribeAddressesInputSet()

    def _make_result_set(self, result, path):
        return DescribeAddressesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeAddressesChoreographyExecution(session, exec_id, path)

class DescribeAddressesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeAddresses
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
    def set_AllocationId(self, value):
        """
        Set the value of the AllocationId input for this Choreo. ((optional, string) One or more allocation IDs corresponding to the address or addresses to describe (VPC addresses only). This can be a comma-separated list of up to 10 Allocation Ids.)
        """
        InputSet._set_input(self, 'AllocationId', value)
    def set_FilterName(self, value):
        """
        Set the value of the FilterName input for this Choreo. ((optional, string) The name of a supported filter to narrow the results with.)
        """
        InputSet._set_input(self, 'FilterName', value)
    def set_FilterValue(self, value):
        """
        Set the value of the FilterValue input for this Choreo. ((optional, string) A value for the specified filter.)
        """
        InputSet._set_input(self, 'FilterValue', value)
    def set_PublicIp(self, value):
        """
        Set the value of the PublicIp input for this Choreo. ((optional, string) One or more EC2 Elastic IP addresses.  This can be a comma-separated list of up to 10 IP addresses.)
        """
        InputSet._set_input(self, 'PublicIp', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class DescribeAddressesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeAddresses Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeAddressesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeAddressesResultSet(response, path)
