# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllDocuments
# Lists all the documents associated with a user's Zoho Writer Account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListAllDocuments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllDocuments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zoho/Writer/ListAllDocuments')


    def new_input_set(self):
        return ListAllDocumentsInputSet()

    def _make_result_set(self, result, path):
        return ListAllDocumentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllDocumentsChoreographyExecution(session, exec_id, path)

class ListAllDocumentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllDocuments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Zoho)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Sets the number of documents to be listed.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_LoginID(self, value):
        """
        Set the value of the LoginID input for this Choreo. ((required, string) Your Zoho username (or login id))
        """
        InputSet._set_input(self, 'LoginID', value)
    def set_OrderBy(self, value):
        """
        Set the value of the OrderBy input for this Choreo. ((optional, string) Order documents by createdTime, lastModifiedTime or name.)
        """
        InputSet._set_input(self, 'OrderBy', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zoho password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Sorting order: asc or desc. Default sort order is set to ascending.)
        """
        InputSet._set_input(self, 'SortOrder', value)
    def set_StartFrom(self, value):
        """
        Set the value of the StartFrom input for this Choreo. ((optional, integer) Sets the initial document number from which the documents will be listed.)
        """
        InputSet._set_input(self, 'StartFrom', value)

class ListAllDocumentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllDocuments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Zoho. Corresponds to the ResponseFormat input. Defaults to XML.)
        """
        return self._output.get('Response', None)

class ListAllDocumentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllDocumentsResultSet(response, path)
