# -*- coding: utf-8 -*-

###############################################################################
#
# ChangeMessageVisibility
# Updates the visibility timeout parameter of a message.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ChangeMessageVisibility(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ChangeMessageVisibility Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/ChangeMessageVisibility')


    def new_input_set(self):
        return ChangeMessageVisibilityInputSet()

    def _make_result_set(self, result, path):
        return ChangeMessageVisibilityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChangeMessageVisibilityChoreographyExecution(session, exec_id, path)

class ChangeMessageVisibilityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ChangeMessageVisibility
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The AWS account id associated with the queue. Enter account number omitting any dashes.)
        """
        InputSet._set_input(self, 'AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue that contains the message.)
        """
        InputSet._set_input(self, 'QueueName', value)
    def set_ReceiptHandle(self, value):
        """
        Set the value of the ReceiptHandle input for this Choreo. ((required, string) The receipt handle associated with the message you want to modify. This is returned in the RecieveMessage request.)
        """
        InputSet._set_input(self, 'ReceiptHandle', value)
    def set_VisibilityTimeout(self, value):
        """
        Set the value of the VisibilityTimeout input for this Choreo. ((required, integer) The new value for the visibility timeout of the message (in seconds).)
        """
        InputSet._set_input(self, 'VisibilityTimeout', value)

class ChangeMessageVisibilityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ChangeMessageVisibility Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class ChangeMessageVisibilityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ChangeMessageVisibilityResultSet(response, path)
