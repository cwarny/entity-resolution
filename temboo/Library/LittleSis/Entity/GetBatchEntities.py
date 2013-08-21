# -*- coding: utf-8 -*-

###############################################################################
#
# GetBatchEntities
# Retrieves the LittleSis record for a given Entity (person or organization) by its ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetBatchEntities(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBatchEntities Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetBatchEntities')


    def new_input_set(self):
        return GetBatchEntitiesInputSet()

    def _make_result_set(self, result, path):
        return GetBatchEntitiesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBatchEntitiesChoreographyExecution(session, exec_id, path)

class GetBatchEntitiesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBatchEntities
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Details(self, value):
        """
        Set the value of the Details input for this Choreo. ((optional, integer) Indicate 1 to retrieve detailed information associated with each record retrieved Otherwise, only a basic record will be returned.)
        """
        InputSet._set_input(self, 'Details', value)
    def set_EntityIDs(self, value):
        """
        Set the value of the EntityIDs input for this Choreo. ((required, string) A comma delimited string of the IDs of the Entities to retrieve.)
        """
        InputSet._set_input(self, 'EntityIDs', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetBatchEntitiesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBatchEntities Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetBatchEntitiesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBatchEntitiesResultSet(response, path)
