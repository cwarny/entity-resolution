# -*- coding: utf-8 -*-

###############################################################################
#
# Categories
# Retrieves a list of all the Relationships possible among people and organizations in LittleSis.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Categories(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Categories Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/Categories')


    def new_input_set(self):
        return CategoriesInputSet()

    def _make_result_set(self, result, path):
        return CategoriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CategoriesChoreographyExecution(session, exec_id, path)

class CategoriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Categories
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from LittleSis.org. Acceptable inputs: xml or json. Defautls to xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class CategoriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Categories Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class CategoriesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CategoriesResultSet(response, path)
