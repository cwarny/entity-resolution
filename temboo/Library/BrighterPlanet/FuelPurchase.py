# -*- coding: utf-8 -*-

###############################################################################
#
# FuelPurchase
# Returns information about the carbon emissions from using a wide variety of fuel types.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FuelPurchase(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FuelPurchase Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/FuelPurchase')


    def new_input_set(self):
        return FuelPurchaseInputSet()

    def _make_result_set(self, result, path):
        return FuelPurchaseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FuelPurchaseChoreographyExecution(session, exec_id, path)

class FuelPurchaseInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FuelPurchase
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Cost(self, value):
        """
        Set the value of the Cost input for this Choreo. ((optional, decimal) The cost of the fuel purchase.)
        """
        InputSet._set_input(self, 'Cost', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The date of the fuel purchase in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_FuelType(self, value):
        """
        Set the value of the FuelType input for this Choreo. ((optional, string) The fuel type purchases (i.e. Asphalt and Road Oil, Aviation Gasoline, Commercial Coal, Commercial Natural Gas, or Motor Gasoline))
        """
        InputSet._set_input(self, 'FuelType', value)
    def set_PADD(self, value):
        """
        Set the value of the PADD input for this Choreo. ((optional, string) A code for the Petroleum administration for defense districts (1A, 1B, 1C, 2, or 3).)
        """
        InputSet._set_input(self, 'PADD', value)
    def set_Price(self, value):
        """
        Set the value of the Price input for this Choreo. ((optional, string) The price of the fuel.)
        """
        InputSet._set_input(self, 'Price', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) A postal abbreviation for the state where the fuel was purchased.)
        """
        InputSet._set_input(self, 'State', value)
    def set_Timeframe(self, value):
        """
        Set the value of the Timeframe input for this Choreo. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        InputSet._set_input(self, 'Timeframe', value)
    def set_Volume(self, value):
        """
        Set the value of the Volume input for this Choreo. ((optional, decimal) The amount of fuel purchased.)
        """
        InputSet._set_input(self, 'Volume', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((optional, string) The postal code for the area where the fuel was purchased.)
        """
        InputSet._set_input(self, 'ZipCode', value)

class FuelPurchaseResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FuelPurchase Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class FuelPurchaseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FuelPurchaseResultSet(response, path)
