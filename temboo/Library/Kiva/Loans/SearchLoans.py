# -*- coding: utf-8 -*-

###############################################################################
#
# SearchLoans
# Returns a keyword search for loan listings by multiple criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchLoans(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchLoans Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Loans/SearchLoans')


    def new_input_set(self):
        return SearchLoansInputSet()

    def _make_result_set(self, result, path):
        return SearchLoansResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchLoansChoreographyExecution(session, exec_id, path)

class SearchLoansInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchLoans
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_CountryCode(self, value):
        """
        Set the value of the CountryCode input for this Choreo. ((optional, string) A list of two-character ISO codes of countries by which to filter results.)
        """
        InputSet._set_input(self, 'CountryCode', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) If supplied, results are filtered to loans with entrepreneurs of the specified gender. In the case of group loans, this matches against the predominate gender in the group: male or female.)
        """
        InputSet._set_input(self, 'Gender', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page position of results to return. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_Partner(self, value):
        """
        Set the value of the Partner input for this Choreo. ((optional, string) A list of partner IDs for which to filter results.)
        """
        InputSet._set_input(self, 'Partner', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A query string against which results should be returned.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_Region(self, value):
        """
        Set the value of the Region input for this Choreo. ((optional, string) List of two-letter codes corresponding to regions in which Kiva operates. If supplied, results are filtered to loans only from the specified regions: na, ca, sa, af, as, me, ee.)
        """
        InputSet._set_input(self, 'Region', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_Sector(self, value):
        """
        Set the value of the Sector input for this Choreo. ((optional, string) A list of business sectors for which to filter results.)
        """
        InputSet._set_input(self, 'Sector', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) The order by which to sort results. Acceptable values: popularity, loan_amount, oldest, expiration, newest, amount_remaining, repayment_term. Defaults to newest.)
        """
        InputSet._set_input(self, 'SortBy', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) The status of loans to return: fundraising, funded, in_repayment, paid, ended_with_loss.)
        """
        InputSet._set_input(self, 'Status', value)

class SearchLoansResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchLoans Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class SearchLoansChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchLoansResultSet(response, path)
