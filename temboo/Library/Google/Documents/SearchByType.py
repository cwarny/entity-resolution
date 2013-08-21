# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByType
# Retrieves a list of all files of a MIME type you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByType(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByType Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/SearchByType')


    def new_input_set(self):
        return SearchByTypeInputSet()

    def _make_result_set(self, result, path):
        return SearchByTypeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByTypeChoreographyExecution(session, exec_id, path)

class SearchByTypeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByType
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((required, string) The MIME type of the files to list: word, excel, powerpoint, pdf, csv, rtf, html, css, xml, plaintext, zip, jpg, or png.)
        """
        InputSet._set_input(self, 'Type', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google account username.)
        """
        InputSet._set_input(self, 'Username', value)

class SearchByTypeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByType Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)

class SearchByTypeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByTypeResultSet(response, path)
