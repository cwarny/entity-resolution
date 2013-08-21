# -*- coding: utf-8 -*-

###############################################################################
#
# ListQueues
# Returns a list of your queues.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListQueues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListQueues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SQS/ListQueues')


    def new_input_set(self):
        return ListQueuesInputSet()

    def _make_result_set(self, result, path):
        return ListQueuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListQueuesChoreographyExecution(session, exec_id, path)

class ListQueuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListQueues
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
    def set_QueueNamePrefix(self, value):
        """
        Set the value of the QueueNamePrefix input for this Choreo. ((optional, string) A string used to filter the list of queues.)
        """
        InputSet._set_input(self, 'QueueNamePrefix', value)

class ListQueuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListQueues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class ListQueuesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListQueuesResultSet(response, path)
