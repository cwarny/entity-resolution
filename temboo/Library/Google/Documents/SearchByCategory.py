# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCategory
# Retrieves a list of all resources in a category you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByCategory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByCategory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/SearchByCategory')


    def new_input_set(self):
        return SearchByCategoryInputSet()

    def _make_result_set(self, result, path):
        return SearchByCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCategoryChoreographyExecution(session, exec_id, path)

class SearchByCategoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByCategory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((required, string) The category to list: "document", "spreadsheet", "presentation", "drawing", "folder", "starred", or "trashed". Combine multiple categories with "/".)
        """
        InputSet._set_input(self, 'Category', value)
    def set_MyDocs(self, value):
        """
        Set the value of the MyDocs input for this Choreo. ((optional, boolean) Enter "true" to return resources for the requesting user only. The default is "false" (returns all account resources).)
        """
        InputSet._set_input(self, 'MyDocs', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google account username.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_Viewed(self, value):
        """
        Set the value of the Viewed input for this Choreo. ((optional, boolean) Enter "true" to return only viewed resources for the specified category. The default is "false" (viewed and unviewed category resources).)
        """
        InputSet._set_input(self, 'Viewed', value)

class SearchByCategoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByCategory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)

class SearchByCategoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCategoryResultSet(response, path)
