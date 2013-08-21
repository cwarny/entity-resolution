# -*- coding: utf-8 -*-

###############################################################################
#
# TopContributors
# Returns the top contributing organizations for a particular politician, ranked by total dollars given.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TopContributors(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopContributors Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/TopContributors')


    def new_input_set(self):
        return TopContributorsInputSet()

    def _make_result_set(self, result, path):
        return TopContributorsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopContributorsChoreographyExecution(session, exec_id, path)

class TopContributorsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopContributors
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

class TopContributorsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopContributors Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Influence Explorer.)
        """
        return self._output.get('Response', None)

class TopContributorsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopContributorsResultSet(response, path)
