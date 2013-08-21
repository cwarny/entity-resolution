# -*- coding: utf-8 -*-

###############################################################################
#
# GetTariffPrice
# Retrieve summarized rates of a specified electricity tariff, in addition to changes in rates over a specified time span.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTariffPrice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTariffPrice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/GetTariffPrice')


    def new_input_set(self):
        return GetTariffPriceInputSet()

    def _make_result_set(self, result, path):
        return GetTariffPriceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTariffPriceChoreographyExecution(session, exec_id, path)

class GetTariffPriceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTariffPrice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((optional, string) The Genability ID for an account. This is optional if MasterTariffID is set.)
        """
        InputSet._set_input(self, 'AccountID', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The App ID provided by Genability.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_ConsumptionAmount(self, value):
        """
        Set the value of the ConsumptionAmount input for this Choreo. ((optional, decimal) Specify a monthly consumption in kWh. By default the highest banded level of consumption is used.)
        """
        InputSet._set_input(self, 'ConsumptionAmount', value)
    def set_DemandAmount(self, value):
        """
        Set the value of the DemandAmount input for this Choreo. ((optional, decimal) Specify a monthly demand in kWh. By default the highest banded level of demand is used.)
        """
        InputSet._set_input(self, 'DemandAmount', value)
    def set_FromDateTime(self, value):
        """
        Set the value of the FromDateTime input for this Choreo. ((required, string) The date and time of the requested start of the price query. Must be in ISO 8601 format.  Example: 2012-06-12T00:00:00.0-0700)
        """
        InputSet._set_input(self, 'FromDateTime', value)
    def set_MasterTariffID(self, value):
        """
        Set the value of the MasterTariffID input for this Choreo. ((optional, string) A Genability tariff ID. This variable is not required, if AccountID is set.)
        """
        InputSet._set_input(self, 'MasterTariffID', value)
    def set_PageCount(self, value):
        """
        Set the value of the PageCount input for this Choreo. ((optional, integer) The number of results to be returned. Defailt is set to: 25.)
        """
        InputSet._set_input(self, 'PageCount', value)
    def set_PageStart(self, value):
        """
        Set the value of the PageStart input for this Choreo. ((optional, integer) The page number to start to display results from. If unspecified, the first page of results will be returned.)
        """
        InputSet._set_input(self, 'PageStart', value)
    def set_TerritoryID(self, value):
        """
        Set the value of the TerritoryID input for this Choreo. ((optional, string) Return rate changes for the specified Territory.)
        """
        InputSet._set_input(self, 'TerritoryID', value)
    def set_ToDateTime(self, value):
        """
        Set the value of the ToDateTime input for this Choreo. ((optional, string) The date and time of the requested start of the price query. Must be in ISO 8601 format.  Example: 2012-06-12T00:00:00.0-0700)
        """
        InputSet._set_input(self, 'ToDateTime', value)

class GetTariffPriceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTariffPrice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTariffPriceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTariffPriceResultSet(response, path)
