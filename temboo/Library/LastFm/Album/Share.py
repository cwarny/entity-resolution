# -*- coding: utf-8 -*-

###############################################################################
#
# Share
# Allows you to share an album with one or more Last.fm users or other friends.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Share(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Share Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Album/Share')


    def new_input_set(self):
        return ShareInputSet()

    def _make_result_set(self, result, path):
        return ShareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShareChoreographyExecution(session, exec_id, path)

class ShareInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Share
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
    def set_Album(self, value):
        """
        Set the value of the Album input for this Choreo. ((string) The album name.)
        """
        InputSet._set_input(self, 'Album', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((string) The artist name.)
        """
        InputSet._set_input(self, 'Artist', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) An optional message to send with the recommendation. If not supplied a default message will be used.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_Public(self, value):
        """
        Set the value of the Public input for this Choreo. ((optional, boolean) Optionally show in the sharing users activity feed. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'Public', value)
    def set_Recipient(self, value):
        """
        Set the value of the Recipient input for this Choreo. ((string) A comma delimited list of email addresses or Last.fm usernames. Maximum is 10.)
        """
        InputSet._set_input(self, 'Recipient', value)
    def set_SessionKey(self, value):
        """
        Set the value of the SessionKey input for this Choreo. ((string) The session key retrieved in the last step of the authorization process.)
        """
        InputSet._set_input(self, 'SessionKey', value)

class ShareResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Share Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class ShareChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShareResultSet(response, path)
