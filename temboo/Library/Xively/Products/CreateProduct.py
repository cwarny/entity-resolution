# -*- coding: utf-8 -*-

###############################################################################
#
# CreateProduct
# Creates a new product batch.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateProduct(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateProduct Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Products/CreateProduct')


    def new_input_set(self):
        return CreateProductInputSet()

    def _make_result_set(self, result, path):
        return CreateProductResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateProductChoreographyExecution(session, exec_id, path)

class CreateProductInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateProduct
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CustomProduct(self, value):
        """
        Set the value of the CustomProduct input for this Choreo. ((optional, json) Optional custom configuration for creating your product in JSON. If you use this field the other optional parameters will be ignored. See Choreo description and Xively documentation for details.)
        """
        InputSet._set_input(self, 'CustomProduct', value)
    def set_Datastreams(self, value):
        """
        Set the value of the Datastreams input for this Choreo. ((optional, json) Default device datastream JSON array. Every newly created device in this product will have this default datastream. Ex: [{"id":"channel1"},{"id":"demo"}])
        """
        InputSet._set_input(self, 'Datastreams', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) Description of the product.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((conditional, string) Name of the product. Required unless using the CustomProduct JSON input.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Private(self, value):
        """
        Set the value of the Private input for this Choreo. ((optional, string) Default device feed privacy settings. Valid values: "true", "false" (default).)
        """
        InputSet._set_input(self, 'Private', value)

class CreateProductResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateProduct Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ProductID(self):
        """
        Retrieve the value for the "ProductID" output from this Choreo execution. ((string) The ProductID obtained from the ProductLocation returned by this Choreo.)
        """
        return self._output.get('ProductID', None)
    def get_ProductLocation(self):
        """
        Retrieve the value for the "ProductLocation" output from this Choreo execution. ((string) The URL of the newly created product.)
        """
        return self._output.get('ProductLocation', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful product creation, the code should be 201.)
        """
        return self._output.get('ResponseStatusCode', None)

class CreateProductChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateProductResultSet(response, path)
