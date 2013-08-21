# -*- coding: utf-8 -*-

###############################################################################
#
# Programs
# Retrieves a list of NPR programs and corresponding IDs. Also used to look up the IDs of specific NPR programs by specifying them as an optional parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Programs(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Programs Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/Programs')


    def new_input_set(self):
        return ProgramsInputSet()

    def _make_result_set(self, result, path):
        return ProgramsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ProgramsChoreographyExecution(session, exec_id, path)

class ProgramsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Programs
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Program(self, value):
        """
        Set the value of the Program input for this Choreo. ((optional, string) The specific program title to return. Multiple prorgam titles can be specified separated by commas (i.e. All Things Considered,Tell Me More). Program IDs are returned when this input is used.)
        """
        InputSet._set_input(self, 'Program', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Set to json or xml (the default). Note that when specifying Program, only xml is returned.)
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

class ProgramsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Programs Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Id(self):
        """
        Retrieve the value for the "Id" output from this Choreo execution. ((integer) The ID of the program. This is only returned when the Program input is specified. When multiple programs are specified, this will be a list of IDs separated by commas.)
        """
        return self._output.get('Id', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class ProgramsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ProgramsResultSet(response, path)
