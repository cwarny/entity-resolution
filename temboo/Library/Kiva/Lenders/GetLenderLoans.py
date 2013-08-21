# -*- coding: utf-8 -*-

###############################################################################
#
# GetLenderLoans
# Returns loans belonging to a particular lender.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetLenderLoans(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLenderLoans Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Lenders/GetLenderLoans')


    def new_input_set(self):
        return GetLenderLoansInputSet()

    def _make_result_set(self, result, path):
        return GetLenderLoansResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLenderLoansChoreographyExecution(session, exec_id, path)

class GetLenderLoansInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLenderLoans
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_LenderName(self, value):
        """
        Set the value of the LenderName input for this Choreo. ((required, string) The lender name for which to return details.)
        """
        InputSet._set_input(self, 'LenderName', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page position of results to return. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) The order by which to sort results. Acceptable values: oldest, newest. Defaults to newest.)
        """
        InputSet._set_input(self, 'SortBy', value)

class GetLenderLoansResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLenderLoans Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class GetLenderLoansChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLenderLoansResultSet(response, path)
