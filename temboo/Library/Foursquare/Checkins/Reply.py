# -*- coding: utf-8 -*-

###############################################################################
#
# Reply
# Replies to a user about their check-in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification
from temboo.outputs.Foursquare.FoursquareReply import FoursquareReply

import json

class Reply(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Reply Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/Reply')


    def new_input_set(self):
        return ReplyInputSet()

    def _make_result_set(self, result, path):
        return ReplyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReplyChoreographyExecution(session, exec_id, path)

class ReplyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Reply
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((required, string) The ID of the check-in to add a post to.)
        """
        InputSet._set_input(self, 'CheckinID', value)
    def set_ContentID(self, value):
        """
        Set the value of the ContentID input for this Choreo. ((optional, string) An ID for the reply to be used in a native link. Can be up to 50 characters. The URL input must also be specified when using this parameter.)
        """
        InputSet._set_input(self, 'ContentID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The FourSquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text of the post. Max length is 200 characters.)
        """
        InputSet._set_input(self, 'Text', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) A URL linking to more details. The following URL schemes are supported: http, https, foursquare, mailto, tel, and sms.)
        """
        InputSet._set_input(self, 'URL', value)

class ReplyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Reply Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getMeta(self):
        """
        Get the response status code
        """
        return FoursquareMeta(self.getJSONFromString(self._output.get('Response', [])).get("meta", []))
    def getNotifications(self):
        """
        Get the count of unread notifications for the authenticated user
        """
        return [FoursquareNotification(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("notifications", [])]

    def getReply(self):
        """
        Get the reply to a checkin
        """
        return FoursquareReply(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("reply", []))

class ReplyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReplyResultSet(response, path)
