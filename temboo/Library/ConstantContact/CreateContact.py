# -*- coding: utf-8 -*-

###############################################################################
#
# CreateContact
# Creates a contact in your Constant Contact account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateContact(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateContact Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/CreateContact')


    def new_input_set(self):
        return CreateContactInputSet()

    def _make_result_set(self, result, path):
        return CreateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateContactChoreographyExecution(session, exec_id, path)

class CreateContactInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateContact
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Constant Contact.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Addr1(self, value):
        """
        Set the value of the Addr1 input for this Choreo. ((optional, string) The first line of the contact's address.)
        """
        InputSet._set_input(self, 'Addr1', value)
    def set_Addr2(self, value):
        """
        Set the value of the Addr2 input for this Choreo. ((optional, string) The second line of the contact's address.)
        """
        InputSet._set_input(self, 'Addr2', value)
    def set_Addr3(self, value):
        """
        Set the value of the Addr3 input for this Choreo. ((optional, string) The third line of the contact's address.)
        """
        InputSet._set_input(self, 'Addr3', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The city portion of the contact's address.)
        """
        InputSet._set_input(self, 'City', value)
    def set_CompanyName(self, value):
        """
        Set the value of the CompanyName input for this Choreo. ((optional, string) The company name for the contact.)
        """
        InputSet._set_input(self, 'CompanyName', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) The country code associated with the contact's address.)
        """
        InputSet._set_input(self, 'CountryCode', value)
    def set_CountryName(self, value):
        """
        Set the value of the CountryName input for this Choreo. ((optional, string) Corresponds to the Country Name field in Constant Contact)
        """
        InputSet._set_input(self, 'CountryName', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address for the contact.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_EmailType(self, value):
        """
        Set the value of the EmailType input for this Choreo. ((optional, string) The email type that the contact should receive.)
        """
        InputSet._set_input(self, 'EmailType', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) The first name of the contact.)
        """
        InputSet._set_input(self, 'FirstName', value)
    def set_HomePhone(self, value):
        """
        Set the value of the HomePhone input for this Choreo. ((optional, string) The contact's home phone.)
        """
        InputSet._set_input(self, 'HomePhone', value)
    def set_JobTitle(self, value):
        """
        Set the value of the JobTitle input for this Choreo. ((optional, string) The contact's job title.)
        """
        InputSet._set_input(self, 'JobTitle', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The last name of the contact.)
        """
        InputSet._set_input(self, 'LastName', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, integer) The ID for the list that you want to add the contact to.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_MiddleName(self, value):
        """
        Set the value of the MiddleName input for this Choreo. ((optional, string) The middle name of the contact.)
        """
        InputSet._set_input(self, 'MiddleName', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) The full name of the contact.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Note(self, value):
        """
        Set the value of the Note input for this Choreo. ((optional, string) A note associated with the contact.)
        """
        InputSet._set_input(self, 'Note', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Constant Contact password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_PostalCode(self, value):
        """
        Set the value of the PostalCode input for this Choreo. ((optional, string) The postal code for the contact's address.)
        """
        InputSet._set_input(self, 'PostalCode', value)
    def set_StateCode(self, value):
        """
        Set the value of the StateCode input for this Choreo. ((optional, string) The state code for the contact's address.)
        """
        InputSet._set_input(self, 'StateCode', value)
    def set_StateName(self, value):
        """
        Set the value of the StateName input for this Choreo. ((optional, string) Corresponds to the State Name field in Constant Contact)
        """
        InputSet._set_input(self, 'StateName', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) The status of the contact (i.e. Active).)
        """
        InputSet._set_input(self, 'Status', value)
    def set_SubPostalCode(self, value):
        """
        Set the value of the SubPostalCode input for this Choreo. ((optional, string) The sub postal code for the contact.)
        """
        InputSet._set_input(self, 'SubPostalCode', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Your Constant Contact username.)
        """
        InputSet._set_input(self, 'UserName', value)
    def set_WorkPhone(self, value):
        """
        Set the value of the WorkPhone input for this Choreo. ((optional, string) The contact's work phone.)
        """
        InputSet._set_input(self, 'WorkPhone', value)

class CreateContactResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateContact Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Constant Contact.)
        """
        return self._output.get('Response', None)

class CreateContactChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateContactResultSet(response, path)
