# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateList
# Updates a given list.
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

class UpdateList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/UpdateList')


    def new_input_set(self):
        return UpdateListInputSet()

    def _make_result_set(self, result, path):
        return UpdateListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateListChoreographyExecution(session, exec_id, path)

class UpdateListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Collaborative(self, value):
        """
        Set the value of the Collaborative input for this Choreo. ((optional, boolean) A flag indicating that this list can be edited by friends. Set to 1 for true. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'Collaborative', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The description of the list.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, string) The id of the list to update.)
        """
        InputSet._set_input(self, 'ListID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the list.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The FourSquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((optional, string) The id of a photo that should be set as the list photo.)
        """
        InputSet._set_input(self, 'PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class UpdateListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateList Choreo.
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

class UpdateListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateListResultSet(response, path)
