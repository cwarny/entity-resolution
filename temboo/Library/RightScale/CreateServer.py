# -*- coding: utf-8 -*-

###############################################################################
#
# CreateServer
# Creates a RightScale server instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateServer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateServer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RightScale/CreateServer')


    def new_input_set(self):
        return CreateServerInputSet()

    def _make_result_set(self, result, path):
        return CreateServerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateServerChoreographyExecution(session, exec_id, path)

class CreateServerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateServer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AKIImage(self, value):
        """
        Set the value of the AKIImage input for this Choreo. ((optional, string) The URL to the AKI image.)
        """
        InputSet._set_input(self, 'AKIImage', value)
    def set_ARIImage(self, value):
        """
        Set the value of the ARIImage input for this Choreo. ((optional, string) The URL to the ARI Image.)
        """
        InputSet._set_input(self, 'ARIImage', value)
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, integer) The RightScale Account ID.)
        """
        InputSet._set_input(self, 'AccountID', value)
    def set_CloudID(self, value):
        """
        Set the value of the CloudID input for this Choreo. ((optional, integer) The cloud region identifier. If undefined, the default is 1 (us-east).)
        """
        InputSet._set_input(self, 'CloudID', value)
    def set_EC2AvailabilityZone(self, value):
        """
        Set the value of the EC2AvailabilityZone input for this Choreo. ((optional, string) The  EC2 availablity zone, for example: us-east-1a, or any.  Do not set, if also passing the vpc_subnet_href parameter.)
        """
        InputSet._set_input(self, 'EC2AvailabilityZone', value)
    def set_EC2Image(self, value):
        """
        Set the value of the EC2Image input for this Choreo. ((optional, string) The URL to AMI image.)
        """
        InputSet._set_input(self, 'EC2Image', value)
    def set_EC2SSHKeyHref(self, value):
        """
        Set the value of the EC2SSHKeyHref input for this Choreo. ((optional, string) The URL to the SSH Key.)
        """
        InputSet._set_input(self, 'EC2SSHKeyHref', value)
    def set_EC2SecurityGroupsHref(self, value):
        """
        Set the value of the EC2SecurityGroupsHref input for this Choreo. ((optional, string) The URL(s) to security group(s). Do not set, if also passing the vpc_subnet_href parameter.)
        """
        InputSet._set_input(self, 'EC2SecurityGroupsHref', value)
    def set_InstanceType(self, value):
        """
        Set the value of the InstanceType input for this Choreo. ((optional, string) The AWS instance type: small, medium, etc.)
        """
        InputSet._set_input(self, 'InstanceType', value)
    def set_MaxSpotPrice(self, value):
        """
        Set the value of the MaxSpotPrice input for this Choreo. ((optional, integer) The maximum price (a dollar value) dollars) per hour for the spot server.)
        """
        InputSet._set_input(self, 'MaxSpotPrice', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Pricing(self, value):
        """
        Set the value of the Pricing input for this Choreo. ((optional, string) AWS pricing.  Specify on_demand, or spot.)
        """
        InputSet._set_input(self, 'Pricing', value)
    def set_ServerDeployment(self, value):
        """
        Set the value of the ServerDeployment input for this Choreo. ((required, string) The URL of the deployment that this server wil be added to.)
        """
        InputSet._set_input(self, 'ServerDeployment', value)
    def set_ServerNickname(self, value):
        """
        Set the value of the ServerNickname input for this Choreo. ((required, string) The nickname for the server being created.)
        """
        InputSet._set_input(self, 'ServerNickname', value)
    def set_ServerTemplate(self, value):
        """
        Set the value of the ServerTemplate input for this Choreo. ((required, string) The URL to a server template.)
        """
        InputSet._set_input(self, 'ServerTemplate', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The username obtained from RightScale.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_VPCSubnet(self, value):
        """
        Set the value of the VPCSubnet input for this Choreo. ((optional, string) The href to the VPC subnet.)
        """
        InputSet._set_input(self, 'VPCSubnet', value)

class CreateServerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateServer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)

class CreateServerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateServerResultSet(response, path)
