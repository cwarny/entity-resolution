# -*- coding: utf-8 -*-

###############################################################################
#
# RemovePermission
# Removes the statement from a topic's access control policy that was created with the AddPermission action.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RemovePermission(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RemovePermission Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/RemovePermission')


    def new_input_set(self):
        return RemovePermissionInputSet()

    def _make_result_set(self, result, path):
        return RemovePermissionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RemovePermissionChoreographyExecution(session, exec_id, path)

class RemovePermissionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RemovePermission
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
    def set_Label(self, value):
        """
        Set the value of the Label input for this Choreo. ((required, string) The unique identifier for the policy statement that you want to delete.)
        """
        InputSet._set_input(self, 'Label', value)
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic that has an access control policy you want to adjust.)
        """
        InputSet._set_input(self, 'TopicArn', value)

class RemovePermissionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RemovePermission Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class RemovePermissionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RemovePermissionResultSet(response, path)
