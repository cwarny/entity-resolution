# -*- coding: utf-8 -*-

###############################################################################
#
# DeletePeople
# Deletes a specified contact from your Highrise CRM.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeletePeople(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeletePeople Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Highrise/DeletePeople')


    def new_input_set(self):
        return DeletePeopleInputSet()

    def _make_result_set(self, result, path):
        return DeletePeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePeopleChoreographyExecution(session, exec_id, path)

class DeletePeopleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeletePeople
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Highrise account name. This is the first part of the account's URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_ContactID(self, value):
        """
        Set the value of the ContactID input for this Choreo. ((required, string) The ID number of the contact you want to delete. This is used to contruct the URL for the request.)
        """
        InputSet._set_input(self, 'ContactID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Highrise account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Highrise account username or API Key.)
        """
        InputSet._set_input(self, 'Username', value)

class DeletePeopleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeletePeople Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Highrise. The delete people API method returns no XML, so this variable will contain no data.)
        """
        return self._output.get('Response', None)

class DeletePeopleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeletePeopleResultSet(response, path)
