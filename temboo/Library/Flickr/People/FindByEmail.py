# -*- coding: utf-8 -*-

###############################################################################
#
# FindByEmail
# Obtain a user's NSID by providing their email address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindByEmail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindByEmail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/People/FindByEmail')


    def new_input_set(self):
        return FindByEmailInputSet()

    def _make_result_set(self, result, path):
        return FindByEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByEmailChoreographyExecution(session, exec_id, path)

class FindByEmailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindByEmail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_FindEmail(self, value):
        """
        Set the value of the FindEmail input for this Choreo. ((required, string) Enter the email of the user being sought.)
        """
        InputSet._set_input(self, 'FindEmail', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class FindByEmailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindByEmail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class FindByEmailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindByEmailResultSet(response, path)
