# -*- coding: utf-8 -*-

###############################################################################
#
# AddBookmark
# Adds a link bookmark to a Delicious account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddBookmark(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddBookmark Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Delicious/AddBookmark')


    def new_input_set(self):
        return AddBookmarkInputSet()

    def _make_result_set(self, result, path):
        return AddBookmarkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddBookmarkChoreographyExecution(session, exec_id, path)

class AddBookmarkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddBookmark
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((required, string) A description for the link to post.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Notes(self, value):
        """
        Set the value of the Notes input for this Choreo. ((optional, string) Descriptive notes for the posted link.)
        """
        InputSet._set_input(self, 'Notes', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Replace(self, value):
        """
        Set the value of the Replace input for this Choreo. ((optional, integer) Specify "1" to replace the post if the URL has already been posted. Set to "0" (don't replace) by default.)
        """
        InputSet._set_input(self, 'Replace', value)
    def set_Shared(self, value):
        """
        Set the value of the Shared input for this Choreo. ((optional, integer) Specify "1" to make the posted link private. Set to "0" (shared) by default.)
        """
        InputSet._set_input(self, 'Shared', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, string) Add keyword tags to the posted link. Separate multiple tags with commas.)
        """
        InputSet._set_input(self, 'Tags', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The URL for the link to post.)
        """
        InputSet._set_input(self, 'URL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        InputSet._set_input(self, 'Username', value)

class AddBookmarkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddBookmark Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class AddBookmarkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddBookmarkResultSet(response, path)
