# -*- coding: utf-8 -*-

###############################################################################
#
# EntityTypes
# Retrieves a list of the types of Entities (people or organizations) in LittleSis, along with TypeIDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EntityTypes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EntityTypes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LittleSis/Entity/EntityTypes')


    def new_input_set(self):
        return EntityTypesInputSet()

    def _make_result_set(self, result, path):
        return EntityTypesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EntityTypesChoreographyExecution(session, exec_id, path)

class EntityTypesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EntityTypes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from LittleSis.org. Acceptable inputs: xml or json. Defautls to xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class EntityTypesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EntityTypes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LittleSis.org.)
        """
        return self._output.get('Response', None)

class EntityTypesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EntityTypesResultSet(response, path)
