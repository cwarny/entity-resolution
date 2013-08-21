# -*- coding: utf-8 -*-

###############################################################################
#
# RailTrip
# Returns information about the carbon footprint of a passenger's train travel.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RailTrip(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RailTrip Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/RailTrip')


    def new_input_set(self):
        return RailTripInputSet()

    def _make_result_set(self, result, path):
        return RailTripResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RailTripChoreographyExecution(session, exec_id, path)

class RailTripInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RailTrip
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Compliance(self, value):
        """
        Set the value of the Compliance input for this Choreo. ((optional, string) Comply with one or more protocols:  Greenhouse Gas Protocol Scope 3 (ghg_protocol_scope_3), ISO 14064-1 (iso), and The Climate Registry (tcr).)
        """
        InputSet._set_input(self, 'Compliance', value)
    def set_Country(self, value):
        """
        Set the value of the Country input for this Choreo. ((optional, string) A country code associated with the rail trip (in ISO 3166 format).)
        """
        InputSet._set_input(self, 'Country', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The date of the rail trip in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Destination(self, value):
        """
        Set the value of the Destination input for this Choreo. ((optional, string) The destination of the rail trip.)
        """
        InputSet._set_input(self, 'Destination', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, decimal) The distance of the rail trip in kilometres.)
        """
        InputSet._set_input(self, 'Distance', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((optional, decimal) The duration of the rail trip in seconds.)
        """
        InputSet._set_input(self, 'Duration', value)
    def set_Origin(self, value):
        """
        Set the value of the Origin input for this Choreo. ((optional, string) The origin of the rail trip.)
        """
        InputSet._set_input(self, 'Origin', value)
    def set_RailClass(self, value):
        """
        Set the value of the RailClass input for this Choreo. ((optional, string) The rail class associated with the rail trip (i.e. commuter, heavy, highspeed, intercity, light).)
        """
        InputSet._set_input(self, 'RailClass', value)
    def set_RailCompany(self, value):
        """
        Set the value of the RailCompany input for this Choreo. ((optional, string) The rail company associated with the rail trip (i.e. AMTRAK).)
        """
        InputSet._set_input(self, 'RailCompany', value)
    def set_RailTraction(self, value):
        """
        Set the value of the RailTraction input for this Choreo. ((optional, string) The rail traction associated with the rail trip (i.e. diesel, electric).)
        """
        InputSet._set_input(self, 'RailTraction', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Timeframe(self, value):
        """
        Set the value of the Timeframe input for this Choreo. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        InputSet._set_input(self, 'Timeframe', value)

class RailTripResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RailTrip Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class RailTripChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RailTripResultSet(response, path)
