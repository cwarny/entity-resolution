# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteMultipleDatapoints
# Deletes multiple datapoints from a single datastream given a start date, end date, and/or duration.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteMultipleDatapoints(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteMultipleDatapoints Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/DeleteMultipleDatapoints')


    def new_input_set(self):
        return DeleteMultipleDatapointsInputSet()

    def _make_result_set(self, result, path):
        return DeleteMultipleDatapointsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteMultipleDatapointsChoreographyExecution(session, exec_id, path)

class DeleteMultipleDatapointsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteMultipleDatapoints
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((required, string) The ID of the datastream you would like to delete datapoints from.)
        """
        InputSet._set_input(self, 'DatastreamID', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((conditional, string) Specifies the duration of the deletion. Can be used with StartDate or EndDate. Ex: 5seconds, 10minutes, 6hours. See documentation for full description / examples.)
        """
        InputSet._set_input(self, 'Duration', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((conditional, date) Defines the end point of the deletion as a timestamp. Can be used with Duration. Ex: 2013-05-10T12:00:00Z.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, string) The ID of the feed you would like to delete datapoints from.)
        """
        InputSet._set_input(self, 'FeedID', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((conditional, date) Defines the starting point of the deletion as a timestamp. Can be used with Duration. Ex: 2013-05-10T00:00:00Z.)
        """
        InputSet._set_input(self, 'StartDate', value)

class DeleteMultipleDatapointsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteMultipleDatapoints Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponsStatusCode(self):
        """
        Retrieve the value for the "ResponsStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful datapoint range deletion, the code should be 200.)
        """
        return self._output.get('ResponsStatusCode', None)

class DeleteMultipleDatapointsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteMultipleDatapointsResultSet(response, path)
