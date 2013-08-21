# -*- coding: utf-8 -*-

###############################################################################
#
# GetPropertyKeys
# Returns a list of Property Keys based on a specified search criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPropertyKeys(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPropertyKeys Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetPropertyKeys')


    def new_input_set(self):
        return GetPropertyKeysInputSet()

    def _make_result_set(self, result, path):
        return GetPropertyKeysResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPropertyKeysChoreographyExecution(session, exec_id, path)

class GetPropertyKeysInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPropertyKeys
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
    def set_EntityID(self, value):
        """
        Set the value of the EntityID input for this Choreo. ((optional, string) Filters the result so that only Properties that belong to this EntityID are returned. When specified, EntityType must also be specified.)
        """
        InputSet._set_input(self, 'EntityID', value)
    def set_EntityType(self, value):
        """
        Set the value of the EntityType input for this Choreo. ((optional, string) Filters the result so that only Properties that belong to this EntityType are returned. When specified, EntityID must also be specified.)
        """
        InputSet._set_input(self, 'EntityType', value)
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

class GetPropertyKeysResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPropertyKeys Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetPropertyKeysChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPropertyKeysResultSet(response, path)
