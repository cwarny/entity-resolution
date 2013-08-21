# -*- coding: utf-8 -*-

###############################################################################
#
# GetTransactionDetails
# Returns transaction details for a specified transaction ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTransactionDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTransactionDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/AuthorizeNet/TransactionDetailsAPI/GetTransactionDetails')


    def new_input_set(self):
        return GetTransactionDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetTransactionDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTransactionDetailsChoreographyExecution(session, exec_id, path)

class GetTransactionDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTransactionDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APILoginId(self, value):
        """
        Set the value of the APILoginId input for this Choreo. ((required, string) The API Login Id provided by Authorize.net when signing up for a developer account.)
        """
        InputSet._set_input(self, 'APILoginId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to api.authorize.net when running in production. Defaults to apitest.authorize.net for sandbox testing.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_TransactionId(self, value):
        """
        Set the value of the TransactionId input for this Choreo. ((required, integer) The id of the transaction that you want to retrieve information for.)
        """
        InputSet._set_input(self, 'TransactionId', value)
    def set_TransactionKey(self, value):
        """
        Set the value of the TransactionKey input for this Choreo. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        InputSet._set_input(self, 'TransactionKey', value)

class GetTransactionDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTransactionDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Authorize.net.)
        """
        return self._output.get('Response', None)

class GetTransactionDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTransactionDetailsResultSet(response, path)
