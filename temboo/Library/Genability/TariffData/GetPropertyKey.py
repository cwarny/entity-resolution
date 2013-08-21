# -*- coding: utf-8 -*-

###############################################################################
#
# GetPropertyKey
# Returns an individual Property Key using a given key name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPropertyKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPropertyKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetPropertyKey')


    def new_input_set(self):
        return GetPropertyKeyInputSet()

    def _make_result_set(self, result, path):
        return GetPropertyKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPropertyKeyChoreographyExecution(session, exec_id, path)

class GetPropertyKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPropertyKey
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
    def set_KeyName(self, value):
        """
        Set the value of the KeyName input for this Choreo. ((required, string) The key name for the property key you want to return.)
        """
        InputSet._set_input(self, 'KeyName', value)

class GetPropertyKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPropertyKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetPropertyKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPropertyKeyResultSet(response, path)
