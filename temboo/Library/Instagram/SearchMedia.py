# -*- coding: utf-8 -*-

###############################################################################
#
# SearchMedia
# Allows you to search for media in a given area.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchMedia(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchMedia Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/SearchMedia')


    def new_input_set(self):
        return SearchMediaInputSet()

    def _make_result_set(self, result, path):
        return SearchMediaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchMediaChoreographyExecution(session, exec_id, path)

class SearchMediaInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchMedia
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
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, integer) The distance in meters. Defaults to 1000. Max is 5000.)
        """
        InputSet._set_input(self, 'Distance', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Latitude of the center search coordinate.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Longitude of the center search coordinate.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_MaxTimestamp(self, value):
        """
        Set the value of the MaxTimestamp input for this Choreo. ((optional, date) A unix timestamp. All media returned will be taken earlier than this timestamp.)
        """
        InputSet._set_input(self, 'MaxTimestamp', value)
    def set_MinTimestamp(self, value):
        """
        Set the value of the MinTimestamp input for this Choreo. ((optional, date) A unix timestamp. All media returned will be taken later than this timestamp.)
        """
        InputSet._set_input(self, 'MinTimestamp', value)

class SearchMediaResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchMedia Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class SearchMediaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchMediaResultSet(response, path)
