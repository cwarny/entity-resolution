# -*- coding: utf-8 -*-

###############################################################################
#
# CreateOrder
# Populates a shopping cart and sends order information to your merchant  account allowing a user to complete an order using Google Checkout.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateOrder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateOrder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Checkout/CreateOrder')


    def new_input_set(self):
        return CreateOrderInputSet()

    def _make_result_set(self, result, path):
        return CreateOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateOrderChoreographyExecution(session, exec_id, path)

class CreateOrderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateOrder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to checkout.google.com when running in production. Defaults to sandbox.google.com for sandbox testing.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_ItemDescription(self, value):
        """
        Set the value of the ItemDescription input for this Choreo. ((string) The description of the shopping cart item)
        """
        InputSet._set_input(self, 'ItemDescription', value)
    def set_ItemName(self, value):
        """
        Set the value of the ItemName input for this Choreo. ((string) A name of the shopping cart item)
        """
        InputSet._set_input(self, 'ItemName', value)
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
    def set_Quanity(self, value):
        """
        Set the value of the Quanity input for this Choreo. ((integer) The quantity of the shopping cart item)
        """
        InputSet._set_input(self, 'Quanity', value)
    def set_ShippingMethod(self, value):
        """
        Set the value of the ShippingMethod input for this Choreo. ((string) The shipping method for the order (i.e. SuperShip Ground))
        """
        InputSet._set_input(self, 'ShippingMethod', value)
    def set_ShippingPrice(self, value):
        """
        Set the value of the ShippingPrice input for this Choreo. ((decimal) The shipping price for the order)
        """
        InputSet._set_input(self, 'ShippingPrice', value)
    def set_UnitPrice(self, value):
        """
        Set the value of the UnitPrice input for this Choreo. ((decimal) The unit price of the item that is added to the shopping cart)
        """
        InputSet._set_input(self, 'UnitPrice', value)

class CreateOrderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateOrder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Google.  Contains the redirect URL that a customer will use to complete the order.)
        """
        return self._output.get('Response', None)

class CreateOrderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateOrderResultSet(response, path)
