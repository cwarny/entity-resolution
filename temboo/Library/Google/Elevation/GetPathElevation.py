# -*- coding: utf-8 -*-

###############################################################################
#
# GetPathElevation
# Obtain elevation information for a path specified by a set of  geo-coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPathElevation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPathElevation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Elevation/GetPathElevation')


    def new_input_set(self):
        return GetPathElevationInputSet()

    def _make_result_set(self, result, path):
        return GetPathElevationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPathElevationChoreographyExecution(session, exec_id, path)

class GetPathElevationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPathElevation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) Specify the path for which elevation data will be obtained.  Input formats: an array of two or more lat/longitude coordinate pairs; A set of encoded coordinates using the Encoded Polyline Algorithm.)
        """
        InputSet._set_input(self, 'Path', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Samples(self, value):
        """
        Set the value of the Samples input for this Choreo. ((required, integer) Enter the number of sample points.  See API docs for additional information.)
        """
        InputSet._set_input(self, 'Samples', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'Sensor', value)

class GetPathElevationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPathElevation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)

class GetPathElevationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPathElevationResultSet(response, path)
