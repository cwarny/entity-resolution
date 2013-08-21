# -*- coding: utf-8 -*-

###############################################################################
#
# Outbox
# Retrieves a list of messages in a specified user's outbox.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Facebook.FacebookOutboxItem import FacebookOutboxItem

import json

class Outbox(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Outbox Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Reading/Outbox')


    def new_input_set(self):
        return OutboxInputSet()

    def _make_result_set(self, result, path):
        return OutboxResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return OutboxChoreographyExecution(session, exec_id, path)

class OutboxInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Outbox
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to retrieve outgoing messages for. Defaults to "me" indicating the authenticated user.)
        """
        InputSet._set_input(self, 'ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class OutboxResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Outbox Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getOutboxItems(self):
        """
        Get the user's outbox item
        """
        return [FacebookOutboxItem(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("data", [])]


class OutboxChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return OutboxResultSet(response, path)
