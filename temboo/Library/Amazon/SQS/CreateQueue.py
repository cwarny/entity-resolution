# -*- coding: utf-8 -*-

###############################################################################
#
# CreateQueue
# Creates a new queue with a specified queue name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateQueue(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateQueue Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/CreateQueue')


    def new_input_set(self):
        return CreateQueueInputSet()

    def _make_result_set(self, result, path):
        return CreateQueueResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateQueueChoreographyExecution(session, exec_id, path)

class CreateQueueInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateQueue
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
    def set_DefaultVisibilityTimeout(self, value):
        """
        Set the value of the DefaultVisibilityTimeout input for this Choreo. ((optional, integer) The visibility timeout (in seconds) to use for the newly created queue.)
        """
        InputSet._set_input(self, 'DefaultVisibilityTimeout', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue you want to create.)
        """
        InputSet._set_input(self, 'QueueName', value)

class CreateQueueResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateQueue Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateQueueChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateQueueResultSet(response, path)
