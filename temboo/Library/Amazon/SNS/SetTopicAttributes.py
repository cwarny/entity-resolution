# -*- coding: utf-8 -*-

###############################################################################
#
# SetTopicAttributes
# Allows a topic owner to update the attribute of a topic to a new value.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SetTopicAttributes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetTopicAttributes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/SetTopicAttributes')


    def new_input_set(self):
        return SetTopicAttributesInputSet()

    def _make_result_set(self, result, path):
        return SetTopicAttributesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetTopicAttributesChoreographyExecution(session, exec_id, path)

class SetTopicAttributesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetTopicAttributes
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
    def set_AttributeName(self, value):
        """
        Set the value of the AttributeName input for this Choreo. ((required, string) The name of the attribute you want to modify. Valid values are: Policy and DisplayName.)
        """
        InputSet._set_input(self, 'AttributeName', value)
    def set_AttributeValue(self, value):
        """
        Set the value of the AttributeValue input for this Choreo. ((required, string) The new value for the attribute that you want to update.)
        """
        InputSet._set_input(self, 'AttributeValue', value)
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic that has an attribute that you want to set.)
        """
        InputSet._set_input(self, 'TopicArn', value)

class SetTopicAttributesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetTopicAttributes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class SetTopicAttributesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetTopicAttributesResultSet(response, path)
