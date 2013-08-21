# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteComment
# Removes a comment to a specified check-in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareCheckin import FoursquareCheckin
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class DeleteComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/DeleteComment')


    def new_input_set(self):
        return DeleteCommentInputSet()

    def _make_result_set(self, result, path):
        return DeleteCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCommentChoreographyExecution(session, exec_id, path)

class DeleteCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((required, string) The ID of the check-in associated with the comment you want to remove.)
        """
        InputSet._set_input(self, 'CheckinID', value)
    def set_CommentID(self, value):
        """
        Set the value of the CommentID input for this Choreo. ((required, string) The id of the comment to remove.)
        """
        InputSet._set_input(self, 'CommentID', value)
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

class DeleteCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteComment Choreo.
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

    def getCheckin(self):
        """
        Get the checkin associated with the deleted comment
        """
        return FoursquareCheckin(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("checkin", []))

class DeleteCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteCommentResultSet(response, path)
