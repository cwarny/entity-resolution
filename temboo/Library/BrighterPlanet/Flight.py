# -*- coding: utf-8 -*-

###############################################################################
#
# Flight
# Returns information about the carbon footprint of a passenger's air travel.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Flight(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Flight Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Flight')


    def new_input_set(self):
        return FlightInputSet()

    def _make_result_set(self, result, path):
        return FlightResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FlightChoreographyExecution(session, exec_id, path)

class FlightInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Flight
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Aircraft(self, value):
        """
        Set the value of the Aircraft input for this Choreo. ((optional, string) The ICAO code associated with the aircraft.)
        """
        InputSet._set_input(self, 'Aircraft', value)
    def set_Airline(self, value):
        """
        Set the value of the Airline input for this Choreo. ((optional, string) The name of the airline used (i.e. Continental, Delta, etc).)
        """
        InputSet._set_input(self, 'Airline', value)
    def set_Compliance(self, value):
        """
        Set the value of the Compliance input for this Choreo. ((optional, string) Comply with one or more protocols:  Greenhouse Gas Protocol Scope 3 (ghg_protocol_scope_3), ISO 14064-1 (iso), and The Climate Registry (tcr).)
        """
        InputSet._set_input(self, 'Compliance', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The date of the trip in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_DestinationAirport(self, value):
        """
        Set the value of the DestinationAirport input for this Choreo. ((optional, string) The airport code for the destination (i.e. LGA, JFK, etc.).)
        """
        InputSet._set_input(self, 'DestinationAirport', value)
    def set_DistanceClass(self, value):
        """
        Set the value of the DistanceClass input for this Choreo. ((optional, string) The distance class associated it the air travel (i.e. long haul, short haul).)
        """
        InputSet._set_input(self, 'DistanceClass', value)
    def set_DistanceEstimate(self, value):
        """
        Set the value of the DistanceEstimate input for this Choreo. ((optional, decimal) A estimate of the distance of the travel in kilometres.)
        """
        InputSet._set_input(self, 'DistanceEstimate', value)
    def set_Fuel(self, value):
        """
        Set the value of the Fuel input for this Choreo. ((optional, string) The type of fuel used in the aircraft (i.e. Aviation Gasoline, Biodiesel).)
        """
        InputSet._set_input(self, 'Fuel', value)
    def set_OriginAirport(self, value):
        """
        Set the value of the OriginAirport input for this Choreo. ((optional, string) The airport code for the origin (i.e. LGA, JFK, etc.).)
        """
        InputSet._set_input(self, 'OriginAirport', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Seats(self, value):
        """
        Set the value of the Seats input for this Choreo. ((optional, integer) The number of seats.)
        """
        InputSet._set_input(self, 'Seats', value)
    def set_Timeframe(self, value):
        """
        Set the value of the Timeframe input for this Choreo. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        InputSet._set_input(self, 'Timeframe', value)
    def set_Trips(self, value):
        """
        Set the value of the Trips input for this Choreo. ((optional, string) The number of trips to calculate information for.)
        """
        InputSet._set_input(self, 'Trips', value)

class FlightResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Flight Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class FlightChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FlightResultSet(response, path)
