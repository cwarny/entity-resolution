# -*- coding: utf-8 -*-

###############################################################################
#
# UpdatePriceAndQuantity
# Updates only the price and quantity of a particular product with a given product SKU.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdatePriceAndQuantity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdatePriceAndQuantity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/UpdatePriceAndQuantity')


    def new_input_set(self):
        return UpdatePriceAndQuantityInputSet()

    def _make_result_set(self, result, path):
        return UpdatePriceAndQuantityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdatePriceAndQuantityChoreographyExecution(session, exec_id, path)

class UpdatePriceAndQuantityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdatePriceAndQuantity
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
    def set_Price(self, value):
        """
        Set the value of the Price input for this Choreo. ((required, decimal) Enter the unit price for this product. The price must be greater than 0.00. Do NOT include the currency symbol (e.g. $).)
        """
        InputSet._set_input(self, 'Price', value)
    def set_Quantity(self, value):
        """
        Set the value of the Quantity input for this Choreo. ((required, integer) Enter the quantity of the product you have for sale. The quantity must be a whole number, and should be greater than zero.)
        """
        InputSet._set_input(self, 'Quantity', value)
    def set_SKU(self, value):
        """
        Set the value of the SKU input for this Choreo. ((required, string) A SKU is a "Stock Keeping Unit" which you can assign to your products to track your inventory. Provide the SKU that you want to modify.)
        """
        InputSet._set_input(self, 'SKU', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        InputSet._set_input(self, 'TimeToWait', value)

class UpdatePriceAndQuantityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdatePriceAndQuantity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ProcessingStatus(self):
        """
        Retrieve the value for the "ProcessingStatus" output from this Choreo execution. ((string) The processing status of the feed submission which is parsed from the Amazon response.)
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

class UpdatePriceAndQuantityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdatePriceAndQuantityResultSet(response, path)
