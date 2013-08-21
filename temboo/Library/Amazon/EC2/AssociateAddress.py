# -*- coding: utf-8 -*-

###############################################################################
#
# AssociateAddress
# Associates an Elastic IP address with an instance or a network interface.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AssociateAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AssociateAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/AssociateAddress')


    def new_input_set(self):
        return AssociateAddressInputSet()

    def _make_result_set(self, result, path):
        return AssociateAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AssociateAddressChoreographyExecution(session, exec_id, path)

class AssociateAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AssociateAddress
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
        Set the value of the AllocationId input for this Choreo. ((optional, string) [EC2-VPC] The allocation ID.  Required for a VPC.)
        """
        InputSet._set_input(self, 'AllocationId', value)
    def set_AllowReassociation(self, value):
        """
        Set the value of the AllowReassociation input for this Choreo. ((optional, string) [EC2-VPC] Allows an Elastic IP address that is already associated with an instance or network interface to be re-associated with the specified instance or network interface. False if not specified.)
        """
        InputSet._set_input(self, 'AllowReassociation', value)
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((conditional, string) The ID of the instance.  Required for EC2-Classic. For a VPC, you can specify either an instance ID or a network interface ID, but not both.)
        """
        InputSet._set_input(self, 'InstanceId', value)
    def set_NetworkInterfaceId(self, value):
        """
        Set the value of the NetworkInterfaceId input for this Choreo. ((optional, string) [EC2-VPC] The ID of the network interface. Association fails when specifying an instance ID unless exactly one interface is attached.)
        """
        InputSet._set_input(self, 'NetworkInterfaceId', value)
    def set_PrivateIpAddress(self, value):
        """
        Set the value of the PrivateIpAddress input for this Choreo. ((optional, string) [EC2-VPC] The primary or secondary private IP address to associate with the Elastic IP address. If nothing is specified, the Elastic IP address is associated with the primary private IP address.)
        """
        InputSet._set_input(self, 'PrivateIpAddress', value)
    def set_PublicIp(self, value):
        """
        Set the value of the PublicIp input for this Choreo. ((conditional, string) The Elastic IP address.)
        """
        InputSet._set_input(self, 'PublicIp', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class AssociateAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AssociateAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class AssociateAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AssociateAddressResultSet(response, path)
