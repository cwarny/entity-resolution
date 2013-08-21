# -*- coding: utf-8 -*-

###############################################################################
#
# Series
# Retrieves a list of NPR series titles and corresponding IDs. Also used to look up the IDs of specific NPR series by specifying those as an optional parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Series(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Series Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/Series')


    def new_input_set(self):
        return SeriesInputSet()

    def _make_result_set(self, result, path):
        return SeriesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SeriesChoreographyExecution(session, exec_id, path)

class SeriesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Series
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Set to json or xml (the default). Note that when specifying Series, only xml is returned.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Series(self, value):
        """
        Set the value of the Series input for this Choreo. ((optional, string) The specific series title to return. Multiple titles can be specified separated by commas (i.e. Life in Berlin,Climate Connections). Series IDs are returned when this input is used.)
        """
        InputSet._set_input(self, 'Series', value)
    def set_StoryCountAll(self, value):
        """
        Set the value of the StoryCountAll input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories.)
        """
        InputSet._set_input(self, 'StoryCountAll', value)
    def set_StoryCountMonth(self, value):
        """
        Set the value of the StoryCountMonth input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published in the last month.)
        """
        InputSet._set_input(self, 'StoryCountMonth', value)
    def set_StoryCountToday(self, value):
        """
        Set the value of the StoryCountToday input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published today.)
        """
        InputSet._set_input(self, 'StoryCountToday', value)

class SeriesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Series Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Id(self):
        """
        Retrieve the value for the "Id" output from this Choreo execution. ((integer) The ID of the series. This is only returned when the Series input is specified. When multiple series are specified, this will be a list of IDs separated by commas.)
        """
        return self._output.get('Id', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class SeriesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SeriesResultSet(response, path)
