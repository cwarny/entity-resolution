# -*- coding: utf-8 -*-

###############################################################################
#
# UserContacts
# Retrieves the information for contacts for the user assoicated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UserContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Contacts/UserContacts')


    def new_input_set(self):
        return UserContactsInputSet()

    def _make_result_set(self, result, path):
        return UserContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserContactsChoreographyExecution(session, exec_id, path)

class UserContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of contacts to retrieve. Defaults to 10. Can be between 1 and 200 contacts.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Search(self, value):
        """
        Set the value of the Search input for this Choreo. ((optional, string) Search term used to search the contacts.)
        """
        InputSet._set_input(self, 'Search', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((optional, string) Type of accounts to retrieve, in the form of a comma-separated list (e.g. "Facebook,Dwolla"))
        """
        InputSet._set_input(self, 'Types', value)

class UserContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class UserContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserContactsResultSet(response, path)
