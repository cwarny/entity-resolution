# -*- coding: utf-8 -*-

###############################################################################
#
# CreateGroup
# Creates a new group in your AWS account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateGroup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateGroup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/CreateGroup')


    def new_input_set(self):
        return CreateGroupInputSet()

    def _make_result_set(self, result, path):
        return CreateGroupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateGroupChoreographyExecution(session, exec_id, path)

class CreateGroupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateGroup
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
    def set_GroupName(self, value):
        """
        Set the value of the GroupName input for this Choreo. ((required, string) The name of the group to create.)
        """
        InputSet._set_input(self, 'GroupName', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((optional, string) The path to the group. If it is not included, it defaults to a slash (/).)
        """
        InputSet._set_input(self, 'Path', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class CreateGroupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateGroup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateGroupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateGroupResultSet(response, path)
