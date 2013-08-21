# -*- coding: utf-8 -*-

###############################################################################
#
# FootprintLookup
# Retrieves the footprint for a specified place identifier.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FootprintLookup(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FootprintLookup Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/UnlockPlaces/FootprintLookup')


    def new_input_set(self):
        return FootprintLookupInputSet()

    def _make_result_set(self, result, path):
        return FootprintLookupResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FootprintLookupChoreographyExecution(session, exec_id, path)

class FootprintLookupInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FootprintLookup
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) The format of the place search results. One of xml, kml, json, georss or txt. Defaults to "xml".)
        """
        InputSet._set_input(self, 'Format', value)
    def set_Gazetteer(self, value):
        """
        Set the value of the Gazetteer input for this Choreo. ((optional, string) The place-name source to take locations from. The options are geonames, os, naturalearth or unlock which combines all the previous. Defaults to "unlock".)
        """
        InputSet._set_input(self, 'Gazetteer', value)
    def set_Identifier(self, value):
        """
        Set the value of the Identifier input for this Choreo. ((required, integer) The place identifier that you want to use for the search. Note that this identifier is returned in the <geometryRef> response element of other Unlock Places search Choreos.)
        """
        InputSet._set_input(self, 'Identifier', value)
    def set_MaxRows(self, value):
        """
        Set the value of the MaxRows input for this Choreo. ((optional, integer) The maximum number of results to return. Defaults to 20. Cannot exceed 1000.)
        """
        InputSet._set_input(self, 'MaxRows', value)
    def set_StartRow(self, value):
        """
        Set the value of the StartRow input for this Choreo. ((optional, integer) The row to start results display from. Defaults to 1.)
        """
        InputSet._set_input(self, 'StartRow', value)

class FootprintLookupResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FootprintLookup Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Unlock. Defaults to XML based on the format input parameter.)
        """
        return self._output.get('Response', None)

class FootprintLookupChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FootprintLookupResultSet(response, path)
