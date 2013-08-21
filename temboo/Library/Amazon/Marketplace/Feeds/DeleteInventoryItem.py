# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteInventoryItem
# Deletes an individual inventory listings from a Seller Central account with a given SKU.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteInventoryItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteInventoryItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Feeds/DeleteInventoryItem')


    def new_input_set(self):
        return DeleteInventoryItemInputSet()

    def _make_result_set(self, result, path):
        return DeleteInventoryItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteInventoryItemChoreographyExecution(session, exec_id, path)

class DeleteInventoryItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteInventoryItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_SKU(self, value):
        """
        Set the value of the SKU input for this Choreo. ((required, string) A individual SKU associating with the product to delete.)
        """
        InputSet._set_input(self, 'SKU', value)
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
    def set_DeleteOptions(self, value):
        """
        Set the value of the DeleteOptions input for this Choreo. ((optional, string) Use 'd' to reduce the listings inventory to 0 and keep details in the system. Use 'x'  to completely delete listings from your current inventory. Defaults to "d".)
        """
        InputSet._set_input(self, 'DeleteOptions', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_TimeToWait(self, value):
        """
        Set the value of the TimeToWait input for this Choreo. ((optional, integer) By default, the Choreo will wait for 10 minutes to see if the report is ready for retrieval. Max is 120 minutes.)
        """
        InputSet._set_input(self, 'TimeToWait', value)


class DeleteInventoryItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteInventoryItem Choreo.
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

class DeleteInventoryItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteInventoryItemResultSet(response, path)
