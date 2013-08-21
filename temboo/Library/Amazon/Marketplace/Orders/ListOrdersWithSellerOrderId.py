# -*- coding: utf-8 -*-

###############################################################################
#
# ListOrdersWithSellerOrderId
# Returns orders associated with a seller order id that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListOrdersWithSellerOrderId(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListOrdersWithSellerOrderId Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Orders/ListOrdersWithSellerOrderId')


    def new_input_set(self):
        return ListOrdersWithSellerOrderIdInputSet()

    def _make_result_set(self, result, path):
        return ListOrdersWithSellerOrderIdResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListOrdersWithSellerOrderIdChoreographyExecution(session, exec_id, path)

class ListOrdersWithSellerOrderIdInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListOrdersWithSellerOrderId
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
    def set_CreatedAfter(self, value):
        """
        Set the value of the CreatedAfter input for this Choreo. ((optional, date) A date used for selecting orders created after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01). Defaults to today's date if not provided.)
        """
        InputSet._set_input(self, 'CreatedAfter', value)
    def set_CreatedBefore(self, value):
        """
        Set the value of the CreatedBefore input for this Choreo. ((optional, date) A date used for selecting orders created before (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01).)
        """
        InputSet._set_input(self, 'CreatedBefore', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((conditional, string) The base URL for the MWS endpoint. Defaults to mws.amazonservices.co.uk.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_MaxResultsPerPage(self, value):
        """
        Set the value of the MaxResultsPerPage input for this Choreo. ((optional, integer) A number that indicates the maximum number of orders that can be returned per page. Valid values are: 1-100.)
        """
        InputSet._set_input(self, 'MaxResultsPerPage', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SellerOrderId(self, value):
        """
        Set the value of the SellerOrderId input for this Choreo. ((required, string) An order identifier that is specified by the seller.)
        """
        InputSet._set_input(self, 'SellerOrderId', value)

class ListOrdersWithSellerOrderIdResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListOrdersWithSellerOrderId Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class ListOrdersWithSellerOrderIdChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListOrdersWithSellerOrderIdResultSet(response, path)
