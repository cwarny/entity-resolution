# -*- coding: utf-8 -*-

###############################################################################
#
# PublishLink
# Publishes a link on a given profile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PublishLink(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PublishLink Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/PublishLink')


    def new_input_set(self):
        return PublishLinkInputSet()

    def _make_result_set(self, result, path):
        return PublishLinkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PublishLinkChoreographyExecution(session, exec_id, path)

class PublishLinkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PublishLink
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Caption(self, value):
        """
        Set the value of the Caption input for this Choreo. ((optional, string) A caption for the link being published.)
        """
        InputSet._set_input(self, 'Caption', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the link being published.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Link(self, value):
        """
        Set the value of the Link input for this Choreo. ((required, string) The link to publish.)
        """
        InputSet._set_input(self, 'Link', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message about the link.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) The name of the link.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Picture(self, value):
        """
        Set the value of the Picture input for this Choreo. ((optional, string) A URL to the thumbnail image to use for the link post.)
        """
        InputSet._set_input(self, 'Picture', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile that the link will be published to. Defaults to "me" indicating the authenticated user.)
        """
        InputSet._set_input(self, 'ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class PublishLinkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PublishLink Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getFacebookObjectId(self):
        """
        Get the ID of the object that has been created
        """
        return self.getJSONFromString(self._output.get('Response', [])).get("id", [])

class PublishLinkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PublishLinkResultSet(response, path)
