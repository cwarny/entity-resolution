# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDBSecurityGroup
# Creates a new database security group which you can use to control the access to the database instance.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateDBSecurityGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDBSecurityGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/RDS/CreateDBSecurityGroup')


    def new_input_set(self):
        return CreateDBSecurityGroupInputSet()

    def _make_result_set(self, result, path):
        return CreateDBSecurityGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDBSecurityGroupChoreographyExecution(session, exec_id, path)

class CreateDBSecurityGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDBSecurityGroup
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
    def set_DBSecurityGroupDescription(self, value):
        """
        Set the value of the DBSecurityGroupDescription input for this Choreo. ((required, string) A description for the security group you're creating.)
        """
        InputSet._set_input(self, 'DBSecurityGroupDescription', value)
    def set_DBSecurityGroupName(self, value):
        """
        Set the value of the DBSecurityGroupName input for this Choreo. ((required, string) A unique name for the security group you want to create.)
        """
        InputSet._set_input(self, 'DBSecurityGroupName', value)

class CreateDBSecurityGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDBSecurityGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateDBSecurityGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDBSecurityGroupResultSet(response, path)
