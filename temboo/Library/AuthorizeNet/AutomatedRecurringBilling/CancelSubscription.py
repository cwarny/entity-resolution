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

import json

class CancelSubscription(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CancelSubscription Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/AuthorizeNet/AutomatedRecurringBilling/CancelSubscription')


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
    def set_APILoginId(self, value):
        """
        Set the value of the APILoginId input for this Choreo. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        InputSet._set_input(self, 'APILoginId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_RefId(self, value):
        """
        Set the value of the RefId input for this Choreo. ((optional, string) The merchant assigned reference id for the subscription.)
        """
        InputSet._set_input(self, 'RefId', value)
    def set_SubscriptionId(self, value):
        """
        Set the value of the SubscriptionId input for this Choreo. ((required, integer) The id of the subscription that you want to cancel.)
        """
        InputSet._set_input(self, 'SubscriptionId', value)
    def set_TransactionKey(self, value):
        """
        Set the value of the TransactionKey input for this Choreo. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        InputSet._set_input(self, 'TransactionKey', value)

class CancelSubscriptionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CancelSubscription Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Authorize.net.)
        """
        return self._output.get('Response', None)

class CancelSubscriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CancelSubscriptionResultSet(response, path)
