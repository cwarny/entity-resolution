# -*- coding: utf-8 -*-

###############################################################################
#
# AddTags
# Tags an artist with one or more user supplied tags. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Artist/AddTags')


    def new_input_set(self):
        return AddTagsInputSet()

    def _make_result_set(self, result, path):
        return AddTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddTagsChoreographyExecution(session, exec_id, path)

class AddTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((string) Your Last.fm API Secret.)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((string) The artist name.)
        """
        InputSet._set_input(self, 'Artist', value)
    def set_SessionKey(self, value):
        """
        Set the value of the SessionKey input for this Choreo. ((string) The session key retrieved in the last step of the authorization process.)
        """
        InputSet._set_input(self, 'SessionKey', value)
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((string) A comma delimited list of user supplied tags to apply to this artist. Accepts a maximum of 10 tags.)
        """
        InputSet._set_input(self, 'Tags', value)

class AddTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class AddTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddTagsResultSet(response, path)
