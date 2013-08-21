# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByNDC
# Returns a list of drugs in the DailyMed database associated with a given National Drug Code (NDC).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByNDC(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByNDC Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DailyMed/SearchByNDC')


    def new_input_set(self):
        return SearchByNDCInputSet()

    def _make_result_set(self, result, path):
        return SearchByNDCResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByNDCChoreographyExecution(session, exec_id, path)

class SearchByNDCInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByNDC
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_NDC(self, value):
        """
        Set the value of the NDC input for this Choreo. ((required, string) National Drug Code. This is a unique 10-digit numeric identifier assigned to each medication by the Food and Drug Administration (FDA).)
        """
        InputSet._set_input(self, 'NDC', value)
    def set_OutputFormat(self, value):
        """
        Set the value of the OutputFormat input for this Choreo. ((optional, string) Defaults to XML format when nothing is specified. Acceptable values: xml or json.)
        """
        InputSet._set_input(self, 'OutputFormat', value)

class SearchByNDCResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByNDC Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from DailyMed.)
        """
        return self._output.get('Response', None)

class SearchByNDCChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByNDCResultSet(response, path)
