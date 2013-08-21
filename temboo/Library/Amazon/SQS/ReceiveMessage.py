# -*- coding: utf-8 -*-

###############################################################################
#
# ReceiveMessage
# Returns one or more messages from the specified queue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReceiveMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReceiveMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/ReceiveMessage')


    def new_input_set(self):
        return ReceiveMessageInputSet()

    def _make_result_set(self, result, path):
        return ReceiveMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReceiveMessageChoreographyExecution(session, exec_id, path)

class ReceiveMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReceiveMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The id for the AWS account associated with the queue you're retrieving a message from (remove all dashes in the account number).)
        """
        InputSet._set_input(self, 'AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_AttributeName(self, value):
        """
        Set the value of the AttributeName input for this Choreo. ((optional, string) The attribute you to return. Values are: All (default), SenderId, SentTimestamp, ApproximateReceiveCount, or ApproximateFirstReceiveTimestamp.)
        """
        InputSet._set_input(self, 'AttributeName', value)
    def set_MaxNumberOfMessages(self, value):
        """
        Set the value of the MaxNumberOfMessages input for this Choreo. ((optional, integer) The maximum number of messages to return. Defaults to 1.)
        """
        InputSet._set_input(self, 'MaxNumberOfMessages', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue you want to retrieve a message from.)
        """
        InputSet._set_input(self, 'QueueName', value)
    def set_VisibilityTimeout(self, value):
        """
        Set the value of the VisibilityTimeout input for this Choreo. ((optional, integer) The duration (in seconds) that the received messages are hidden from future retrieve requests after a ReceiveMessage request (max is 43200).)
        """
        InputSet._set_input(self, 'VisibilityTimeout', value)

class ReceiveMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReceiveMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class ReceiveMessageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReceiveMessageResultSet(response, path)
