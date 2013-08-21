# -*- coding: utf-8 -*-

###############################################################################
#
# GetLinkInfo
# Returns the page title for a given bitly link.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetLinkInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetLinkInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Bitly/Links/GetLinkInfo')


    def new_input_set(self):
        return GetLinkInfoInputSet()

    def _make_result_set(self, result, path):
        return GetLinkInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetLinkInfoChoreographyExecution(session, exec_id, path)

class GetLinkInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetLinkInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The oAuth access token provided by Bitly.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ShortURL(self, value):
        """
        Set the value of the ShortURL input for this Choreo. ((required, string) One or more bitly links.)
        """
        InputSet._set_input(self, 'ShortURL', value)

class GetLinkInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetLinkInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class GetLinkInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetLinkInfoResultSet(response, path)
