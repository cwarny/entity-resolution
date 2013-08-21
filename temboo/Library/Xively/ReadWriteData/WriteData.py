# -*- coding: utf-8 -*-

###############################################################################
#
# WriteData
# Allows you to update your feed, including updating/creating new datastreams and datapoints. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class WriteData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WriteData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/WriteData')


    def new_input_set(self):
        return WriteDataInputSet()

    def _make_result_set(self, result, path):
        return WriteDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WriteDataChoreographyExecution(session, exec_id, path)

class WriteDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WriteData
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FeedData(self, value):
        """
        Set the value of the FeedData input for this Choreo. ((optional, any) Custom data body for the new feed in JSON or XML format (set by FeedType). See documentation for the minimum required fields for a feed. If custom FeedData is used, Value and Timestamp is ignored.)
        """
        InputSet._set_input(self, 'FeedData', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((optional, string) ID for single datastream you would like to update. Required if specifying a single datapoint update using Value.)
        """
        InputSet._set_input(self, 'DatastreamID', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID for the feed that you would like to update.)
        """
        InputSet._set_input(self, 'FeedID', value)
    def set_FeedType(self, value):
        """
        Set the value of the FeedType input for this Choreo. ((optional, string) The type of feed that is being provided for custom FeedData. Valid values are "json" (the default), "xml" and "csv". Ignored if specifying single datapoint Value.)
        """
        InputSet._set_input(self, 'FeedType', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((optional, date) Can be used with a single Value and DatastreamID. If specified, sets timestamp for Value. If Value is set with blank Timestamp, Value's timestamp will be current time. Ex: 2013-05-10T00:00:00.123456Z.)
        """
        InputSet._set_input(self, 'Timestamp', value)
    def set_Value(self, value):
        """
        Set the value of the Value input for this Choreo. ((optional, string) Specifies the value for a single datapoint in a specified datastream.)
        """
        InputSet._set_input(self, 'Value', value)

class WriteDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WriteData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful feed / data update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class WriteDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WriteDataResultSet(response, path)
