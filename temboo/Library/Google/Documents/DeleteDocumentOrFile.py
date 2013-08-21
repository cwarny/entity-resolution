# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteDocumentOrFile
# Permanently deletes the document or file you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteDocumentOrFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteDocumentOrFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/DeleteDocumentOrFile')


    def new_input_set(self):
        return DeleteDocumentOrFileInputSet()

    def _make_result_set(self, result, path):
        return DeleteDocumentOrFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDocumentOrFileChoreographyExecution(session, exec_id, path)

class DeleteDocumentOrFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteDocumentOrFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ResourceID(self, value):
        """
        Set the value of the ResourceID input for this Choreo. ((required, string) The resource ID for the document or file to delete.)
        """
        InputSet._set_input(self, 'ResourceID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google account username.)
        """
        InputSet._set_input(self, 'Username', value)

class DeleteDocumentOrFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteDocumentOrFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (There is no XML response for delete requests.)
        """
        return self._output.get('Response', None)

class DeleteDocumentOrFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDocumentOrFileResultSet(response, path)
