# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteProduct
# Deletes a product batch. This will also delete all devices and feeds associated with the specified product batch.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteProduct(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteProduct Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Products/DeleteProduct')


    def new_input_set(self):
        return DeleteProductInputSet()

    def _make_result_set(self, result, path):
        return DeleteProductResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteProductChoreographyExecution(session, exec_id, path)

class DeleteProductInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteProduct
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ProductID(self, value):
        """
        Set the value of the ProductID input for this Choreo. ((required, string) The ID of the product you are trying to delete.)
        """
        InputSet._set_input(self, 'ProductID', value)

class DeleteProductResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteProduct Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful product deletion, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class DeleteProductChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteProductResultSet(response, path)
