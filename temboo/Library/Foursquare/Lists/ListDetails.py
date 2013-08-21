# -*- coding: utf-8 -*-

###############################################################################
#
# ListDetails
# Returns details about a given list. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareList import FoursquareList
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class ListDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/ListDetails')


    def new_input_set(self):
        return ListDetailsInputSet()

    def _make_result_set(self, result, path):
        return ListDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListDetailsChoreographyExecution(session, exec_id, path)

class ListDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 500.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, string) The id of a user-created or followed list or an id for a tip or todo in the form of USER_ID/tips or USER_ID/todos. When getting tips or todos for the acting user, the user id is not required.)
        """
        InputSet._set_input(self, 'ListID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The FourSquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Identity of the user to get lists for. Defaults to "self" to get lists of the acting user.)
        """
        InputSet._set_input(self, 'UserID', value)

class ListDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListDetails Choreo.
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

    def getList(self):
        """
        Get get list details
        """
        return FoursquareList(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("list", []))

class ListDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListDetailsResultSet(response, path)
