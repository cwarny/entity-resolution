# -*- coding: utf-8 -*-

###############################################################################
#
# Purchase
# Returns lifecycle emissions for any good or service. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Purchase(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Purchase Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Purchase')


    def new_input_set(self):
        return PurchaseInputSet()

    def _make_result_set(self, result, path):
        return PurchaseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PurchaseChoreographyExecution(session, exec_id, path)

class PurchaseInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Purchase
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Cost(self, value):
        """
        Set the value of the Cost input for this Choreo. ((optional, decimal) The cost associated with the purchase.)
        """
        InputSet._set_input(self, 'Cost', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The date of the purchase in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Industry(self, value):
        """
        Set the value of the Industry input for this Choreo. ((optional, integer) An industry code (NAICS CODE) corresponding to the industry to return results for. For example, the id for Audio and Video Equipment Manufacturing is 334310.)
        """
        InputSet._set_input(self, 'Industry', value)
    def set_MerchantCategory(self, value):
        """
        Set the value of the MerchantCategory input for this Choreo. ((optional, string) The id for a merchant category.)
        """
        InputSet._set_input(self, 'MerchantCategory', value)
    def set_Merchant(self, value):
        """
        Set the value of the Merchant input for this Choreo. ((optional, integer) An id corresponding to a merchant that you want to return data for.)
        """
        InputSet._set_input(self, 'Merchant', value)
    def set_PurchaseAmount(self, value):
        """
        Set the value of the PurchaseAmount input for this Choreo. ((optional, decimal) The purchase amount.)
        """
        InputSet._set_input(self, 'PurchaseAmount', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SicIndustry(self, value):
        """
        Set the value of the SicIndustry input for this Choreo. ((optional, integer) A Sic Industry id (i.e. 0111 is the code for Wheat, 0112 is the code for Rice, etc).)
        """
        InputSet._set_input(self, 'SicIndustry', value)
    def set_Tax(self, value):
        """
        Set the value of the Tax input for this Choreo. ((optional, decimal) The tax amount for the purchase.)
        """
        InputSet._set_input(self, 'Tax', value)
    def set_Timeframe(self, value):
        """
        Set the value of the Timeframe input for this Choreo. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        InputSet._set_input(self, 'Timeframe', value)

class PurchaseResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Purchase Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class PurchaseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PurchaseResultSet(response, path)
