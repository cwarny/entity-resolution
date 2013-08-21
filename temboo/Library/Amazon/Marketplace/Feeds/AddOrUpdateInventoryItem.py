# -*- coding: utf-8 -*-

###############################################################################
#
# AddOrUpdateInventoryItem
# Add or update an individual inventory listing.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddOrUpdateInventoryItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddOrUpdateInventoryItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/AddOrUpdateInventoryItem')


    def new_input_set(self):
        return AddOrUpdateInventoryItemInputSet()

    def _make_result_set(self, result, path):
        return AddOrUpdateInventoryItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddOrUpdateInventoryItemChoreographyExecution(session, exec_id, path)

class AddOrUpdateInventoryItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddOrUpdateInventoryItem
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
    def set_ExpeditedShipping(self, value):
        """
        Set the value of the ExpeditedShipping input for this Choreo. ((optional, string) The expedited shipping options that you offer for this item. Valid values: 3 = UK Only; N = None, no express delivery offered.)
        """
        InputSet._set_input(self, 'ExpeditedShipping', value)
    def set_FulfillmentCenterId(self, value):
        """
        Set the value of the FulfillmentCenterId input for this Choreo. ((conditional, string) For those merchants using Amazon fulfillment services, this designates which fulfillment network will be used. Required when using Amazon fulfillment services. Valid values are: AMAZON_EU, DEFAULT.)
        """
        InputSet._set_input(self, 'FulfillmentCenterId', value)
    def set_ItemCondition(self, value):
        """
        Set the value of the ItemCondition input for this Choreo. ((conditional, integer) A numerical entry that indicates the condition of the item. Required for new listings. Valid values are: 1-11. See documentation for description of item condition numeric values.)
        """
        InputSet._set_input(self, 'ItemCondition', value)
    def set_ItemNote(self, value):
        """
        Set the value of the ItemNote input for this Choreo. ((optional, string) A description or note for the item you're adding or updating.)
        """
        InputSet._set_input(self, 'ItemNote', value)
    def set_Price(self, value):
        """
        Set the value of the Price input for this Choreo. ((conditional, decimal) The price at which the merchant offers the product for sale. Required if ProductId is provided.)
        """
        InputSet._set_input(self, 'Price', value)
    def set_ProductIdType(self, value):
        """
        Set the value of the ProductIdType input for this Choreo. ((conditional, integer) The type of standard, unique identifier entered in the product-id field. This is a required field if product-id is provided. Valid values are: 1 (ASIN), 2 (ISBN), 3 (UPC), 4  (EAN).)
        """
        InputSet._set_input(self, 'ProductIdType', value)
    def set_ProductId(self, value):
        """
        Set the value of the ProductId input for this Choreo. ((conditional, string) A standard, alphanumeric string that uniquely identifies the product. This could be a UPC, EAN or ISBN.  This is a required field if product-id-type is provided.)
        """
        InputSet._set_input(self, 'ProductId', value)
    def set_Quantity(self, value):
        """
        Set the value of the Quantity input for this Choreo. ((conditional, integer) Enter the quantity of the item you are making available for sale. Required for merchant-fulfilled items. Leave blank for amazon-fullfilled items.)
        """
        InputSet._set_input(self, 'Quantity', value)
    def set_SKU(self, value):
        """
        Set the value of the SKU input for this Choreo. ((required, string) A unique identifier for the product, assigned by the merchant. The SKU must be unique for each product listed.)
        """
        InputSet._set_input(self, 'SKU', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        InputSet._set_input(self, 'TimeToWait', value)
    def set_WillShipInternationally(self, value):
        """
        Set the value of the WillShipInternationally input for this Choreo. ((optional, integer) Specify your international shipping options. Valid values are: 3 = UK Only; 4 = UK and Europe; 5 = UK, Europe, and North America; 6 = Worldwide)
        """
        InputSet._set_input(self, 'WillShipInternationally', value)

class AddOrUpdateInventoryItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddOrUpdateInventoryItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ProcessingStatus(self):
        """
        Retrieve the value for the "ProcessingStatus" output from this Choreo execution. ((string) The processing status of the product submission which is parsed from the Amazon response.)
        """
        return self._output.get('ProcessingStatus', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon after submitting the feed.)
        """
        return self._output.get('Response', None)
    def get_SubmissionId(self):
        """
        Retrieve the value for the "SubmissionId" output from this Choreo execution. ((integer) The submission id parsed from the Amazon response.)
        """
        return self._output.get('SubmissionId', None)
    def get_SubmissionResult(self):
        """
        Retrieve the value for the "SubmissionResult" output from this Choreo execution. ((string) The submission result returned from Amazon.)
        """
        return self._output.get('SubmissionResult', None)

class AddOrUpdateInventoryItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddOrUpdateInventoryItemResultSet(response, path)
