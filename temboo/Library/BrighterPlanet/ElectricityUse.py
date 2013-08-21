# -*- coding: utf-8 -*-

###############################################################################
#
# ElectricityUse
# Returns information about the carbon footprint of using electricity from the US public grid.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ElectricityUse(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ElectricityUse Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/ElectricityUse')


    def new_input_set(self):
        return ElectricityUseInputSet()

    def _make_result_set(self, result, path):
        return ElectricityUseResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ElectricityUseChoreographyExecution(session, exec_id, path)

class ElectricityUseInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ElectricityUse
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) An iso_3166 country code.)
        """
        InputSet._set_input(self, 'Country', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The date of the electricity use in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Energy(self, value):
        """
        Set the value of the Energy input for this Choreo. ((optional, decimal) The amount of engery in kilowatt hours.)
        """
        InputSet._set_input(self, 'Energy', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) A postal abbreviation for the state to return electricity information for.)
        """
        InputSet._set_input(self, 'State', value)
    def set_Timeframe(self, value):
        """
        Set the value of the Timeframe input for this Choreo. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        InputSet._set_input(self, 'Timeframe', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((optional, string) The postal code for the area to retrieve electricity information for.)
        """
        InputSet._set_input(self, 'ZipCode', value)

class ElectricityUseResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ElectricityUse Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class ElectricityUseChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ElectricityUseResultSet(response, path)
