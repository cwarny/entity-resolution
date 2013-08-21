# -*- coding: utf-8 -*-

###############################################################################
#
# ObjectGet
# Retrieves one or more objects from Cloudmine.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ObjectGet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ObjectGet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/ObjectStorage/ObjectGet')


    def new_input_set(self):
        return ObjectGetInputSet()

    def _make_result_set(self, result, path):
        return ObjectGetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ObjectGetChoreographyExecution(session, exec_id, path)

class ObjectGetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ObjectGet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'ApplicationIdentifier', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, boolean) Returns a count of the results in the response if set to true. Valid values are true and false.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_Keys(self, value):
        """
        Set the value of the Keys input for this Choreo. ((optional, string) A comma separated list of keys to return. If not specified, all key/value pairs are returned.)
        """
        InputSet._set_input(self, 'Keys', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limits the number of results returned. Use -1 for no limit. Use 0 for no results, and with Count=true to just get the number of available results. This defaults to 50.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        InputSet._set_input(self, 'SessionToken', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Indicates to start results after skiping this number objects. Used to page through results.)
        """
        InputSet._set_input(self, 'Skip', value)

class ObjectGetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ObjectGet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class ObjectGetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ObjectGetResultSet(response, path)
