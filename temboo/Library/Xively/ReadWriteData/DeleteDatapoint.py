# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteDatapoint
# Deletes a single existing datapoint for a specific timestamp.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteDatapoint(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteDatapoint Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/DeleteDatapoint')


    def new_input_set(self):
        return DeleteDatapointInputSet()

    def _make_result_set(self, result, path):
        return DeleteDatapointResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteDatapointChoreographyExecution(session, exec_id, path)

class DeleteDatapointInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteDatapoint
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((required, string) The ID of the datastream you would like to delete the datapoint for.)
        """
        InputSet._set_input(self, 'DatastreamID', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, string) The ID of the feed you would like to delete the datapoint for.)
        """
        InputSet._set_input(self, 'FeedID', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((required, date) Timestamp of datapoint value to delete. Must be in ISO 8601 format, and can include up to 6 decimal places of resolution (in seconds), default zone is UTC.  Ex: 2013-05-07T00:00:00.123456Z.)
        """
        InputSet._set_input(self, 'Timestamp', value)

class DeleteDatapointResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteDatapoint Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponsStatusCode(self):
        """
        Retrieve the value for the "ResponsStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful datapoint deletion, the code should be 200.)
        """
        return self._output.get('ResponsStatusCode', None)

class DeleteDatapointChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteDatapointResultSet(response, path)
