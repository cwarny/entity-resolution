# -*- coding: utf-8 -*-

###############################################################################
#
# Publish
# Sends a message to a topic's subscribed endpoints.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Publish(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Publish Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/Publish')


    def new_input_set(self):
        return PublishInputSet()

    def _make_result_set(self, result, path):
        return PublishResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PublishChoreographyExecution(session, exec_id, path)

class PublishInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Publish
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
    def set_MessageStructure(self, value):
        """
        Set the value of the MessageStructure input for this Choreo. ((optional, string) Can be set to 'json' if you are providing a valid JSON object for the Message input variable.)
        """
        InputSet._set_input(self, 'MessageStructure', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((required, string) The text for the message you want to send to the topic.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((optional, string) The "Subject" line of the message when the message is delivered to e-mail endpoints or as a JSON message.)
        """
        InputSet._set_input(self, 'Subject', value)
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic you want to publish to.)
        """
        InputSet._set_input(self, 'TopicArn', value)

class PublishResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Publish Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class PublishChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PublishResultSet(response, path)
