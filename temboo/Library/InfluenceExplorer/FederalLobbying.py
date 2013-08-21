# -*- coding: utf-8 -*-

###############################################################################
#
# FederalLobbying
# Obtain detailed lobbying information.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FederalLobbying(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FederalLobbying Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/FederalLobbying')


    def new_input_set(self):
        return FederalLobbyingInputSet()

    def _make_result_set(self, result, path):
        return FederalLobbyingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FederalLobbyingChoreographyExecution(session, exec_id, path)

class FederalLobbyingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FederalLobbying
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((optional, string) Enter the amount of dollars spent on lobbying.  Valid formats include: 500 (exactly $500); >|500 (greater than, or equal to 500); <|500 (less than or equal to 500).)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_ClientParentOrganization(self, value):
        """
        Set the value of the ClientParentOrganization input for this Choreo. ((optional, string) Specify a full-text search of a client's parent organizationfor.)
        """
        InputSet._set_input(self, 'ClientParentOrganization', value)
    def set_ClientSearch(self, value):
        """
        Set the value of the ClientSearch input for this Choreo. ((optional, string) Enter the name of the client for whom this lobbyist is working. This parameter executes a full-text search.)
        """
        InputSet._set_input(self, 'ClientSearch', value)
    def set_FilingType(self, value):
        """
        Set the value of the FilingType input for this Choreo. ((optional, string) Specify the type of filing as identified by CRP.  Example: n, for non-self filer parent.  For more info, go here: http://data.influenceexplorer.com/api/lobbying/)
        """
        InputSet._set_input(self, 'FilingType', value)
    def set_LobbyistSearch(self, value):
        """
        Set the value of the LobbyistSearch input for this Choreo. ((optional, string) Specify a full-text search of a lobbyist's name.)
        """
        InputSet._set_input(self, 'LobbyistSearch', value)
    def set_RegistrantSearch(self, value):
        """
        Set the value of the RegistrantSearch input for this Choreo. ((optional, string) Specify a full-text search of an organization or a person, who is fling the lobbyist registration.)
        """
        InputSet._set_input(self, 'RegistrantSearch', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Indicates the desired format for the response. Accepted values are: json (the default), csv, and xls. Note when specifying xls, restults are returned as Base64 encoded data.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((optional, string) Enter the report ID given by the Senate Office of Public Records.)
        """
        InputSet._set_input(self, 'TransactionID', value)
    def set_TransactionType(self, value):
        """
        Set the value of the TransactionType input for this Choreo. ((optional, string) Enter the type of filing as reported by the Senate Office of Public Records. See here for additional info: http://assets.transparencydata.org.s3.amazonaws.com/docs/transaction_types-20100402.csv)
        """
        InputSet._set_input(self, 'TransactionType', value)
    def set_YearFiled(self, value):
        """
        Set the value of the YearFiled input for this Choreo. ((optional, string) Specify the year in which a registration was filed. Use the following format: yyyy. Example: 2011. Logical OR is also possible by using the | (pipe) symbol.  Example: 2008|2012.)
        """
        InputSet._set_input(self, 'YearFiled', value)

class FederalLobbyingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FederalLobbying Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Influence Explorer. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class FederalLobbyingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FederalLobbyingResultSet(response, path)
