# -*- coding: utf-8 -*-

###############################################################################
#
# GetOrder
# Returns orders based on the AmazonOrderId values that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetOrder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetOrder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Orders/GetOrder')


    def new_input_set(self):
        return GetOrderInputSet()

    def _make_result_set(self, result, path):
        return GetOrderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetOrderChoreographyExecution(session, exec_id, path)

class GetOrderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetOrder
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
    def set_AmazonOrderId(self, value):
        """
        Set the value of the AmazonOrderId input for this Choreo. ((required, string) An AmazonOrderId value used to retrieve the order.)
        """
        InputSet._set_input(self, 'AmazonOrderId', value)
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

class GetOrderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetOrder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class GetOrderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetOrderResultSet(response, path)
