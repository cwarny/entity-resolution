# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Returns a list of all committees for a given chamber along with their subcommittees.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/Committee/GetList')


    def new_input_set(self):
        return GetListInputSet()

    def _make_result_set(self, result, path):
        return GetListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListChoreographyExecution(session, exec_id, path)

class GetListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Chamber(self, value):
        """
        Set the value of the Chamber input for this Choreo. ((required, string) A chamber to list committees for. Valid values are: House, Senate, or Joint.)
        """
        InputSet._set_input(self, 'Chamber', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
