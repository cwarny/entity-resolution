# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteContact
# Deletes a specified contact.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteContact(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteContact Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Contacts/DeleteContact')


    def new_input_set(self):
        return DeleteContactInputSet()

    def _make_result_set(self, result, path):
        return DeleteContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteContactChoreographyExecution(session, exec_id, path)

class DeleteContactInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteContact
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
    def set_ContactID(self, value):
        """
        Set the value of the ContactID input for this Choreo. ((required, string) The unique ID string for the contact you want to delete.)
        """
        InputSet._set_input(self, 'ContactID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((required, string) The refresh token retrieved in the last step of the OAuth process. This is used when an access token is expired or not provided.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class DeleteContactResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteContact Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((optional, string) The access token retrieved in the last step of the OAuth process. Access tokens that are expired will be refreshed and returned in the Choreo output.)
        """
        return self._output.get('AccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google. No content is returned for a successful delete request.)
        """
        return self._output.get('Response', None)

class DeleteContactChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteContactResultSet(response, path)
