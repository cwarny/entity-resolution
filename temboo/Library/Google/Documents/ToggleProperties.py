# -*- coding: utf-8 -*-

###############################################################################
#
# ToggleProperties
# Toggle settings for a document or file on or off, depending on its current state.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ToggleProperties(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ToggleProperties Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/ToggleProperties')


    def new_input_set(self):
        return TogglePropertiesInputSet()

    def _make_result_set(self, result, path):
        return TogglePropertiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TogglePropertiesChoreographyExecution(session, exec_id, path)

class TogglePropertiesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ToggleProperties
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the document with the properties you want to toggle. Enclose in quotation marks for an exact, non-case-sensitive match.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google account username.)
        """
        InputSet._set_input(self, 'Username', value)

class TogglePropertiesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ToggleProperties Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_EditLink(self):
        """
        Retrieve the value for the "EditLink" output from this Choreo execution. ((string) The edit link URL for the document, parsed from the Google response.)
        """
        return self._output.get('EditLink', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)

class TogglePropertiesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TogglePropertiesResultSet(response, path)
