# -*- coding: utf-8 -*-

###############################################################################
#
# AddOrUpdateProductImage
# Adds or updates a product image with a given image location and SKU.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddOrUpdateProductImage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddOrUpdateProductImage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/AddOrUpdateProductImage')


    def new_input_set(self):
        return AddOrUpdateProductImageInputSet()

    def _make_result_set(self, result, path):
        return AddOrUpdateProductImageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddOrUpdateProductImageChoreographyExecution(session, exec_id, path)

class AddOrUpdateProductImageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddOrUpdateProductImage
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
    def set_ImageLocation(self, value):
        """
        Set the value of the ImageLocation input for this Choreo. ((required, string) The URL for the image location.)
        """
        InputSet._set_input(self, 'ImageLocation', value)
    def set_ImageType(self, value):
        """
        Set the value of the ImageType input for this Choreo. ((optional, string) The type of image (Main, Alternate, or Swatch). Defaults to "Main".)
        """
        InputSet._set_input(self, 'ImageType', value)
    def set_SKU(self, value):
        """
        Set the value of the SKU input for this Choreo. ((required, string) A SKU is a "Stock Keeping Unit" which you can assign to your products to track your inventory. Provide the SKU for the product that is associated with the image you are uploading.)
        """
        InputSet._set_input(self, 'SKU', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        InputSet._set_input(self, 'TimeToWait', value)

class AddOrUpdateProductImageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddOrUpdateProductImage Choreo.
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

class AddOrUpdateProductImageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddOrUpdateProductImageResultSet(response, path)
