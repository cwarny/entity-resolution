# -*- coding: utf-8 -*-

###############################################################################
#
# CreateKey
# Creates a new APIKey.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/APIKeys/CreateKey')


    def new_input_set(self):
        return CreateKeyInputSet()

    def _make_result_set(self, result, path):
        return CreateKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateKeyChoreographyExecution(session, exec_id, path)

class CreateKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateKey
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The master API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessMethods(self, value):
        """
        Set the value of the AccessMethods input for this Choreo. ((conditional, string) Comma-separated input containing one or more allowed HTTP methods that the key is allowed. Valid values: get, put, post, and/or delete. Ex.: "put,post". Required unless writing your own CustomKey.)
        """
        InputSet._set_input(self, 'AccessMethods', value)
    def set_CustomKey(self, value):
        """
        Set the value of the CustomKey input for this Choreo. ((optional, any) Optional Custom key to send to Xively. Type and format depends on CustomType. Please see documentation for more information on constructing your own body. If used, all other scalar inputs are ignored.)
        """
        InputSet._set_input(self, 'CustomKey', value)
    def set_CustomPermissions(self, value):
        """
        Set the value of the CustomPermissions input for this Choreo. ((optional, any) Optional custom permissions for advanced configuration. Type and format depends on CustomType. If specified, ignores SourceIP, ResourcesData and AccessMethodsData.)
        """
        InputSet._set_input(self, 'CustomPermissions', value)
    def set_CustomType(self, value):
        """
        Set the value of the CustomType input for this Choreo. ((optional, string) The datatype that is being input if adding custom permission objects. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'CustomType', value)
    def set_ExpirationDate(self, value):
        """
        Set the value of the ExpirationDate input for this Choreo. ((optional, date) Expiration date for the key, after which it won't work. Must be in ISO 8601 format, default zone is UTC.  Ex: 2013-05-07T00:00:00Z.)
        """
        InputSet._set_input(self, 'ExpirationDate', value)
    def set_Label(self, value):
        """
        Set the value of the Label input for this Choreo. ((conditional, string) A label by which the key can be referenced. Required unless writing your own CustomKey.)
        """
        InputSet._set_input(self, 'Label', value)
    def set_PrivateAccess(self, value):
        """
        Set the value of the PrivateAccess input for this Choreo. ((optional, string) Flag that indicates whether this key can access private resources belonging to the user. To turn on, input "true", leave blank for "false".)
        """
        InputSet._set_input(self, 'PrivateAccess', value)
    def set_ResourceFeedID(self, value):
        """
        Set the value of the ResourceFeedID input for this Choreo. ((optional, integer) Specify a particular FeedID that the new APIKey should have access to. If not specified, the new APIKey permissions will apply to all feeds you are authorized to access.)
        """
        InputSet._set_input(self, 'ResourceFeedID', value)
    def set_SourceIP(self, value):
        """
        Set the value of the SourceIP input for this Choreo. ((optional, string) An IP address that, when specified, limits incoming requests to that specific IP address only.)
        """
        InputSet._set_input(self, 'SourceIP', value)

class CreateKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_APIKeyLocation(self):
        """
        Retrieve the value for the "APIKeyLocation" output from this Choreo execution. ((string) The URL of the newly created APIKey.)
        """
        return self._output.get('APIKeyLocation', None)
    def get_NewAPIKey(self):
        """
        Retrieve the value for the "NewAPIKey" output from this Choreo execution. ((string) The new APIKey obtained from the APIKeyLocation returned by this Choreo.)
        """
        return self._output.get('NewAPIKey', None)

class CreateKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateKeyResultSet(response, path)
