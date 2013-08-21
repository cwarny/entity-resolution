# -*- coding: utf-8 -*-

###############################################################################
#
# GetWordsInWordList
# Retrievs the words in a word list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetWordsInWordList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWordsInWordList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/WordList/GetWordsInWordList')


    def new_input_set(self):
        return GetWordsInWordListInputSet()

    def _make_result_set(self, result, path):
        return GetWordsInWordListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWordsInWordListChoreographyExecution(session, exec_id, path)

class GetWordsInWordListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWordsInWordList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from Wordnik.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limits teh number of results returned. Defaults to 100.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The Password of the Wordnik user account.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Number of results to skip. Defaults to 0.)
        """
        InputSet._set_input(self, 'Skip', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Sorts the results by either alpha (alphabetically) or createDate (the date created). Defaults to createDate.)
        """
        InputSet._set_input(self, 'SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) The direction to sort results by either asc (ascending) or desc (descending). Defaults to desc.)
        """
        InputSet._set_input(self, 'SortOrder', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The Username of the Wordnik user.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WordList(self, value):
        """
        Set the value of the WordList input for this Choreo. ((required, string) The perma-link for the Word List to retrieve.)
        """
        InputSet._set_input(self, 'WordList', value)

class GetWordsInWordListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWordsInWordList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetWordsInWordListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWordsInWordListResultSet(response, path)
