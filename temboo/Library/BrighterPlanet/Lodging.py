# -*- coding: utf-8 -*-

###############################################################################
#
# Lodging
# Returns the the footprint of a guest's hotel stay.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Lodging(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Lodging Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Lodging')


    def new_input_set(self):
        return LodgingInputSet()

    def _make_result_set(self, result, path):
        return LodgingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LodgingChoreographyExecution(session, exec_id, path)

class LodgingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Lodging
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ACCoverage(self, value):
        """
        Set the value of the ACCoverage input for this Choreo. ((optional, decimal) A numeric value representing the AC coverage of the lodging establishment.)
        """
        InputSet._set_input(self, 'ACCoverage', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The city of the establishment.)
        """
        InputSet._set_input(self, 'City', value)
    def set_Compliance(self, value):
        """
        Set the value of the Compliance input for this Choreo. ((optional, string) Comply with one or more protocols:  Greenhouse Gas Protocol Scope 3 (ghg_protocol_scope_3), ISO 14064-1 (iso), and The Climate Registry (tcr).)
        """
        InputSet._set_input(self, 'Compliance', value)
    def set_ConstructionYear(self, value):
        """
        Set the value of the ConstructionYear input for this Choreo. ((optional, integer) The year that the establishment was constructed.)
        """
        InputSet._set_input(self, 'ConstructionYear', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) The ISO 3166 country code associated with the establishment.)
        """
        InputSet._set_input(self, 'Country', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The date of the stay at the establishment in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((optional, integer) The amount of time spent at the establishment in seconds.)
        """
        InputSet._set_input(self, 'Duration', value)
    def set_Floors(self, value):
        """
        Set the value of the Floors input for this Choreo. ((optional, integer) The number of floors at the establishment.)
        """
        InputSet._set_input(self, 'Floors', value)
    def set_HotTubs(self, value):
        """
        Set the value of the HotTubs input for this Choreo. ((optional, integer) The number of hot tubs that the establishment has.)
        """
        InputSet._set_input(self, 'HotTubs', value)
    def set_IndoorPools(self, value):
        """
        Set the value of the IndoorPools input for this Choreo. ((optional, integer) The number of indoor pools that the establishment has.)
        """
        InputSet._set_input(self, 'IndoorPools', value)
    def set_LodgingClass(self, value):
        """
        Set the value of the LodgingClass input for this Choreo. ((optional, string) The lodging class (i.e. Hotel, Inn, or Motel).)
        """
        InputSet._set_input(self, 'LodgingClass', value)
    def set_OutdoorPools(self, value):
        """
        Set the value of the OutdoorPools input for this Choreo. ((optional, integer) The number of outdoor pools that the establishment has.)
        """
        InputSet._set_input(self, 'OutdoorPools', value)
    def set_PropertyRooms(self, value):
        """
        Set the value of the PropertyRooms input for this Choreo. ((optional, integer) The number of rooms on the property.)
        """
        InputSet._set_input(self, 'PropertyRooms', value)
    def set_Property(self, value):
        """
        Set the value of the Property input for this Choreo. ((optional, integer) A property id (or northstart_id) associated with the establishment.)
        """
        InputSet._set_input(self, 'Property', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Rooms(self, value):
        """
        Set the value of the Rooms input for this Choreo. ((optional, integer) The number of rooms.)
        """
        InputSet._set_input(self, 'Rooms', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The postal abbreviation for the state that the establishment is in.)
        """
        InputSet._set_input(self, 'State', value)
    def set_Timeframe(self, value):
        """
        Set the value of the Timeframe input for this Choreo. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        InputSet._set_input(self, 'Timeframe', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((optional, string) The postal code associated with the establishment.)
        """
        InputSet._set_input(self, 'ZipCode', value)

class LodgingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Lodging Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class LodgingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LodgingResultSet(response, path)
