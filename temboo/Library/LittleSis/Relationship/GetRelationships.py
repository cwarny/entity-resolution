# -*- coding: utf-8 -*-

###############################################################################
#
# GetRelationships
# Retrieves information about a specific relationship documented in LittleSis according to its Relationship ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetRelationships(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRelationships Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Relationship/GetRelationships')


    def new_input_set(self):
        return GetRelationshipsInputSet()

    def _make_result_set(self, result, path):
        return GetRelationshipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRelationshipsChoreographyExecution(session, exec_id, path)

class GetRelationshipsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRelationships
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Details(self, value):
        """
        Set the value of the Details input for this Choreo. ((optional, string) Indicate "details" to retrieve detailed information associated with this record, including fields associated with the specific relationship type. Otherwise, only a basic record will be returned.)
        """
        InputSet._set_input(self, 'Details', value)
    def set_RelationshipID(self, value):
        """
        Set the value of the RelationshipID input for this Choreo. ((required, integer) The ID of the relationship record to be returned.)
        """
        InputSet._set_input(self, 'RelationshipID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetRelationshipsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRelationships Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetRelationshipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRelationshipsResultSet(response, path)
