# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateContact
# Updates an existing contact in your Constant Contact system when you supply a contact ID to the Choreo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateContact(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateContact Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/UpdateContact')


    def new_input_set(self):
        return UpdateContactInputSet()

    def _make_result_set(self, result, path):
        return UpdateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateContactChoreographyExecution(session, exec_id, path)

class UpdateContactInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateContact
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_UpdatedContactXML(self, value):
        """
        Set the value of the UpdatedContactXML input for this Choreo. ((required, xml) This input should be the updated XML returned from the ObtainContactInformation Choreo.)
        """
        InputSet._set_input(self, 'UpdatedContactXML', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Constant Contact.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ContactId(self, value):
        """
        Set the value of the ContactId input for this Choreo. ((required, integer) The id for the contact you want to update.)
        """
        InputSet._set_input(self, 'ContactId', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, integer) The ID for the list that you want to update)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Constant Contact password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) You Constant Contact username.)
        """
        InputSet._set_input(self, 'UserName', value)

class UpdateContactResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateContact Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Constant Contact. Note that a successful update returns no content.)
        """
        return self._output.get('Response', None)

class UpdateContactChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateContactResultSet(response, path)
