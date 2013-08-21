# -*- coding: utf-8 -*-

###############################################################################
#
# RefundOrder
# Allows you to refund an order that's been submitted to your Google Checkout merchant account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RefundOrder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RefundOrder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Checkout/RefundOrder')


    def new_input_set(self):
        return RefundOrderInputSet()

    def _make_result_set(self, result, path):
        return RefundOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RefundOrderChoreographyExecution(session, exec_id, path)

class RefundOrderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RefundOrder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((decimal) The amount to refund)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((string) The comment for the order refund)
        """
        InputSet._set_input(self, 'Comment', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to checkout.google.com when running in production. Defaults to sandbox.google.com for sandbox testing.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_MerchantId(self, value):
        """
        Set the value of the MerchantId input for this Choreo. ((integer) The Merchant Id provided by Google)
        """
        InputSet._set_input(self, 'MerchantId', value)
    def set_MerchantKey(self, value):
        """
        Set the value of the MerchantKey input for this Choreo. ((string) The Merchant Key provided by Google)
        """
        InputSet._set_input(self, 'MerchantKey', value)
    def set_OrderNumber(self, value):
        """
        Set the value of the OrderNumber input for this Choreo. ((integer) The unique identifier for the order (There is an order number column in your Google Checkout Inbox).)
        """
        InputSet._set_input(self, 'OrderNumber', value)
    def set_Reason(self, value):
        """
        Set the value of the Reason input for this Choreo. ((string) The reason for the refund)
        """
        InputSet._set_input(self, 'Reason', value)
    def set_SandboxMode(self, value):
        """
        Set the value of the SandboxMode input for this Choreo. ((optional, boolean) Set this flag to 1 when using this Choreo with the Google Checkout sandbox endpoint (i.e. sandbox.google.com). Defaults to 0.)
        """
        InputSet._set_input(self, 'SandboxMode', value)

class RefundOrderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RefundOrder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ExecutionStatus(self):
        """
        Retrieve the value for the "ExecutionStatus" output from this Choreo execution. (Contains status information on the Choreo execution)
        """
        return self._output.get('ExecutionStatus', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Google)
        """
        return self._output.get('Response', None)

class RefundOrderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RefundOrderResultSet(response, path)
