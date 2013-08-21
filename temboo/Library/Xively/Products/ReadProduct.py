# -*- coding: utf-8 -*-

###############################################################################
#
# ReadProduct
# Returns a JSON representation of a product. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReadProduct(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReadProduct Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Products/ReadProduct')


    def new_input_set(self):
        return ReadProductInputSet()

    def _make_result_set(self, result, path):
        return ReadProductResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReadProductChoreographyExecution(session, exec_id, path)

class ReadProductInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReadProduct
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The ID of the product you are trying to read information on.)
        """
        InputSet._set_input(self, 'ProductID', value)

class ReadProductResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReadProduct Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Xively.)
        """
        return self._output.get('Response', None)

class ReadProductChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReadProductResultSet(response, path)
