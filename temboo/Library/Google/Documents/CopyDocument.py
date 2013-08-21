# -*- coding: utf-8 -*-

###############################################################################
#
# CopyDocument
# Copies a document with the title you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CopyDocument(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CopyDocument Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/CopyDocument')


    def new_input_set(self):
        return CopyDocumentInputSet()

    def _make_result_set(self, result, path):
        return CopyDocumentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CopyDocumentChoreographyExecution(session, exec_id, path)

class CopyDocumentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CopyDocument
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_NewTitle(self, value):
        """
        Set the value of the NewTitle input for this Choreo. ((required, string) The title for the new, copied document.)
        """
        InputSet._set_input(self, 'NewTitle', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the document to copy. Enclose in quotation marks for an exact, non-case-sensitive match.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google account username.)
        """
        InputSet._set_input(self, 'Username', value)

class CopyDocumentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CopyDocument Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)

class CopyDocumentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CopyDocumentResultSet(response, path)
