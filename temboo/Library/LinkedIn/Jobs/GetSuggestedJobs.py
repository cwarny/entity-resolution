# -*- coding: utf-8 -*-

###############################################################################
#
# GetSuggestedJobs
# Get a list of job suggestions for the current user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetSuggestedJobs(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetSuggestedJobs Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/Jobs/GetSuggestedJobs')


    def new_input_set(self):
        return GetSuggestedJobsInputSet()

    def _make_result_set(self, result, path):
        return GetSuggestedJobsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetSuggestedJobsChoreographyExecution(session, exec_id, path)

class GetSuggestedJobsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetSuggestedJobs
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)

class GetSuggestedJobsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetSuggestedJobs Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from LinkedIn in XML format.)
        """
        return self._output.get('Response', None)

class GetSuggestedJobsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetSuggestedJobsResultSet(response, path)
