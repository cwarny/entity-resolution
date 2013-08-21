# -*- coding: utf-8 -*-

###############################################################################
#
# CreateShare
# Allows you to share content on behalf of a LinkedIn member.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateShare(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateShare Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/ShareAndSocialStream/CreateShare')


    def new_input_set(self):
        return CreateShareInputSet()

    def _make_result_set(self, result, path):
        return CreateShareResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateShareChoreographyExecution(session, exec_id, path)

class CreateShareInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateShare
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
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((conditional, string) The text of the member's comment. Required unless providing Title and URL for a shared post.)
        """
        InputSet._set_input(self, 'Comment', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A description of the shared content.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_ImageURL(self, value):
        """
        Set the value of the ImageURL input for this Choreo. ((optional, string) The URL for the image of the shared content.)
        """
        InputSet._set_input(self, 'ImageURL', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((conditional, string) The title of the shared content. Required unless providing a Comment.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((conditional, string) The URL for the shared content. Required unless providing a Comment.)
        """
        InputSet._set_input(self, 'URL', value)
    def set_Visibility(self, value):
        """
        Set the value of the Visibility input for this Choreo. ((optional, string) Determines if the post will be visible to everyone, or only those who are connected to you. Valid values are: "anyone" or "connections-only" (the default).)
        """
        InputSet._set_input(self, 'Visibility', value)

class CreateShareResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateShare Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from LinkedIn.)
        """
        return self._output.get('Response', None)

class CreateShareChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateShareResultSet(response, path)
