# -*- coding: utf-8 -*-

###############################################################################
#
# GetLoadServingEntity
# Returns a Load Serving Entity with a given ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetLoadServingEntity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLoadServingEntity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetLoadServingEntity')


    def new_input_set(self):
        return GetLoadServingEntityInputSet()

    def _make_result_set(self, result, path):
        return GetLoadServingEntityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLoadServingEntityChoreographyExecution(session, exec_id, path)

class GetLoadServingEntityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLoadServingEntity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) The App ID provided by Genability.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_LSEID(self, value):
        """
        Set the value of the LSEID input for this Choreo. ((required, integer) The id of a particular Load Serving Entity to return.)
        """
        InputSet._set_input(self, 'LSEID', value)

class GetLoadServingEntityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLoadServingEntity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetLoadServingEntityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLoadServingEntityResultSet(response, path)
