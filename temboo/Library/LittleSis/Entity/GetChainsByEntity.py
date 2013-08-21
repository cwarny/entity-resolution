# -*- coding: utf-8 -*-

###############################################################################
#
# GetChainsByEntity
# Retrieves a chain of connections between two Entities (person or organization) in LittleSis.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetChainsByEntity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetChainsByEntity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetChainsByEntity')


    def new_input_set(self):
        return GetChainsByEntityInputSet()

    def _make_result_set(self, result, path):
        return GetChainsByEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetChainsByEntityChoreographyExecution(session, exec_id, path)

class GetChainsByEntityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetChainsByEntity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((optional, integer) Limit the relationships to specific categories by specifying the category number.)
        """
        InputSet._set_input(self, 'CategoryID', value)
    def set_EntityIDs(self, value):
        """
        Set the value of the EntityIDs input for this Choreo. ((required, integer) The EntityIDs of the two entities for which a relationship chain is to be returned, separated by a semicolon (e.g. 14629;2 ).)
        """
        InputSet._set_input(self, 'EntityIDs', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, string) Specifies which of the found chain to expand in detail. Default is 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetChainsByEntityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetChainsByEntity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetChainsByEntityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetChainsByEntityResultSet(response, path)
