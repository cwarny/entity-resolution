# -*- coding: utf-8 -*-

###############################################################################
#
# ListItems
# Lists files within a specified directory in your FilesAnywhere account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/ListItems')


    def new_input_set(self):
        return ListItemsInputSet()

    def _make_result_set(self, result, path):
        return ListItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListItemsChoreographyExecution(session, exec_id, path)

class ListItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((conditional, string) The API Key provided by FilesAnywhere. Required unless supplying a valid Token input.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_PageNum(self, value):
        """
        Set the value of the PageNum input for this Choreo. ((optional, integer) The page number to return. Can be used to page through large result sets. Defaults to 1.)
        """
        InputSet._set_input(self, 'PageNum', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results to return per page. Defaults to 10.)
        """
        InputSet._set_input(self, 'PageSize', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your FilesAnywhere password. Required unless supplying a valid Token input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The path to the folder that you want to list items for (i.e. \JOHNSMITH\MyFolder).)
        """
        InputSet._set_input(self, 'Path', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        InputSet._set_input(self, 'Token', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) Your FilesAnywhere username. Required unless supplying a valid Token input.)
        """
        InputSet._set_input(self, 'Username', value)

class ListItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FilesAnywhere.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        return self._output.get('Token', None)

class ListItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListItemsResultSet(response, path)
