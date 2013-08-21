# -*- coding: utf-8 -*-

###############################################################################
#
# GetList
# Retrieves information about a List in LittleSis according to its ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/List/GetList')


    def new_input_set(self):
        return GetListInputSet()

    def _make_result_set(self, result, path):
        return GetListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListChoreographyExecution(session, exec_id, path)

class GetListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Entities(self, value):
        """
        Set the value of the Entities input for this Choreo. ((optional, string) Indicate "entities" to retrieve records of the entities that belong to the list. Otherwise, only a basic record about the list will be returned.)
        """
        InputSet._set_input(self, 'Entities', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, integer) The ID of the list record to be returned.)
        """
        InputSet._set_input(self, 'ListID', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((optional, integer) Specifies what number of results to show. Used in conjunction with Page parameter, a Nnumber of 20 and a Page of 6 will show results 100-120.)
        """
        InputSet._set_input(self, 'Number', value)
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
    def set_TypeID(self, value):
        """
        Set the value of the TypeID input for this Choreo. ((optional, integer) When the Entities parameter is activated, you can specify type IDs limiting the entities returned to those having the specified types (as a comma-delimited list).)
        """
        InputSet._set_input(self, 'TypeID', value)

class GetListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class GetListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListResultSet(response, path)
