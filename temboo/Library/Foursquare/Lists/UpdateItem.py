# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateItem
# Allows you to add or remove photos and tips from items on user-created lists.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareItem import FoursquareItem
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class UpdateItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/UpdateItem')


    def new_input_set(self):
        return UpdateItemInputSet()

    def _make_result_set(self, result, path):
        return UpdateItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateItemChoreographyExecution(session, exec_id, path)

class UpdateItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((required, string) The id of an item on a list that you wish to update.)
        """
        InputSet._set_input(self, 'ItemID', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, string) The ID of a user-created list to update)
        """
        InputSet._set_input(self, 'ListID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The FourSquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((optional, string) If present and non-empty, adds a photo to this item. If present and empty, will remove the photo on this item. If the photo was a private checkin photo, it will be promoted to a public venue photo.)
        """
        InputSet._set_input(self, 'PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((optional, string) If present, this creates a public tip on the venue and replaces any existing tip on the item. Cannot be used in conjuction with TipID or PhotoID.)
        """
        InputSet._set_input(self, 'Text', value)
    def set_TipID(self, value):
        """
        Set the value of the TipID input for this Choreo. ((optional, string) The id of a tip to add to the list. Cannot be used in conjunction with the Text and URL inputs. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        InputSet._set_input(self, 'TipID', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) If adding a new tip using the Text input, this can associate a url with the tip.)
        """
        InputSet._set_input(self, 'URL', value)

class UpdateItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateItem Choreo.
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

    def getItem(self):
        """
        Get the item that was updated
        """
        return FoursquareItem(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("item", []))

class UpdateItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateItemResultSet(response, path)
