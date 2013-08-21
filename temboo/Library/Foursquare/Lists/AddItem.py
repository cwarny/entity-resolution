# -*- coding: utf-8 -*-

###############################################################################
#
# AddItem
# Allows a user to add an item to a list.
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

class AddItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Lists/AddItem')


    def new_input_set(self):
        return AddItemInputSet()

    def _make_result_set(self, result, path):
        return AddItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddItemChoreographyExecution(session, exec_id, path)

class AddItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ItemID(self, value):
        """
        Set the value of the ItemID input for this Choreo. ((conditional, string) The id of an item on a list that you wish to copy to the target list. Used in conjuction with ListID. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        InputSet._set_input(self, 'ItemID', value)
    def set_ItemListID(self, value):
        """
        Set the value of the ItemListID input for this Choreo. ((conditional, string) The ID of a list that contains an item that you wish to copy to the new list. Used in conjuction with ItemID. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        InputSet._set_input(self, 'ItemListID', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, string) The ID of the list that  you are adding an item to. This can be a user-created list id or one of tips, todos, or dones.)
        """
        InputSet._set_input(self, 'ListID', value)
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
        Set the value of the Text input for this Choreo. ((optional, string) If the target is a user-created list, this will create a public tip on the venue. If the target is todos, the text will be a private note that is only visible to the author.)
        """
        InputSet._set_input(self, 'Text', value)
    def set_TipID(self, value):
        """
        Set the value of the TipID input for this Choreo. ((conditional, string) The id of a tip to add to the list. Cannot be used in conjunction with the Text and URL inputs. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        InputSet._set_input(self, 'TipID', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) If adding a new tip using the Text input, this can associate a url with the tip.)
        """
        InputSet._set_input(self, 'URL', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((conditional, string) The id of a venue to add to the list. Note that one of the following must be specified: VenueID, TipID, ItemListID, or ItemID.)
        """
        InputSet._set_input(self, 'VenueID', value)

class AddItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddItem Choreo.
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
        Get the item that was added to a list
        """
        return FoursquareItem(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("item", []))

class AddItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddItemResultSet(response, path)
