# -*- coding: utf-8 -*-

###############################################################################
#
# Blogs
# Retrieves a list of NPR blogs and corresponding IDs. Also used to look up the IDs of specific NPR blog by specifying those as an optional parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Blogs(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Blogs Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/Blogs')


    def new_input_set(self):
        return BlogsInputSet()

    def _make_result_set(self, result, path):
        return BlogsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BlogsChoreographyExecution(session, exec_id, path)

class BlogsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Blogs
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Blog(self, value):
        """
        Set the value of the Blog input for this Choreo. ((optional, string) The specific blog title to return. Multiple blog titles can be specified separated by commas (i.e. Soapbox,Planet Money). Blog IDs are returned when this input is used.)
        """
        InputSet._set_input(self, 'Blog', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Set to json or xml (the default). Note that when specifying Blog, only xml is returned.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
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

class BlogsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Blogs Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Id(self):
        """
        Retrieve the value for the "Id" output from this Choreo execution. ((integer) The ID of the blog. This is only returned when the Blog input is specified. When multiple blogs are specified, this will be a list of IDs separated by commas.)
        """
        return self._output.get('Id', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class BlogsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BlogsResultSet(response, path)
