# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDeployment
# Create a RightScale Deployment.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateDeployment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDeployment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RightScale/CreateDeployment')


    def new_input_set(self):
        return CreateDeploymentInputSet()

    def _make_result_set(self, result, path):
        return CreateDeploymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDeploymentChoreographyExecution(session, exec_id, path)

class CreateDeploymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDeployment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, integer) The RightScale Account ID.)
        """
        InputSet._set_input(self, 'AccountID', value)
    def set_DeploymentDefaultEC2AvailabilityZone(self, value):
        """
        Set the value of the DeploymentDefaultEC2AvailabilityZone input for this Choreo. ((optional, string) The default EC2 availability zone for this deployment.)
        """
        InputSet._set_input(self, 'DeploymentDefaultEC2AvailabilityZone', value)
    def set_DeploymentDefaultVPCSubnetHref(self, value):
        """
        Set the value of the DeploymentDefaultVPCSubnetHref input for this Choreo. ((optional, string) The href of the vpc subnet.)
        """
        InputSet._set_input(self, 'DeploymentDefaultVPCSubnetHref', value)
    def set_DeploymentDescription(self, value):
        """
        Set the value of the DeploymentDescription input for this Choreo. ((optional, string) The deployment being created.)
        """
        InputSet._set_input(self, 'DeploymentDescription', value)
    def set_DeploymentNickname(self, value):
        """
        Set the value of the DeploymentNickname input for this Choreo. ((required, string) The nickname of the deployment being created.)
        """
        InputSet._set_input(self, 'DeploymentNickname', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        InputSet._set_input(self, 'Username', value)

class CreateDeploymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDeployment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format)
        """
        return self._output.get('Response', None)

class CreateDeploymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDeploymentResultSet(response, path)
