# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteDatastream
# Deletes a datastream. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteDatastream(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteDatastream Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/DeleteDatastream')


    def new_input_set(self):
        return DeleteDatastreamInputSet()

    def _make_result_set(self, result, path):
        return DeleteDatastreamResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDatastreamChoreographyExecution(session, exec_id, path)

class DeleteDatastreamInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteDatastream
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((required, string) The ID of the datastream you wish to delete.)
        """
        InputSet._set_input(self, 'DatastreamID', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, string) The ID of the feed you would like to delete the datastream for.)
        """
        InputSet._set_input(self, 'FeedID', value)

class DeleteDatastreamResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteDatastream Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful deletion, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class DeleteDatastreamChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDatastreamResultSet(response, path)
