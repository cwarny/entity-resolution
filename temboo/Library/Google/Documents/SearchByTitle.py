# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByTitle
# Retrieves information for a file with the title you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByTitle(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByTitle Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/SearchByTitle')


    def new_input_set(self):
        return SearchByTitleInputSet()

    def _make_result_set(self, result, path):
        return SearchByTitleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByTitleChoreographyExecution(session, exec_id, path)

class SearchByTitleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByTitle
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the document to search for. Enclose in quotation marks for an exact, non-case-sensitive match.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google account username.)
        """
        InputSet._set_input(self, 'Username', value)

class SearchByTitleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByTitle Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_EditMediaLink(self):
        """
        Retrieve the value for the "EditMediaLink" output from this Choreo execution. ((string) The 'resumable-edit-media' link of the document. This link is used when editing the content of an existing Google doc.)
        """
        return self._output.get('EditMediaLink', None)
    def get_EditMetaDataLink(self):
        """
        Retrieve the value for the "EditMetaDataLink" output from this Choreo execution. ((string) The 'edit' link of the document. This link is used when editing the metadata of an existing Google doc.)
        """
        return self._output.get('EditMetaDataLink', None)
    def get_ResourceID(self):
        """
        Retrieve the value for the "ResourceID" output from this Choreo execution. ((string) The document resource ID returned from Google.)
        """
        return self._output.get('ResourceID', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)

class SearchByTitleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByTitleResultSet(response, path)
