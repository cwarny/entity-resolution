# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteSecurityGroup
# Deletes a security group using the group name you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteSecurityGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteSecurityGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DeleteSecurityGroup')


    def new_input_set(self):
        return DeleteSecurityGroupInputSet()

    def _make_result_set(self, result, path):
        return DeleteSecurityGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteSecurityGroupChoreographyExecution(session, exec_id, path)

class DeleteSecurityGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteSecurityGroup
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
        Set the value of the GroupId input for this Choreo. ((conditional, string) The id of the security group to delete. Required unless providing the GroupName.)
        """
        InputSet._set_input(self, 'GroupId', value)
    def set_GroupName(self, value):
        """
        Set the value of the GroupName input for this Choreo. ((conditional, string) The name of the security group to delete.Required unless providing the GroupId.)
        """
        InputSet._set_input(self, 'GroupName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, any) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class DeleteSecurityGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteSecurityGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteSecurityGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteSecurityGroupResultSet(response, path)
