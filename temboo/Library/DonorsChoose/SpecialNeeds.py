# -*- coding: utf-8 -*-

###############################################################################
#
# SpecialNeeds
# Returns results for projects within the Special Needs category.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SpecialNeeds(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SpecialNeeds Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DonorsChoose/SpecialNeeds')


    def new_input_set(self):
        return SpecialNeedsInputSet()

    def _make_result_set(self, result, path):
        return SpecialNeedsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SpecialNeedsChoreographyExecution(session, exec_id, path)

class SpecialNeedsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SpecialNeeds
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The APIKey provided by DonorsChoose.org. Defaults to the test  APIKey 'DONORSCHOOSE'.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((optional, integer) The number of the first row to return in the result. For example, if index=10, the results could show rows 10-59.)
        """
        InputSet._set_input(self, 'Index', value)
    def set_Max(self, value):
        """
        Set the value of the Max input for this Choreo. ((optional, integer) The max number of projects to return. Can return up to 50 rows at a time. Defaults to 10 when left empty.)
        """
        InputSet._set_input(self, 'Max', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ShowSynopsis(self, value):
        """
        Set the value of the ShowSynopsis input for this Choreo. ((optional, boolean) Set to 1 to show the synopsis for each project listing)
        """
        InputSet._set_input(self, 'ShowSynopsis', value)

class SpecialNeedsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SpecialNeeds Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from DonorsChoose.org)
        """
        return self._output.get('Response', None)

class SpecialNeedsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SpecialNeedsResultSet(response, path)
