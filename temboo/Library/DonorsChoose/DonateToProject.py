# -*- coding: utf-8 -*-

###############################################################################
#
# DonateToProject
# Makes a donation to a specified DonorsChoose.org project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DonateToProject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DonateToProject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DonorsChoose/DonateToProject')


    def new_input_set(self):
        return DonateToProjectInputSet()

    def _make_result_set(self, result, path):
        return DonateToProjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DonateToProjectChoreographyExecution(session, exec_id, path)

class DonateToProjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DonateToProject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The APIKey provided by DonorsChoose.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APIPassword(self, value):
        """
        Set the value of the APIPassword input for this Choreo. ((required, string) Your DonorsChoose.org API password. This is only required when performing transactions.)
        """
        InputSet._set_input(self, 'APIPassword', value)
    def set_Address1(self, value):
        """
        Set the value of the Address1 input for this Choreo. ((optional, string) Line one of the donor's address.)
        """
        InputSet._set_input(self, 'Address1', value)
    def set_Address2(self, value):
        """
        Set the value of the Address2 input for this Choreo. ((optional, string) Line two of the donor's address.)
        """
        InputSet._set_input(self, 'Address2', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, integer) The donation amount. Must be a whole number.)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) To wrap the response in a callback function, include the name in this input.)
        """
        InputSet._set_input(self, 'Callback', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((optional, string) The donor's city.)
        """
        InputSet._set_input(self, 'City', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address of the person who is making the donation.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_FirstName(self, value):
        """
        Set the value of the FirstName input for this Choreo. ((optional, string) The first name of the donor.)
        """
        InputSet._set_input(self, 'FirstName', value)
    def set_LastName(self, value):
        """
        Set the value of the LastName input for this Choreo. ((optional, string) The last name of the donor.)
        """
        InputSet._set_input(self, 'LastName', value)
    def set_ProposalId(self, value):
        """
        Set the value of the ProposalId input for this Choreo. ((required, integer) The ID of the project that will receive the donation.)
        """
        InputSet._set_input(self, 'ProposalId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Salutation(self, value):
        """
        Set the value of the Salutation input for this Choreo. ((optional, string) Hwo the donor wants to be acknowledged on donorschoose.org.)
        """
        InputSet._set_input(self, 'Salutation', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) The donor's state.)
        """
        InputSet._set_input(self, 'State', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, string) The donor's five-digit zip code.)
        """
        InputSet._set_input(self, 'Zip', value)

class DonateToProjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DonateToProject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from DonorsChoose.org.)
        """
        return self._output.get('Response', None)

class DonateToProjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DonateToProjectResultSet(response, path)
