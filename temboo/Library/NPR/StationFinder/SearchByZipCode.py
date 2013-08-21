# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByZipCode
# Retrieves local NPR member stations based on zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByZipCode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByZipCode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByZipCode')


    def new_input_set(self):
        return SearchByZipCodeInputSet()

    def _make_result_set(self, result, path):
        return SearchByZipCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByZipCodeChoreographyExecution(session, exec_id, path)

class SearchByZipCodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByZipCode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, string) Enter a five-digit zip code.)
        """
        InputSet._set_input(self, 'Zip', value)

class SearchByZipCodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByZipCode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) )
        """
        return self._output.get('Response', None)

class SearchByZipCodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByZipCodeResultSet(response, path)
