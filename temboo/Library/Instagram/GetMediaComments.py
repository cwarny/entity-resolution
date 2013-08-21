# -*- coding: utf-8 -*-

###############################################################################
#
# GetMediaComments
# Retrieves a full list of comments for a specified media object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetMediaComments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMediaComments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetMediaComments')


    def new_input_set(self):
        return GetMediaCommentsInputSet()

    def _make_result_set(self, result, path):
        return GetMediaCommentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMediaCommentsChoreographyExecution(session, exec_id, path)

class GetMediaCommentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMediaComments
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
    def set_MediaID(self, value):
        """
        Set the value of the MediaID input for this Choreo. ((required, integer) The ID of the media object that you want to get comments for. For example, a valid MediaID could be 3.)
        """
        InputSet._set_input(self, 'MediaID', value)

class GetMediaCommentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMediaComments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetMediaCommentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMediaCommentsResultSet(response, path)
