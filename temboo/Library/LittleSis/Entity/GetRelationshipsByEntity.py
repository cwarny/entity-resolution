# -*- coding: utf-8 -*-

###############################################################################
#
# GetRelationshipsByEntity
# Retrieves a list of Relationships (to a person or to an organization) of a given Entity known in LittleSis.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetRelationshipsByEntity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRelationshipsByEntity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/GetRelationshipsByEntity')


    def new_input_set(self):
        return GetRelationshipsByEntityInputSet()

    def _make_result_set(self, result, path):
        return GetRelationshipsByEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRelationshipsByEntityChoreographyExecution(session, exec_id, path)

class GetRelationshipsByEntityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRelationshipsByEntity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CategoryIDs(self, value):
        """
        Set the value of the CategoryIDs input for this Choreo. ((optional, string) Comma delimited list of category IDs the resulting Relationships must have.)
        """
        InputSet._set_input(self, 'CategoryIDs', value)
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((required, integer) The ID of the person or organization fro which a record is to be returned.)
        """
        InputSet._set_input(self, 'EntityID', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((optional, integer) Specifies what number of results to show. Used in conjunction with Page parameter, a Number of 20 and a Page of 6 will show results 100-120.)
        """
        InputSet._set_input(self, 'Number', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, integer) Specifies what order the given entity must have in the relationship.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Specifies what page of results to show. Used in conjunction with Number parameter. A number of 20 and a Page of 6 will show results 100-120.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Format of the response returned by LittleSis.org. Acceptable inputs: xml or json. Defaults to xml)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetRelationshipsByEntityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRelationshipsByEntity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetRelationshipsByEntityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRelationshipsByEntityResultSet(response, path)
