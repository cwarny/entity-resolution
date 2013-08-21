# -*- coding: utf-8 -*-

###############################################################################
#
# SearchTeams
# Returns a keyword search of all lending teams using multiple criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchTeams(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchTeams Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Teams/SearchTeams')


    def new_input_set(self):
        return SearchTeamsInputSet()

    def _make_result_set(self, result, path):
        return SearchTeamsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchTeamsChoreographyExecution(session, exec_id, path)

class SearchTeamsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchTeams
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_MembershipType(self, value):
        """
        Set the value of the MembershipType input for this Choreo. ((optional, string) If supplied, only teams with the specified membership policy are returned: open or closed.)
        """
        InputSet._set_input(self, 'MembershipType', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page position of results to return. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A query string against which results should be returned.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) The order by which to sort results. Acceptable values: popularity, loan_amount, oldest, expiration, newest, amount_remaining, repayment_term. Defaults to newest.)
        """
        InputSet._set_input(self, 'SortBy', value)

class SearchTeamsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchTeams Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class SearchTeamsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchTeamsResultSet(response, path)
