# -*- coding: utf-8 -*-

###############################################################################
#
# GetDrivingDirections
#  Generates directions between two locations, denoted by address, or latitude/longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetDrivingDirections(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDrivingDirections Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Directions/GetDrivingDirections')


    def new_input_set(self):
        return GetDrivingDirectionsInputSet()

    def _make_result_set(self, result, path):
        return GetDrivingDirectionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDrivingDirectionsChoreographyExecution(session, exec_id, path)

class GetDrivingDirectionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDrivingDirections
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Alternatives(self, value):
        """
        Set the value of the Alternatives input for this Choreo. ((optional, string) If set to true, additional routes will be returned.)
        """
        InputSet._set_input(self, 'Alternatives', value)
    def set_Avoid(self, value):
        """
        Set the value of the Avoid input for this Choreo. ((optional, string) Specify whether the calculated directions should avoid the following features: tolls, or highways.)
        """
        InputSet._set_input(self, 'Avoid', value)
    def set_Destination(self, value):
        """
        Set the value of the Destination input for this Choreo. ((required, string) Enter the address or latitude/longitude coordinates from which directions will be generated (i.e."104 Franklin St, New York, NY" or "40.7160,-74.0037").)
        """
        InputSet._set_input(self, 'Destination', value)
    def set_Origin(self, value):
        """
        Set the value of the Origin input for this Choreo. ((required, string) Enter the address or latitude/longitude coordinates from which directions will be computed (i.e."104 Franklin St, New York, NY" or "40.7160,-74.0037").)
        """
        InputSet._set_input(self, 'Origin', value)
    def set_Region(self, value):
        """
        Set the value of the Region input for this Choreo. ((optional, string) Enter the region code for the directions, specified as a ccTLD two-character value.)
        """
        InputSet._set_input(self, 'Region', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'Sensor', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) Specify the units to be used when displaying results.  Options include, metric, or imperial.)
        """
        InputSet._set_input(self, 'Units', value)
    def set_Waypoints(self, value):
        """
        Set the value of the Waypoints input for this Choreo. ((optional, string) Specify route waypoints, either by address, or latitude/longitude coordinates.)
        """
        InputSet._set_input(self, 'Waypoints', value)

class GetDrivingDirectionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDrivingDirections Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class GetDrivingDirectionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDrivingDirectionsResultSet(response, path)
