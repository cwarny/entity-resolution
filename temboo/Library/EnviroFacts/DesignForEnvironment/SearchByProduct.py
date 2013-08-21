# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByProduct
# Searches for products in the EPA Design for the Environment database.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByProduct(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByProduct Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/DesignForEnvironment/SearchByProduct')


    def new_input_set(self):
        return SearchByProductInputSet()

    def _make_result_set(self, result, path):
        return SearchByProductResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByProductChoreographyExecution(session, exec_id, path)

class SearchByProductInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByProduct
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CompanyKeyword(self, value):
        """
        Set the value of the CompanyKeyword input for this Choreo. ((conditional, string) A keyword in the name of the company to search for. If a specific ProductName or ProductID is specified, this input is ignored.)
        """
        InputSet._set_input(self, 'CompanyKeyword', value)
    def set_Operator(self, value):
        """
        Set the value of the Operator input for this Choreo. ((optional, string) Default output is "CONTAINING" and does not require an operator, but users can enter "<", " >", "!=", "BEGINNING", "=" for more customized searches.)
        """
        InputSet._set_input(self, 'Operator', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((conditional, integer) A number representing the unique identifier for a product in the EnviroFacts database.)
        """
        InputSet._set_input(self, 'ProductID', value)
    def set_ProductKeyword(self, value):
        """
        Set the value of the ProductKeyword input for this Choreo. ((conditional, string) A keyword in the name of the product to search for. If a specific ProductID is specified, this input is ignored.)
        """
        InputSet._set_input(self, 'ProductKeyword', value)
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

class SearchByProductResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByProduct Choreo.
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

class SearchByProductChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByProductResultSet(response, path)
