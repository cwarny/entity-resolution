# -*- coding: utf-8 -*-

###############################################################################
#
# Automobile
# Returns greenhouse gas modeling for passenger vehicles operated over periods of time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Automobile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Automobile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Automobile')


    def new_input_set(self):
        return AutomobileInputSet()

    def _make_result_set(self, result, path):
        return AutomobileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AutomobileChoreographyExecution(session, exec_id, path)

class AutomobileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Automobile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Acquisition(self, value):
        """
        Set the value of the Acquisition input for this Choreo. ((optional, string) Date automobile was acquired in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Acquisition', value)
    def set_AnnualDistance(self, value):
        """
        Set the value of the AnnualDistance input for this Choreo. ((optional, decimal) Annual distance traveled in kilometres.)
        """
        InputSet._set_input(self, 'AnnualDistance', value)
    def set_AnnualFuelUse(self, value):
        """
        Set the value of the AnnualFuelUse input for this Choreo. ((optional, decimal) Total fuel used in one year in litres.)
        """
        InputSet._set_input(self, 'AnnualFuelUse', value)
    def set_AutomobileFuel(self, value):
        """
        Set the value of the AutomobileFuel input for this Choreo. ((optional, string) Fuel used by automobile (e.g. regular gasoline).)
        """
        InputSet._set_input(self, 'AutomobileFuel', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) ISO code of the country. Defaults to 3166.)
        """
        InputSet._set_input(self, 'Country', value)
    def set_DailyDistance(self, value):
        """
        Set the value of the DailyDistance input for this Choreo. ((optional, decimal) Daily distance traveled on average in kilometres.)
        """
        InputSet._set_input(self, 'DailyDistance', value)
    def set_DailyDuration(self, value):
        """
        Set the value of the DailyDuration input for this Choreo. ((optional, integer) Average amount of time used daily in seconds.)
        """
        InputSet._set_input(self, 'DailyDuration', value)
    def set_FuelEfficiency(self, value):
        """
        Set the value of the FuelEfficiency input for this Choreo. ((optional, decimal) The automobile's fuel efficiency in kilometres per litre.)
        """
        InputSet._set_input(self, 'FuelEfficiency', value)
    def set_FuelUse(self, value):
        """
        Set the value of the FuelUse input for this Choreo. ((optional, decimal) Amount of fuel used in litres.)
        """
        InputSet._set_input(self, 'FuelUse', value)
    def set_Hybridity(self, value):
        """
        Set the value of the Hybridity input for this Choreo. ((optional, boolean) Enter whether the automobile is a hybrid.)
        """
        InputSet._set_input(self, 'Hybridity', value)
    def set_Make(self, value):
        """
        Set the value of the Make input for this Choreo. ((optional, string) Automobile make (e.g. Honda).)
        """
        InputSet._set_input(self, 'Make', value)
    def set_Model(self, value):
        """
        Set the value of the Model input for this Choreo. ((optional, string) Model of automobile (e.g. Civic, Accord).)
        """
        InputSet._set_input(self, 'Model', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Retirement(self, value):
        """
        Set the value of the Retirement input for this Choreo. ((optional, string) Date automobile is retired from use in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Retirement', value)
    def set_SizeClass(self, value):
        """
        Set the value of the SizeClass input for this Choreo. ((optional, string) Automobile size class (e.g. midsize car, large van).)
        """
        InputSet._set_input(self, 'SizeClass', value)
    def set_Speed(self, value):
        """
        Set the value of the Speed input for this Choreo. ((optional, decimal) Enter average speed when in use in kilometres per hour.)
        """
        InputSet._set_input(self, 'Speed', value)
    def set_Urbanity(self, value):
        """
        Set the value of the Urbanity input for this Choreo. ((optional, boolean) Enter whether the trip is in an urban area.)
        """
        InputSet._set_input(self, 'Urbanity', value)
    def set_WeeklyDistance(self, value):
        """
        Set the value of the WeeklyDistance input for this Choreo. ((optional, integer) Enter average weekly distance automobile travels in kilometres.)
        """
        InputSet._set_input(self, 'WeeklyDistance', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((optional, integer) Year that automobile was manufactured.)
        """
        InputSet._set_input(self, 'Year', value)

class AutomobileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Automobile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class AutomobileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AutomobileResultSet(response, path)
