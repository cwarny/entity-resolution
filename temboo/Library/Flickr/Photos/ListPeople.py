# -*- coding: utf-8 -*-

###############################################################################
#
# ListPeople
# Retrieve a list of people in a given photo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPeople(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPeople Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Photos/ListPeople')


    def new_input_set(self):
        return ListPeopleInputSet()

    def _make_result_set(self, result, path):
        return ListPeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPeopleChoreographyExecution(session, exec_id, path)

class ListPeopleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPeople
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, string) Enter the ID of a photo for which people will be listed.)
        """
        InputSet._set_input(self, 'PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListPeopleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPeople Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListPeopleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPeopleResultSet(response, path)
