# -*- coding: utf-8 -*-

###############################################################################
#
# CreatePeople
# Creates a new contact record in your Highrise CRM.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreatePeople(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreatePeople Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Highrise/CreatePeople')


    def new_input_set(self):
        return CreatePeopleInputSet()

    def _make_result_set(self, result, path):
        return CreatePeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreatePeopleChoreographyExecution(session, exec_id, path)

class CreatePeopleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreatePeople
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Highrise account name. This is the first part of the account's URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_Background(self, value):
        """
        Set the value of the Background input for this Choreo. ((optional, string) Corresponds to the background field in Highrise)
        """
        InputSet._set_input(self, 'Background', value)
    def set_CompanyName(self, value):
        """
        Set the value of the CompanyName input for this Choreo. ((optional, string) Corresponds to the company name field in Highrise.)
        """
        InputSet._set_input(self, 'CompanyName', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((optional, string) Corresponds to the email address field in Highrise.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((required, string) Corresponds to the first name field in Highrise.)
        """
        InputSet._set_input(self, 'FirstName', value)
    def set_HomePhone(self, value):
        """
        Set the value of the HomePhone input for this Choreo. ((optional, string) Corresponds to the home phone field in Highrise.)
        """
        InputSet._set_input(self, 'HomePhone', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) Corresponds to the last name field in Highrise.)
        """
        InputSet._set_input(self, 'LastName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Highrise account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) Corresponds to the title field in Highrise.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Highrise account username or API Key.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WorkPhone(self, value):
        """
        Set the value of the WorkPhone input for this Choreo. ((optional, string) Corresponds to the work phone field in Highrise.)
        """
        InputSet._set_input(self, 'WorkPhone', value)

class CreatePeopleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreatePeople Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Highrise.)
        """
        return self._output.get('Response', None)

class CreatePeopleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreatePeopleResultSet(response, path)
