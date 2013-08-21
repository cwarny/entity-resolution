# -*- coding: utf-8 -*-

###############################################################################
#
# GetContacts
# Retrieves your social contacts from multiple APIs in one API call.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/Social/GetContacts')


    def new_input_set(self):
        return GetContactsInputSet()

    def _make_result_set(self, result, path):
        return GetContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContactsChoreographyExecution(session, exec_id, path)

class GetContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((conditional, json) A list of credentials for the APIs you wish to access. See Choreo documentation for formatting examples.)
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) The Twitter screen name to retrieve followers for.)
        """
        InputSet._set_input(self, 'ScreenName', value)

class GetContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) Contains the merged results from the API responses.)
        """
        return self._output.get('Response', None)

class GetContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetContactsResultSet(response, path)
