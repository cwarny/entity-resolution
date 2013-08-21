# -*- coding: utf-8 -*-

###############################################################################
#
# Text
# Access Freebase topic and schema descriptions.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Text(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Text Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Freebase/Text')


    def new_input_set(self):
        return TextInputSet()

    def _make_result_set(self, result, path):
        return TextResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TextChoreographyExecution(session, exec_id, path)

class TextInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Text
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Freebase.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, boolean) Specify the retrieved results format.  Enter, html, plan, or raw. Default is set to: raw)
        """
        InputSet._set_input(self, 'Format', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) Enter the ID of the entity for which description information will be retrieved. IDs and MIDs can be obtained by running the Search Choreo in this bundle. Example input: /en/bob_dylan)
        """
        InputSet._set_input(self, 'ID', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) Specify the language in which the searches will be performed. Default is set to English: /lang/en)
        """
        InputSet._set_input(self, 'Language', value)
    def set_MaximumLength(self, value):
        """
        Set the value of the MaximumLength input for this Choreo. ((optional, integer) Enter the max number of characters to return with the rage of 0 - 4,294,967,295. Valid only for plan Format. Default is to: 200)
        """
        InputSet._set_input(self, 'MaximumLength', value)

class TextResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Text Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Freebase Text API in JSON.)
        """
        return self._output.get('Response', None)

class TextChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TextResultSet(response, path)
