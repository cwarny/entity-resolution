# -*- coding: utf-8 -*-

###############################################################################
#
# GetLocationInformation
# Retrieves information about a location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetLocationInformation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLocationInformation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetLocationInformation')


    def new_input_set(self):
        return GetLocationInformationInputSet()

    def _make_result_set(self, result, path):
        return GetLocationInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLocationInformationChoreographyExecution(session, exec_id, path)

class GetLocationInformationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLocationInformation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_LocationID(self, value):
        """
        Set the value of the LocationID input for this Choreo. ((required, integer) The ID for the location that you want to retrieve information for.)
        """
        InputSet._set_input(self, 'LocationID', value)

class GetLocationInformationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLocationInformation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetLocationInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLocationInformationResultSet(response, path)
