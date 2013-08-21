# -*- coding: utf-8 -*-

###############################################################################
#
# GetSettledBatchList
# Returns data about a settled batch including: Batch ID, Settlement Time, and Settlement State, and Batch Statistics by payment type.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetSettledBatchList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSettledBatchList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/AuthorizeNet/TransactionDetailsAPI/GetSettledBatchList')


    def new_input_set(self):
        return GetSettledBatchListInputSet()

    def _make_result_set(self, result, path):
        return GetSettledBatchListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSettledBatchListChoreographyExecution(session, exec_id, path)

class GetSettledBatchListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSettledBatchList
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
    def set_FirstSettlementDate(self, value):
        """
        Set the value of the FirstSettlementDate input for this Choreo. ((required, date) Can be an epoch timestamp in milliseconds or formatted like 2010-12-01T00:00:00Z.)
        """
        InputSet._set_input(self, 'FirstSettlementDate', value)
    def set_IncludeStatistics(self, value):
        """
        Set the value of the IncludeStatistics input for this Choreo. ((optional, boolean) When 1 is specified, batch statistics by payment type are returned. Defaults to 1.)
        """
        InputSet._set_input(self, 'IncludeStatistics', value)
    def set_LastSettlementDate(self, value):
        """
        Set the value of the LastSettlementDate input for this Choreo. ((required, date) Can be an epoch timestamp in milliseconds or formatted like 2010-12-01T00:00:00Z.)
        """
        InputSet._set_input(self, 'LastSettlementDate', value)
    def set_TransactionKey(self, value):
        """
        Set the value of the TransactionKey input for this Choreo. ((required, string) The TransactionKey provided by Authorize.net when signing up for a developer account.)
        """
        InputSet._set_input(self, 'TransactionKey', value)

class GetSettledBatchListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSettledBatchList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Authorize.net.)
        """
        return self._output.get('Response', None)

class GetSettledBatchListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSettledBatchListResultSet(response, path)
