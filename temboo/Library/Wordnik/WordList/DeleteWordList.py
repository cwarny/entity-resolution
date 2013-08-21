# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteWordList
# Deletes a given word list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteWordList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteWordList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/WordList/DeleteWordList')


    def new_input_set(self):
        return DeleteWordListInputSet()

    def _make_result_set(self, result, path):
        return DeleteWordListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteWordListChoreographyExecution(session, exec_id, path)

class DeleteWordListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteWordList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from Wordnik.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The Password of the Wordnik account.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The Username of the Wordnik account.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WordList(self, value):
        """
        Set the value of the WordList input for this Choreo. ((required, string) The perma-link of the WordLIst to delete.)
        """
        InputSet._set_input(self, 'WordList', value)

class DeleteWordListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteWordList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class DeleteWordListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteWordListResultSet(response, path)
