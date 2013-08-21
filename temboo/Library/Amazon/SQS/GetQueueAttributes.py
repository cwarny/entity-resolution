# -*- coding: utf-8 -*-

###############################################################################
#
# GetQueueAttributes
# Retrieves one or all attributes of a queue.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetQueueAttributes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetQueueAttributes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/GetQueueAttributes')


    def new_input_set(self):
        return GetQueueAttributesInputSet()

    def _make_result_set(self, result, path):
        return GetQueueAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetQueueAttributesChoreographyExecution(session, exec_id, path)

class GetQueueAttributesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetQueueAttributes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The AWS account number of the queue owner. Enter account number omitting any dashes.)
        """
        InputSet._set_input(self, 'AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_AttributeName(self, value):
        """
        Set the value of the AttributeName input for this Choreo. ((optional, string) The name of the attribute that you want to retrieve for the specified queue. Defaults to 'All'.)
        """
        InputSet._set_input(self, 'AttributeName', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue to retrieve attributes for.)
        """
        InputSet._set_input(self, 'QueueName', value)

class GetQueueAttributesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetQueueAttributes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetQueueAttributesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetQueueAttributesResultSet(response, path)
