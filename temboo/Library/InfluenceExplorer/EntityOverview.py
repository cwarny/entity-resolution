# -*- coding: utf-8 -*-

###############################################################################
#
# EntityOverview
# Returns general information about a particular politician, individual, or organization with a given entity id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EntityOverview(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EntityOverview Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/EntityOverview')


    def new_input_set(self):
        return EntityOverviewInputSet()

    def _make_result_set(self, result, path):
        return EntityOverviewResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EntityOverviewChoreographyExecution(session, exec_id, path)

class EntityOverviewInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EntityOverview
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Cycle(self, value):
        """
        Set the value of the Cycle input for this Choreo. ((optional, date) Specify a yyyy-formatted election cycle. Example: 2012, or 2008|2012 to limit results between 2008 and 2012.)
        """
        InputSet._set_input(self, 'Cycle', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, string) The ID for the Entity that you want to return information for. This ID can be retrieved by running the SearchByName Choreo.)
        """
        InputSet._set_input(self, 'EntityID', value)

class EntityOverviewResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EntityOverview Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Influence Explorer.)
        """
        return self._output.get('Response', None)

class EntityOverviewChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EntityOverviewResultSet(response, path)
