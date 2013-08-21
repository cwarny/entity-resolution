# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopicAttributes
# Returns properties for a specified topic.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTopicAttributes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTopicAttributes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/GetTopicAttributes')


    def new_input_set(self):
        return GetTopicAttributesInputSet()

    def _make_result_set(self, result, path):
        return GetTopicAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopicAttributesChoreographyExecution(session, exec_id, path)

class GetTopicAttributesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTopicAttributes
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
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic you want to retrieve attributes for.)
        """
        InputSet._set_input(self, 'TopicArn', value)

class GetTopicAttributesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopicAttributes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetTopicAttributesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopicAttributesResultSet(response, path)
