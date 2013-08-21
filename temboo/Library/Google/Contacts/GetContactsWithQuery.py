# -*- coding: utf-8 -*-

###############################################################################
#
# GetContactsWithQuery
# Retrieves the contact or contacts in that account that match a specified query term.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetContactsWithQuery(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetContactsWithQuery Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Contacts/GetContactsWithQuery')


    def new_input_set(self):
        return GetContactsWithQueryInputSet()

    def _make_result_set(self, result, path):
        return GetContactsWithQueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContactsWithQueryChoreographyExecution(session, exec_id, path)

class GetContactsWithQueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetContactsWithQuery
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((required, string) The OAuth client ID provided by Google when you register your application.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((required, string) The OAuth client secret provided by Google when you registered your application.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) The contact criteria to search for, such as name or email address.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class GetContactsWithQueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetContactsWithQuery Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        return self._output.get('AccessToken', None)
    def get_ContactID(self):
        """
        Retrieve the value for the "ContactID" output from this Choreo execution. ((string) The unique ID string for the retrieved contact. If more than one contact is retrieved by the request, only the first contact's ID is output.)
        """
        return self._output.get('ContactID', None)
    def get_Link(self):
        """
        Retrieve the value for the "Link" output from this Choreo execution. ((string) The unique edit link for the retrieved contact. If more than one contact is retrieved by the request, only the first contact's edit link is output.)
        """
        return self._output.get('Link', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)

class GetContactsWithQueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetContactsWithQueryResultSet(response, path)
