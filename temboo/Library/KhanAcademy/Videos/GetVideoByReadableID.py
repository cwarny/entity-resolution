# -*- coding: utf-8 -*-

###############################################################################
#
# GetVideoByReadableID
# Retrieves video data for a given video according to its readable ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetVideoByReadableID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetVideoByReadableID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Videos/GetVideoByReadableID')


    def new_input_set(self):
        return GetVideoByReadableIDInputSet()

    def _make_result_set(self, result, path):
        return GetVideoByReadableIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetVideoByReadableIDChoreographyExecution(session, exec_id, path)

class GetVideoByReadableIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetVideoByReadableID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ReadableID(self, value):
        """
        Set the value of the ReadableID input for this Choreo. ((required, string) The ReadableID of the video for which you want to retrieve information (e.g. adding-subtracting-negative-numbers).)
        """
        InputSet._set_input(self, 'ReadableID', value)

class GetVideoByReadableIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetVideoByReadableID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class GetVideoByReadableIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetVideoByReadableIDResultSet(response, path)
