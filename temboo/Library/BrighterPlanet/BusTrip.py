# -*- coding: utf-8 -*-

###############################################################################
#
# BusTrip
# Returns information about the carbon footprint of passenger bus travel.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class BusTrip(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the BusTrip Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/BusTrip')


    def new_input_set(self):
        return BusTripInputSet()

    def _make_result_set(self, result, path):
        return BusTripResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BusTripChoreographyExecution(session, exec_id, path)

class BusTripInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the BusTrip
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_BusClass(self, value):
        """
        Set the value of the BusClass input for this Choreo. ((optional, string) The bus class for the trip (i.e. city transit, regional coach).)
        """
        InputSet._set_input(self, 'BusClass', value)
    def set_Compliance(self, value):
        """
        Set the value of the Compliance input for this Choreo. ((optional, string) Comply with one or more protocols: Greenhouse Gas Protocol Scope 3 (ghg_protocol_scope_3), and ISO 14064-1 (iso), and The Climate Registry (tcr).)
        """
        InputSet._set_input(self, 'Compliance', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, date) The date of the bus trip in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, decimal) The distance of the bus trip in kilometres.)
        """
        InputSet._set_input(self, 'Distance', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((optional, decimal) The duration of the bus trip in seconds.)
        """
        InputSet._set_input(self, 'Duration', value)
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

class BusTripResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the BusTrip Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class BusTripChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BusTripResultSet(response, path)
