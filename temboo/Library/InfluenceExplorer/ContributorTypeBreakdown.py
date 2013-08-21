# -*- coding: utf-8 -*-

###############################################################################
#
# ContributorTypeBreakdown
# Returns a breakdown, for a given candidate, of how much of the money raised came from individuals versus organizations (PACs).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ContributorTypeBreakdown(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ContributorTypeBreakdown Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/ContributorTypeBreakdown')


    def new_input_set(self):
        return ContributorTypeBreakdownInputSet()

    def _make_result_set(self, result, path):
        return ContributorTypeBreakdownResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ContributorTypeBreakdownChoreographyExecution(session, exec_id, path)

class ContributorTypeBreakdownInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ContributorTypeBreakdown
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, string) The ID for the Entity that you want to return information for. This ID can be retrieved by running the SearchByName Choreo.)
        """
        InputSet._set_input(self, 'EntityID', value)

class ContributorTypeBreakdownResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ContributorTypeBreakdown Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Influence Explorer.)
        """
        return self._output.get('Response', None)

class ContributorTypeBreakdownChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ContributorTypeBreakdownResultSet(response, path)
