# -*- coding: utf-8 -*-

###############################################################################
#
# RebootInstances
# Reboot an instance by specifying the instance id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RebootInstances(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RebootInstances Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/RebootInstances')


    def new_input_set(self):
        return RebootInstancesInputSet()

    def _make_result_set(self, result, path):
        return RebootInstancesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RebootInstancesChoreographyExecution(session, exec_id, path)

class RebootInstancesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RebootInstances
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
    def set_InstanceId(self, value):
        """
        Set the value of the InstanceId input for this Choreo. ((required, string) The ID of the instance to reboot. This can be a comma-separated list of up to 10 instance IDs.)
        """
        InputSet._set_input(self, 'InstanceId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class RebootInstancesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RebootInstances Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class RebootInstancesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RebootInstancesResultSet(response, path)
