# -*- coding: utf-8 -*-

###############################################################################
#
# GetTimeOfUseGroupIntervals
# Returns all the Intervals for a Time of Use Group within a given date range.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTimeOfUseGroupIntervals(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTimeOfUseGroupIntervals Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetTimeOfUseGroupIntervals')


    def new_input_set(self):
        return GetTimeOfUseGroupIntervalsInputSet()

    def _make_result_set(self, result, path):
        return GetTimeOfUseGroupIntervalsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTimeOfUseGroupIntervalsChoreographyExecution(session, exec_id, path)

class GetTimeOfUseGroupIntervalsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTimeOfUseGroupIntervals
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The App ID provided by Genability.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_FromDateTime(self, value):
        """
        Set the value of the FromDateTime input for this Choreo. ((optional, date) The starting date and time of the requested Intervals (in ISO 8601 format). Defaults to current date if not specified.)
        """
        InputSet._set_input(self, 'FromDateTime', value)
    def set_LSEID(self, value):
        """
        Set the value of the LSEID input for this Choreo. ((required, integer) Used to retrieve a TOU Group for a specific LSE.)
        """
        InputSet._set_input(self, 'LSEID', value)
    def set_PageCount(self, value):
        """
        Set the value of the PageCount input for this Choreo. ((optional, integer) The number of results to return. Defaults to 25.)
        """
        InputSet._set_input(self, 'PageCount', value)
    def set_PageStart(self, value):
        """
        Set the value of the PageStart input for this Choreo. ((optional, integer) The page number to begin the result set from. Defaults to 1.)
        """
        InputSet._set_input(self, 'PageStart', value)
    def set_TOUGroupID(self, value):
        """
        Set the value of the TOUGroupID input for this Choreo. ((required, integer) Used to retrieve a TOU Group by its ID.)
        """
        InputSet._set_input(self, 'TOUGroupID', value)
    def set_ToDateTime(self, value):
        """
        Set the value of the ToDateTime input for this Choreo. ((optional, date) The ending date and time of the requested Intervals (in ISO 8601 format). If not specified, defaults to one week ahead of the current date.)
        """
        InputSet._set_input(self, 'ToDateTime', value)

class GetTimeOfUseGroupIntervalsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTimeOfUseGroupIntervals Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTimeOfUseGroupIntervalsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTimeOfUseGroupIntervalsResultSet(response, path)
