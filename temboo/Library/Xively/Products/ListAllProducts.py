# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllProducts
# Returns a JSON representation of all products associated with the specified APIKey.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListAllProducts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllProducts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Products/ListAllProducts')


    def new_input_set(self):
        return ListAllProductsInputSet()

    def _make_result_set(self, result, path):
        return ListAllProductsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllProductsChoreographyExecution(session, exec_id, path)

class ListAllProductsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllProducts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)

class ListAllProductsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllProducts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Xively.)
        """
        return self._output.get('Response', None)

class ListAllProductsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllProductsResultSet(response, path)
