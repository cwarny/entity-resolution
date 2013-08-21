# coding: utf-8

class FoursquareListedItems:
    """
     Contains list objects for the authenitcated user
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCanonicalUrl(self):
        """
        The canonical url for the list
        """
        return self.base.get("canonicalUrl", [])

    def getCollaborative(self):
        """
        Whether or not this list is editable by the owner's friends
        """
        return self.base.get("collaborative", [])

    def getCreatedAt(self):
        """
        The epoch timestamp for when this list was created
        """
        return self.base.get("createdAt", [])

    def getDescription(self):
        """
        The description of the list
        """
        return self.base.get("description", [])

    def getEditable(self):
        """
        Whether or not this item is editable
        """
        return self.base.get("editable", [])

    def getFollowers(self):
        """
        Get the follower count for this list item
        """
        return FoursquareFollowers(self.base.get("followers", []))

    def getId(self):
        """
        The id of this item
        """
        return self.base.get("id", [])

    def getItems(self):
        """
        Get the list items
        """
        return [FoursquareItem(le) for le in self.getJSONObject(self.base, "listItems").get("items", [])]


    def getName(self):
        """
        The name of the list
        """
        return self.base.get("name", [])

    def getPublic(self):
        """
        Whether or not the list is public
        """
        return self.base.get("public", [])

    def getUpdatedAt(self):
        """
        An epoch timestamp representing the last update time for the list
        """
        return self.base.get("updatedAt", [])

    def getUrl(self):
        """
        The url for the list
        """
        return self.base.get("url", [])

    def getUser(self):
        """
        Get the user who created the list
        """
        return FoursquareUser(self.base.get("user", []))

    def getBase(self):
        """
        Internal utility method; retrieve the base JSON object for this element of the response data.
        """
        return self.base

    def getJSONObject(self, json, key):
        """
        Internal utility method; retrieve a sub-object from a JSON object/array; returns an empty object if key is not present
        """
        toReturn = {}

        if json is not None:
            toReturn = json.get(key, {})

        return toReturn

from temboo.outputs.Foursquare.FoursquareFollowers import FoursquareFollowers
from temboo.outputs.Foursquare.FoursquareItem import FoursquareItem
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser