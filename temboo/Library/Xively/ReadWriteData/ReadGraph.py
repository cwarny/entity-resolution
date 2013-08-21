# -*- coding: utf-8 -*-

###############################################################################
#
# ReadGraph
# Returns a customizable graph (Base64-encoded PNG image file) of datapoints from a specific datastream.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReadGraph(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReadGraph Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/ReadWriteData/ReadGraph')


    def new_input_set(self):
        return ReadGraphInputSet()

    def _make_result_set(self, result, path):
        return ReadGraphResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReadGraphChoreographyExecution(session, exec_id, path)

class ReadGraphInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReadGraph
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Color(self, value):
        """
        Set the value of the Color input for this Choreo. ((optional, string) The PNG color in hex. Ex: FFCC33.)
        """
        InputSet._set_input(self, 'Color', value)
    def set_DatastreamID(self, value):
        """
        Set the value of the DatastreamID input for this Choreo. ((required, string) The ID for the datastream you wish to read.)
        """
        InputSet._set_input(self, 'DatastreamID', value)
    def set_Duration(self, value):
        """
        Set the value of the Duration input for this Choreo. ((optional, string) Used for a historical query. If used with EndDate will request data prior to EndDate, if used with StartDate will request data after StartDate. By itself will give most recent data. Ex: 6hours, 2days.)
        """
        InputSet._set_input(self, 'Duration', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) Used for a historical query. Defines the end point of the data returned as a timestamp. Ex: 2013-05-10T12:00:00Z. Default value is set to current timestamp.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((required, integer) The ID of the feed you wish to read.)
        """
        InputSet._set_input(self, 'FeedID', value)
    def set_FindPrevious(self, value):
        """
        Set the value of the FindPrevious input for this Choreo. ((optional, boolean) Used for a historical query. Will also return the previous value to the date range being requested. Useful to allow a graph to start a graph with some datapoint. Valid values: "true", blank (default).)
        """
        InputSet._set_input(self, 'FindPrevious', value)
    def set_Height(self, value):
        """
        Set the value of the Height input for this Choreo. ((optional, integer) The PNG height in pixels. Max height: 500. Ex: 400.)
        """
        InputSet._set_input(self, 'Height', value)
    def set_IntervalType(self, value):
        """
        Set the value of the IntervalType input for this Choreo. ((optional, string) Used for a historical query. If set to "discrete" the data will be returned in fixed time interval format according to Interval value. If not set, the raw datapoints will be returned.)
        """
        InputSet._set_input(self, 'IntervalType', value)
    def set_Interval(self, value):
        """
        Set the value of the Interval input for this Choreo. ((optional, integer) Used for a historical query. Determines what interval of data is requested and is defined in seconds between the datapoints. See documentation for full list of possible values. Ex: 0, 30, 60, etc.)
        """
        InputSet._set_input(self, 'Interval', value)
    def set_Legend(self, value):
        """
        Set the value of the Legend input for this Choreo. ((optional, string) Label given datapoints on a legend included on the graph.)
        """
        InputSet._set_input(self, 'Legend', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Used for a historical query. LImits the number of results to the number specified here. Defaults to 100, has a maximum of 1000.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_LineSize(self, value):
        """
        Set the value of the LineSize input for this Choreo. ((optional, integer) Size of the lines/strokes in pixels. Ex: 4.)
        """
        InputSet._set_input(self, 'LineSize', value)
    def set_ShowAxisLabels(self, value):
        """
        Set the value of the ShowAxisLabels input for this Choreo. ((optional, boolean) Show access labels. Input "true" to turn on, leave blank to keep off (default).)
        """
        InputSet._set_input(self, 'ShowAxisLabels', value)
    def set_ShowDetailedGrid(self, value):
        """
        Set the value of the ShowDetailedGrid input for this Choreo. ((optional, string) Show detailed grid. Input "true" to turn on, leave blank to keep off (default).)
        """
        InputSet._set_input(self, 'ShowDetailedGrid', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Used for a historical query. Defines the starting the point of the query as a timestamp. Ex: 2013-05-10T00:00:00Z.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_Timezone(self, value):
        """
        Set the value of the Timezone input for this Choreo. ((optional, string) Timezone of the graph. For a list of valid values please see description and API documenation. Ex: Eastern Time (US & Canada), Pacific Time (US & Canada), UTC, Tokyo.)
        """
        InputSet._set_input(self, 'Timezone', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) Title of the graph.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Width(self, value):
        """
        Set the value of the Width input for this Choreo. ((optional, integer) The PNG width in pixels. Max width: 600. Ex: 600.)
        """
        InputSet._set_input(self, 'Width', value)
    def set_YAxisMax(self, value):
        """
        Set the value of the YAxisMax input for this Choreo. ((optional, string) Y-axis maximum value if the YAxisScale is set to "manual".)
        """
        InputSet._set_input(self, 'YAxisMax', value)
    def set_YAxisMin(self, value):
        """
        Set the value of the YAxisMin input for this Choreo. ((optional, string) Y-axis minimum value if the YAxisScale is set to "manual".)
        """
        InputSet._set_input(self, 'YAxisMin', value)
    def set_YAxisScale(self, value):
        """
        Set the value of the YAxisScale input for this Choreo. ((optional, string) Method used to determine the y-axis scale. Valid values: "auto" (default), "datastream", or "manual".)
        """
        InputSet._set_input(self, 'YAxisScale', value)

class ReadGraphResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReadGraph Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Xively, which is a base64-encoded binary .png file. Decode to get the binary PNG graphic.)
        """
        return self._output.get('Response', None)

class ReadGraphChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReadGraphResultSet(response, path)
