# -*- coding: utf-8 -*-

###############################################################################
#
# Stats
# Retrieves the account information for the user associated with the given authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Stats(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Stats Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Transactions/Stats')


    def new_input_set(self):
        return StatsInputSet()

    def _make_result_set(self, result, path):
        return StatsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StatsChoreographyExecution(session, exec_id, path)

class StatsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Stats
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) Ending date and time to for which to process transactions stats. Defaults to current date and time in UTC.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) Starting date and time to for which to process transactions stats. Defaults to 0300 of the current day in UTC.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((optional, string) Types of status to retrieve. Must be comma delimited. Options are TransactionsCount and TransactionsTotal. Defaults to include all stats.)
        """
        InputSet._set_input(self, 'Types', value)

class StatsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Stats Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class StatsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StatsResultSet(response, path)
