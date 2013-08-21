# -*- coding: utf-8 -*-

###############################################################################
#
# Bios
# Retrieves a list of NPR personalities and corresponding IDs. Also used to look up the IDs of specific NPR personalities by specifying them as an optional parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Bios(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Bios Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/Bios')


    def new_input_set(self):
        return BiosInputSet()

    def _make_result_set(self, result, path):
        return BiosResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BiosChoreographyExecution(session, exec_id, path)

class BiosInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Bios
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Personality(self, value):
        """
        Set the value of the Personality input for this Choreo. ((optional, string) The specific name or an NPR personality to return. Multiple names can be specified separated by commas (i.e. Andrei Codrescu,Allison Keyes). Personality IDs are returned when this input is used.)
        """
        InputSet._set_input(self, 'Personality', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Set to json or xml (the default). Note that when specifying Personality, only xml is returned.)
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

class BiosResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Bios Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Id(self):
        """
        Retrieve the value for the "Id" output from this Choreo execution. ((integer) The ID of the personality specified. This is only returned when the Personality input is specified. When personalities are specified, this will be a list of IDs separated by commas.)
        """
        return self._output.get('Id', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class BiosChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BiosResultSet(response, path)
