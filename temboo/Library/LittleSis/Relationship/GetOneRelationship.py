# -*- coding: utf-8 -*-

###############################################################################
#
# GetOneRelationship
# Retrieves information about any known relationship between two entities in LittleSis according their IDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetOneRelationship(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetOneRelationship Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Relationship/GetOneRelationship')


    def new_input_set(self):
        return GetOneRelationshipInputSet()

    def _make_result_set(self, result, path):
        return GetOneRelationshipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetOneRelationshipChoreographyExecution(session, exec_id, path)

class GetOneRelationshipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetOneRelationship
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_EntityIDs(self, value):
        """
        Set the value of the EntityIDs input for this Choreo. ((required, string) The IDs of the entities between which you want to find relationships. Format is a semicolon delimited string (e.g. 1026;1))
        """
        InputSet._set_input(self, 'EntityIDs', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetOneRelationshipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetOneRelationship Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetOneRelationshipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetOneRelationshipResultSet(response, path)
