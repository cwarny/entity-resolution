# -*- coding: utf-8 -*-

###############################################################################
#
# GetSearchRecordsByPDC
# Retrieves records from your Zoho CRM account and searches by predefined columns.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetSearchRecordsByPDC(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSearchRecordsByPDC Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/GetSearchRecordsByPDC')


    def new_input_set(self):
        return GetSearchRecordsByPDCInputSet()

    def _make_result_set(self, result, path):
        return GetSearchRecordsByPDCResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSearchRecordsByPDCChoreographyExecution(session, exec_id, path)

class GetSearchRecordsByPDCInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSearchRecordsByPDC
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AuthenticationToken(self, value):
        """
        Set the value of the AuthenticationToken input for this Choreo. ((required, string) A valid authentication token. Permanent authentication tokens can be generated by the GenerateAuthToken Choreo.)
        """
        InputSet._set_input(self, 'AuthenticationToken', value)
    def set_FromIndex(self, value):
        """
        Set the value of the FromIndex input for this Choreo. ((optional, integer) The beginning index of the result set to return. Defaults to 1.)
        """
        InputSet._set_input(self, 'FromIndex', value)
    def set_Module(self, value):
        """
        Set the value of the Module input for this Choreo. ((required, string) The Zoho module you want to access. Defaults to 'Leads'.)
        """
        InputSet._set_input(self, 'Module', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid formats are: json and xml (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SearchColumn(self, value):
        """
        Set the value of the SearchColumn input for this Choreo. ((required, string) The column name you want to search (such as "email", the column names used in this method are in lowercase))
        """
        InputSet._set_input(self, 'SearchColumn', value)
    def set_SearchValue(self, value):
        """
        Set the value of the SearchValue input for this Choreo. ((required, string) Specify a search value for the column you're searching)
        """
        InputSet._set_input(self, 'SearchValue', value)
    def set_SelectColumns(self, value):
        """
        Set the value of the SelectColumns input for this Choreo. ((optional, string) The columns to return separated by commas (i.e. First Name,Last Name,Email). When left empty, only IDs are returned.)
        """
        InputSet._set_input(self, 'SelectColumns', value)
    def set_ToIndex(self, value):
        """
        Set the value of the ToIndex input for this Choreo. ((optional, integer) The ending index of the result set to return. Defaults to 20. Max is 200.)
        """
        InputSet._set_input(self, 'ToIndex', value)

class GetSearchRecordsByPDCResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSearchRecordsByPDC Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        return self._output.get('Response', None)

class GetSearchRecordsByPDCChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSearchRecordsByPDCResultSet(response, path)
