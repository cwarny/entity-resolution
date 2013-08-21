# -*- coding: utf-8 -*-

###############################################################################
#
# ListInventorySupplyByDateRange
# Returns information about the availability of a seller's inventory using a given date range.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListInventorySupplyByDateRange(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListInventorySupplyByDateRange Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/Marketplace/Inventory/ListInventorySupplyByDateRange')


    def new_input_set(self):
        return ListInventorySupplyByDateRangeInputSet()

    def _make_result_set(self, result, path):
        return ListInventorySupplyByDateRangeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListInventorySupplyByDateRangeChoreographyExecution(session, exec_id, path)

class ListInventorySupplyByDateRangeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListInventorySupplyByDateRange
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
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((conditional, string) The value returned in the NextPageToken output of this Choreo when there are multiple pages of inventory items to retrieve. Required unless providing QueryStartDateTime.)
        """
        InputSet._set_input(self, 'PageToken', value)
    def set_QueryStartDateTime(self, value):
        """
        Set the value of the QueryStartDateTime input for this Choreo. ((conditional, date) A date used for selecting items that have had changes in inventory availability after (or at) a specified time, in ISO 8601 date format (i.e. 2012-01-01). Required unless providing PageToken.)
        """
        InputSet._set_input(self, 'QueryStartDateTime', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ResponseGroup(self, value):
        """
        Set the value of the ResponseGroup input for this Choreo. ((optional, string) Indicates whether or not to return the SupplyDetail element in the response. Valid values are: "Basic" (does not include SupplyDetail), and "Detailed" (includes SupplyDetail). Defaults to "Basic".)
        """
        InputSet._set_input(self, 'ResponseGroup', value)

class ListInventorySupplyByDateRangeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListInventorySupplyByDateRange Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NextPageToken(self):
        """
        Retrieve the value for the "NextPageToken" output from this Choreo execution. ((string) A token used to retrieve the next page of results. If a token is not returned, there are no more results to retrieve. This token can be passed to the PageToken input of this Choreo.)
        """
        return self._output.get('NextPageToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon.)
        """
        return self._output.get('Response', None)

class ListInventorySupplyByDateRangeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListInventorySupplyByDateRangeResultSet(response, path)
