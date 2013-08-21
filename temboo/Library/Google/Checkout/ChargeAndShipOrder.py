# -*- coding: utf-8 -*-

###############################################################################
#
# ChargeAndShipOrder
# Charge and ship an order once a shopping cart order has arrived in your Google Checkout Inbox.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ChargeAndShipOrder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ChargeAndShipOrder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Checkout/ChargeAndShipOrder')


    def new_input_set(self):
        return ChargeAndShipOrderInputSet()

    def _make_result_set(self, result, path):
        return ChargeAndShipOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChargeAndShipOrderChoreographyExecution(session, exec_id, path)

class ChargeAndShipOrderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ChargeAndShipOrder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((decimal) The dollar amount to charge (i.e. 25.50))
        """
        InputSet._set_input(self, 'Amount', value)
    def set_Carrier(self, value):
        """
        Set the value of the Carrier input for this Choreo. ((string) The desired postal carrier (i.e. UPS))
        """
        InputSet._set_input(self, 'Carrier', value)
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
    def set_TrackingNumber(self, value):
        """
        Set the value of the TrackingNumber input for this Choreo. ((string) The tracking number for the order package)
        """
        InputSet._set_input(self, 'TrackingNumber', value)

class ChargeAndShipOrderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ChargeAndShipOrder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Google)
        """
        return self._output.get('Response', None)

class ChargeAndShipOrderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ChargeAndShipOrderResultSet(response, path)
