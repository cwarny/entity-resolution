# -*- coding: utf-8 -*-

###############################################################################
#
# CreateDiscussion
# Creates a new discussion for a particular folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateDiscussion(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateDiscussion Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Discussions/CreateDiscussion')


    def new_input_set(self):
        return CreateDiscussionInputSet()

    def _make_result_set(self, result, path):
        return CreateDiscussionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateDiscussionChoreographyExecution(session, exec_id, path)

class CreateDiscussionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateDiscussion
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The description of the discussion.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((required, string) The id of the folder to create a discussion for.)
        """
        InputSet._set_input(self, 'FolderID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the discussion.)
        """
        InputSet._set_input(self, 'Name', value)


class CreateDiscussionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateDiscussion Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class CreateDiscussionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateDiscussionResultSet(response, path)
