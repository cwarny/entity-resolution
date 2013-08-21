# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateSubscription
# Subscribes a customer to a specified plan.
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

class UpdateSubscription(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateSubscription Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Subscriptions/UpdateSubscription')


    def new_input_set(self):
        return UpdateSubscriptionInputSet()

    def _make_result_set(self, result, path):
        return UpdateSubscriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateSubscriptionChoreographyExecution(session, exec_id, path)

class UpdateSubscriptionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateSubscription
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Coupon(self, value):
        """
        Set the value of the Coupon input for this Choreo. ((optional, string) If you provide a coupon code, it can be specified here)
        """
        InputSet._set_input(self, 'Coupon', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The unique identifier of the customer you want to subscribe to a plan)
        """
        InputSet._set_input(self, 'CustomerID', value)
    def set_Plan(self, value):
        """
        Set the value of the Plan input for this Choreo. ((required, string) The unique identifier of the plan to subscribe the customer to)
        """
        InputSet._set_input(self, 'Plan', value)
    def set_Prorate(self, value):
        """
        Set the value of the Prorate input for this Choreo. ((optional, boolean) When set to 1, Stripe will prorate switching plans during a billing cycle. When set to 0, this feature is disabled. Defaults to 1.)
        """
        InputSet._set_input(self, 'Prorate', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((optional, string) The token associated with a set of credit card details. This can be used as an alternative to specifying credit card details.)
        """
        InputSet._set_input(self, 'Token', value)
    def set_TrialEnd(self, value):
        """
        Set the value of the TrialEnd input for this Choreo. ((optional, date) A timestamp representing the end of the trial period in UTC. The customer will not be charged during the trial period.)
        """
        InputSet._set_input(self, 'TrialEnd', value)

class UpdateSubscriptionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateSubscription Choreo.
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
        Subscriptions allow you to charge a customer's card on a recurring basis. A subscription ties a customer to a particular plan you've created.
        """
        return StripeSubscription(self.getJSONFromString(self._output.get('Response', [])))

class UpdateSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateSubscriptionResultSet(response, path)
