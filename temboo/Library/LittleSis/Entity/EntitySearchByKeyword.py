# -*- coding: utf-8 -*-

###############################################################################
#
# EntitySearchByKeyword
# Retrieves Entities (people or organizations) in LittleSis that match a given keyword search.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EntitySearchByKeyword(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EntitySearchByKeyword Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/EntitySearchByKeyword')


    def new_input_set(self):
        return EntitySearchByKeywordInputSet()

    def _make_result_set(self, result, path):
        return EntitySearchByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EntitySearchByKeywordChoreographyExecution(session, exec_id, path)

class EntitySearchByKeywordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EntitySearchByKeyword
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from LittleSis.org.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Keywords(self, value):
        """
        Set the value of the Keywords input for this Choreo. ((required, string) Enter search text.)
        """
        InputSet._set_input(self, 'Keywords', value)
    def set_Number(self, value):
        """
        Set the value of the Number input for this Choreo. ((optional, integer) Specifies what number of results to show. Used in conjunction with Page parameter, a Number of 20 and a Page of 6 will show results 100-120.)
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
    def set_SearchAll(self, value):
        """
        Set the value of the SearchAll input for this Choreo. ((optional, integer) Enter 1 to search a record's description and summary fields. When not specified, only the name and aliases fields of each record will be searched.)
        """
        InputSet._set_input(self, 'SearchAll', value)
    def set_TypeIDs(self, value):
        """
        Set the value of the TypeIDs input for this Choreo. ((optional, string) You can specify a TypeIDs value to limit the search results to only those of a given type. Obtain all possible types and type ID's by first running the GetTypes Choreo.)
        """
        InputSet._set_input(self, 'TypeIDs', value)

class EntitySearchByKeywordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EntitySearchByKeyword Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class EntitySearchByKeywordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EntitySearchByKeywordResultSet(response, path)
