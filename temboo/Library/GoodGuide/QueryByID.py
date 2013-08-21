# -*- coding: utf-8 -*-

###############################################################################
#
# QueryByID
# Retrieves information about products based on a GoodGuide product ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class QueryByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the QueryByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GoodGuide/QueryByID')


    def new_input_set(self):
        return QueryByIDInputSet()

    def _make_result_set(self, result, path):
        return QueryByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryByIDChoreographyExecution(session, exec_id, path)

class QueryByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the QueryByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIFormat(self, value):
        """
        Set the value of the APIFormat input for this Choreo. ((optional, string) The response type supplied by GoodGuide. Default is simple. Other acceptable inputs are reference and badge.)
        """
        InputSet._set_input(self, 'APIFormat', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by GoodGuide.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) GoodGuide ID number of product.)
        """
        InputSet._set_input(self, 'ID', value)

class QueryByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the QueryByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from GoodGuide.)
        """
        return self._output.get('Response', None)

class QueryByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryByIDResultSet(response, path)
