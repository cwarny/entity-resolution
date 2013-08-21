# -*- coding: utf-8 -*-

###############################################################################
#
# FindByURL
# Obtain geo-location information for a place using its flickr.com/places URL.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindByURL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindByURL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Places/FindByURL')


    def new_input_set(self):
        return FindByURLInputSet()

    def _make_result_set(self, result, path):
        return FindByURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByURLChoreographyExecution(session, exec_id, path)

class FindByURLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindByURL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) Enter a flickr.com/places URL in the following form: /country/region/city. For example: /USA/NewYork/Rochester.)
        """
        InputSet._set_input(self, 'URL', value)

class FindByURLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindByURL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class FindByURLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindByURLResultSet(response, path)
