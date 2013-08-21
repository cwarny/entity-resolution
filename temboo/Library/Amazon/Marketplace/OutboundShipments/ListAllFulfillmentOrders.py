# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllFulfillmentOrders
# Returns a list of fulfillment orders fulfilled after (or at) a specified date or by fulfillment method.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListAllFulfillmentOrders(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllFulfillmentOrders Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/OutboundShipments/ListAllFulfillmentOrders')


    def new_input_set(self):
        return ListAllFulfillmentOrdersInputSet()

    def _make_result_set(self, result, path):
        return ListAllFulfillmentOrdersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllFulfillmentOrdersChoreographyExecution(session, exec_id, path)

class ListAllFulfillmentOrdersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllFulfillmentOrders
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSMarketplaceId(self, value):
        """
        Set the value of the AWSMarketplaceId input for this Choreo. ((required, string) The Marketplace ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSMarketplaceId', value)
    def set_AWSMerchantId(self, value):
        """
        Set the value of the AWSMerchantId input for this Choreo. ((required, string) The Merchant ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSMerchantId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_FulfillmentMethod(self, value):
        """
        Set the value of the FulfillmentMethod input for this Choreo. ((optional, string) A value used for selecting fulfillment orders based on their fulfillment method. "Consumer" indicates a customer order, and "Removal" indicates that the inventory should be returned to the specified.)
        """
        InputSet._set_input(self, 'FulfillmentMethod', value)
    def set_QueryStartDateTime(self, value):
        """
        Set the value of the QueryStartDateTime input for this Choreo. ((optional, date) A date used for selecting items that have had changes in inventory availability after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01).)
        """
        InputSet._set_input(self, 'QueryStartDateTime', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListAllFulfillmentOrdersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllFulfillmentOrders Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class ListAllFulfillmentOrdersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllFulfillmentOrdersResultSet(response, path)
