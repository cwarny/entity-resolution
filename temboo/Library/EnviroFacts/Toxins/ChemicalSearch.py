# -*- coding: utf-8 -*-

###############################################################################
#
# ChemicalSearch
# Retrieves information about specific chemicals released by EPA-regulated facilities.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ChemicalSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ChemicalSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/Toxins/ChemicalSearch')


    def new_input_set(self):
        return ChemicalSearchInputSet()

    def _make_result_set(self, result, path):
        return ChemicalSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChemicalSearchChoreographyExecution(session, exec_id, path)

class ChemicalSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ChemicalSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ChemicalID(self, value):
        """
        Set the value of the ChemicalID input for this Choreo. ((required, string) EPA ID number of a chemical. Chemical IDs from a given facility can be found by first running the ChemActivityByFacility or ToxinReleaseByFacility Choreos.)
        """
        InputSet._set_input(self, 'ChemicalID', value)

class ChemicalSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ChemicalSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class ChemicalSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ChemicalSearchResultSet(response, path)
