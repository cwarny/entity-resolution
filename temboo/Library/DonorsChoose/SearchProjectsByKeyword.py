# -*- coding: utf-8 -*-

###############################################################################
#
# SearchProjectsByKeyword
# Allows you to projects subjects by keyword.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchProjectsByKeyword(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchProjectsByKeyword Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DonorsChoose/SearchProjectsByKeyword')


    def new_input_set(self):
        return SearchProjectsByKeywordInputSet()

    def _make_result_set(self, result, path):
        return SearchProjectsByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchProjectsByKeywordChoreographyExecution(session, exec_id, path)

class SearchProjectsByKeywordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchProjectsByKeyword
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey provided by DonorsChoose.org. Defaults to the test  APIKey 'DONORSCHOOSE'.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Keyword(self, value):
        """
        Set the value of the Keyword input for this Choreo. ((required, string) Allows you to search for subjects using keyword search)
        """
        InputSet._set_input(self, 'Keyword', value)
    def set_Max(self, value):
        """
        Set the value of the Max input for this Choreo. ((optional, integer) The max number of projects to return. Can return up to 50 rows at a time. Defaults to 10 when left empty.)
        """
        InputSet._set_input(self, 'Max', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class SearchProjectsByKeywordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchProjectsByKeyword Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from DonorsChoose.org)
        """
        return self._output.get('Response', None)

class SearchProjectsByKeywordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchProjectsByKeywordResultSet(response, path)
