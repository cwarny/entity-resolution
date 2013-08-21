# -*- coding: utf-8 -*-

###############################################################################
#
# ConfirmSubscription
# Verifies that the endpoint owner wishes to receive messages by verifying the token sent during the Subscribe action.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ConfirmSubscription(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ConfirmSubscription Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/SNS/ConfirmSubscription')


    def new_input_set(self):
        return ConfirmSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return ConfirmSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConfirmSubscriptionChoreographyExecution(session, exec_id, path)

class ConfirmSubscriptionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ConfirmSubscription
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
    def set_AuthenticateOnUnsubscribed(self, value):
        """
        Set the value of the AuthenticateOnUnsubscribed input for this Choreo. ((optional, boolean) Indicates that you want to disable the ability to unsubscribe from the subscription without authenticating. Specify 1 to enable this flag.)
        """
        InputSet._set_input(self, 'AuthenticateOnUnsubscribed', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The short-lived token sent to an endpoint during the Subscribe action.)
        """
        InputSet._set_input(self, 'Token', value)
    def set_TopicArn(self, value):
        """
        Set the value of the TopicArn input for this Choreo. ((required, string) The ARN of the topic you want to confirm a subscription for.)
        """
        InputSet._set_input(self, 'TopicArn', value)

class ConfirmSubscriptionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ConfirmSubscription Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class ConfirmSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConfirmSubscriptionResultSet(response, path)
