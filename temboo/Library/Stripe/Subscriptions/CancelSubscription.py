# -*- coding: utf-8 -*-

###############################################################################
#
# CancelSubscription
# Cancels an existing subscription.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeSubscription import StripeSubscription

import json

class CancelSubscription(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CancelSubscription Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Subscriptions/CancelSubscription')


    def new_input_set(self):
        return CancelSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return CancelSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CancelSubscriptionChoreographyExecution(session, exec_id, path)

class CancelSubscriptionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CancelSubscription
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AtPeriodEnd(self, value):
        """
        Set the value of the AtPeriodEnd input for this Choreo. ((optional, boolean) Delays the cancellation of the subscription until the end of the current period when set to 1. Defaults to 0.)
        """
        InputSet._set_input(self, 'AtPeriodEnd', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The id of the customer whose subscription you want to cancel)
        """
        InputSet._set_input(self, 'CustomerID', value)

class CancelSubscriptionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CancelSubscription Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getSubscription(self):
        """
        a Stripe Subscription
        """
        return StripeSubscription(self.getJSONFromString(self._output.get('Response', [])))

class CancelSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CancelSubscriptionResultSet(response, path)
