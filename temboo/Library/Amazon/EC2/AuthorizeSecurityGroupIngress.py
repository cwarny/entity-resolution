# -*- coding: utf-8 -*-

###############################################################################
#
# AuthorizeSecurityGroupIngress
# Adds an ingress rule to a security group.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AuthorizeSecurityGroupIngress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AuthorizeSecurityGroupIngress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/AuthorizeSecurityGroupIngress')


    def new_input_set(self):
        return AuthorizeSecurityGroupIngressInputSet()

    def _make_result_set(self, result, path):
        return AuthorizeSecurityGroupIngressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AuthorizeSecurityGroupIngressChoreographyExecution(session, exec_id, path)

class AuthorizeSecurityGroupIngressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AuthorizeSecurityGroupIngress
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
    def set_GroupId(self, value):
        """
        Set the value of the GroupId input for this Choreo. ((conditional, string) The ID of the security group to modify. Can be used instead of GroupName.)
        """
        InputSet._set_input(self, 'GroupId', value)
    def set_GroupName(self, value):
        """
        Set the value of the GroupName input for this Choreo. ((conditional, string) The name of the security group to modify. Can be used instead of GroupId.)
        """
        InputSet._set_input(self, 'GroupName', value)
    def set_IpPermissionsCidrIp(self, value):
        """
        Set the value of the IpPermissionsCidrIp input for this Choreo. ((optional, string) The CIDR range. Cannot be used when specifying a source security group.)
        """
        InputSet._set_input(self, 'IpPermissionsCidrIp', value)
    def set_IpPermissionsFromPort(self, value):
        """
        Set the value of the IpPermissionsFromPort input for this Choreo. ((optional, integer) The start of port range for the TCP and UDP protocols, or an ICMP type number. For the ICMP type number, you can use -1 to specify all ICMP types.)
        """
        InputSet._set_input(self, 'IpPermissionsFromPort', value)
    def set_IpPermissionsGroupId(self, value):
        """
        Set the value of the IpPermissionsGroupId input for this Choreo. ((optional, string) The ID of the source security group. Cannot be used when specifying a CIDR IP address.)
        """
        InputSet._set_input(self, 'IpPermissionsGroupId', value)
    def set_IpPermissionsGroupName(self, value):
        """
        Set the value of the IpPermissionsGroupName input for this Choreo. ((optional, string) The name of the source security group. Cannot be used when specifying a CIDR IP address.)
        """
        InputSet._set_input(self, 'IpPermissionsGroupName', value)
    def set_IpPermissionsIpProtocol(self, value):
        """
        Set the value of the IpPermissionsIpProtocol input for this Choreo. ((required, string) The IP protocol name or number. Valid values for EC2-Classic: tcp, udp, icmp (or 6, 17, 1). Valid values for EC2-VPC: tcp, udp, icmp, any valid protocol number (0-254), or -1 (to specify all).)
        """
        InputSet._set_input(self, 'IpPermissionsIpProtocol', value)
    def set_IpPermissionsToPort(self, value):
        """
        Set the value of the IpPermissionsToPort input for this Choreo. ((optional, integer) The end of port range for the TCP and UDP protocols, or an ICMP code number. For the ICMP code number, you can use -1 to specify all ICMP codes for the given ICMP type.)
        """
        InputSet._set_input(self, 'IpPermissionsToPort', value)
    def set_IpPermissionsUserId(self, value):
        """
        Set the value of the IpPermissionsUserId input for this Choreo. ((optional, string) The AWS account ID that owns the source security group. Cannot be used when specifying a CIDR IP address.)
        """
        InputSet._set_input(self, 'IpPermissionsUserId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class AuthorizeSecurityGroupIngressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AuthorizeSecurityGroupIngress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class AuthorizeSecurityGroupIngressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AuthorizeSecurityGroupIngressResultSet(response, path)
