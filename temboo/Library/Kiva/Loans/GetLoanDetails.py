# -*- coding: utf-8 -*-

###############################################################################
#
# GetLoanDetails
# Returns detailed information for multiple loans.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetLoanDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLoanDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Loans/GetLoanDetails')


    def new_input_set(self):
        return GetLoanDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetLoanDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLoanDetailsChoreographyExecution(session, exec_id, path)

class GetLoanDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLoanDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_LoanID(self, value):
        """
        Set the value of the LoanID input for this Choreo. ((required, string) A comma-delimited list of the loan IDs for which to get details. Maximum list items: 10.)
        """
        InputSet._set_input(self, 'LoanID', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)

class GetLoanDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLoanDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class GetLoanDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLoanDetailsResultSet(response, path)
