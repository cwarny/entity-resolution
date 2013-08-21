# -*- coding: utf-8 -*-

###############################################################################
#
# GetProductCategoriesForSKU
# Returns the product categories that a product belongs to, including parent categories back to the root for the marketplace. This method uses a MarketplaceId and a SellerSKU to uniquely identify a product.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetProductCategoriesForSKU(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetProductCategoriesForSKU Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Products/GetProductCategoriesForSKU')


    def new_input_set(self):
        return GetProductCategoriesForSKUInputSet()

    def _make_result_set(self, result, path):
        return GetProductCategoriesForSKUResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetProductCategoriesForSKUChoreographyExecution(session, exec_id, path)

class GetProductCategoriesForSKUInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetProductCategoriesForSKU
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
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SellerSKU(self, value):
        """
        Set the value of the SellerSKU input for this Choreo. ((required, string) A SellerSKU value used to identify a product in the given marketplace.)
        """
        InputSet._set_input(self, 'SellerSKU', value)

class GetProductCategoriesForSKUResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetProductCategoriesForSKU Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class GetProductCategoriesForSKUChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetProductCategoriesForSKUResultSet(response, path)
