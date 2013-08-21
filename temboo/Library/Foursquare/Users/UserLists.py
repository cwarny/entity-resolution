# -*- coding: utf-8 -*-

###############################################################################
#
# UserLists
# Retrieves user lists.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareListGroup import FoursquareListGroup
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class UserLists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UserLists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/UserLists')


    def new_input_set(self):
        return UserListsInputSet()

    def _make_result_set(self, result, path):
        return UserListsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserListsChoreographyExecution(session, exec_id, path)

class UserListsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UserLists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Group(self, value):
        """
        Set the value of the Group input for this Choreo. ((optional, string) Used to narrow down the lists to returns. Valid values are: created, edited, followed, friends, and suggested. See documentation for definitions of these parameter values.)
        """
        InputSet._set_input(self, 'Group', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) Latitude of user's location. Required in order to return the suggested group.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) Longitude of user's location. Required in order to return the suggested group.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
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

class UserListsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UserLists Choreo.
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

    def getListGroups(self):
        """
        Get list groups
        """
        return [FoursquareListGroup(le) for le in self.getJSONObject(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response"), "lists").get("groups", [])]


class UserListsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserListsResultSet(response, path)
