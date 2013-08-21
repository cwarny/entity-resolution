# -*- coding: utf-8 -*-

###############################################################################
#
# ListOrdersWithBuyerEmail
# Returns orders associated with a buyer's email address that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListOrdersWithBuyerEmail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListOrdersWithBuyerEmail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Orders/ListOrdersWithBuyerEmail')


    def new_input_set(self):
        return ListOrdersWithBuyerEmailInputSet()

    def _make_result_set(self, result, path):
        return ListOrdersWithBuyerEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListOrdersWithBuyerEmailChoreographyExecution(session, exec_id, path)

class ListOrdersWithBuyerEmailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListOrdersWithBuyerEmail
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
    def set_BuyerEmail(self, value):
        """
        Set the value of the BuyerEmail input for this Choreo. ((required, string) The e-mail address of a buyer. Used to select only the orders that contain the specified e-mail address.)
        """
        InputSet._set_input(self, 'BuyerEmail', value)
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

class ListOrdersWithBuyerEmailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListOrdersWithBuyerEmail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class ListOrdersWithBuyerEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListOrdersWithBuyerEmailResultSet(response, path)
