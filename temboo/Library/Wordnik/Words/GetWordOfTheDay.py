# -*- coding: utf-8 -*-

###############################################################################
#
# GetWordOfTheDay
# Retrieves the word of the day for specified dates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetWordOfTheDay(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWordOfTheDay Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Words/GetWordOfTheDay')


    def new_input_set(self):
        return GetWordOfTheDayInputSet()

    def _make_result_set(self, result, path):
        return GetWordOfTheDayResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWordOfTheDayChoreographyExecution(session, exec_id, path)

class GetWordOfTheDayInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWordOfTheDay
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, string) The date of the Word of the Day to retrieve, in yyyy-MM-dd format.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)

class GetWordOfTheDayResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWordOfTheDay Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetWordOfTheDayChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWordOfTheDayResultSet(response, path)
