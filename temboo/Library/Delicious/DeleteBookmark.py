# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteBookmark
# Deletes a bookmarked link from a Delicious account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteBookmark(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteBookmark Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Delicious/DeleteBookmark')


    def new_input_set(self):
        return DeleteBookmarkInputSet()

    def _make_result_set(self, result, path):
        return DeleteBookmarkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteBookmarkChoreographyExecution(session, exec_id, path)

class DeleteBookmarkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteBookmark
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The URL for the posted link to delete.)
        """
        InputSet._set_input(self, 'URL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        InputSet._set_input(self, 'Username', value)

class DeleteBookmarkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteBookmark Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class DeleteBookmarkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteBookmarkResultSet(response, path)
