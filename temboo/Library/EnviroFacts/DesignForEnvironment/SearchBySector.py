# -*- coding: utf-8 -*-

###############################################################################
#
# SearchBySector
# Looks up products by sector in the EPA Design for the Environment database
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchBySector(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchBySector Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/DesignForEnvironment/SearchBySector')


    def new_input_set(self):
        return SearchBySectorInputSet()

    def _make_result_set(self, result, path):
        return SearchBySectorResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchBySectorChoreographyExecution(session, exec_id, path)

class SearchBySectorInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchBySector
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((conditional, string) Specify either Industrial or Consumer to retrieve a list of products that fall into either category. If a specific SectorKeyword or SectorID is given, this input is ignored.)
        """
        InputSet._set_input(self, 'Category', value)
    def set_Operator(self, value):
        """
        Set the value of the Operator input for this Choreo. ((optional, string) Default output is "CONTAINING" and does not require an operator, but users can enter "<", " >", "!=", "BEGINNING", "=" for more customized searches.)
        """
        InputSet._set_input(self, 'Operator', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((conditional, string) Response can be returned in JSON or XML. Defaults to XML.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_RowEnd(self, value):
        """
        Set the value of the RowEnd input for this Choreo. ((optional, integer) Number 1 or greater indicates the ending row number of the results displayed. Default is 4999 when RowStart is 0. Up to 5000 entries are returned in the output.)
        """
        InputSet._set_input(self, 'RowEnd', value)
    def set_RowStart(self, value):
        """
        Set the value of the RowStart input for this Choreo. ((optional, integer) Indicates the starting row number of the results displayed. Default is 0.)
        """
        InputSet._set_input(self, 'RowStart', value)
    def set_SectorID(self, value):
        """
        Set the value of the SectorID input for this Choreo. ((conditional, integer) A number representing the unique identifier for the product's sector in the EnviroFacts database.)
        """
        InputSet._set_input(self, 'SectorID', value)
    def set_SectorKeyword(self, value):
        """
        Set the value of the SectorKeyword input for this Choreo. ((conditional, string) A keyword in the name of the sector to search for. If a specific SectorID is given, this input is ignored.)
        """
        InputSet._set_input(self, 'SectorKeyword', value)

class SearchBySectorResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchBySector Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Count(self):
        """
        Retrieve the value for the "Count" output from this Choreo execution. (The total number of records returned for any given search.)
        """
        return self._output.get('Count', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class SearchBySectorChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchBySectorResultSet(response, path)
