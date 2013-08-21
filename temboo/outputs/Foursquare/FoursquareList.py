# coding: utf-8

class FoursquareList:
    """
     A list object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCanonicalUrl(self):
        """
        The canonical URL for the list
        """
        return self.base.get("canonicalUrl", [])

    def getCategories(self):
        """
        Get categories for the list
        """
        return [FoursquareCategory(le) for le in self.getJSONObject(self.base, "categories").get("item", [])]


    def getCollaborative(self):
        """
        Whether or not the list has collaborators
        """
        return self.base.get("collaborative", [])

    def getCollaborators(self):
        """
        Get collaborators for this list
        """
        return [FoursquareCollaborator(le) for le in self.getJSONObject(self.base, "collaborators").get("items", [])]


    def getDescription(self):
        """
        The description of the list
        """
        return self.base.get("description", [])

    def getDoneCount(self):
        """
        The count of items that are done
        """
        return self.base.get("doneCount", [])

    def getEditable(self):
        """
        Whether or not the list is editable
        """
        return self.base.get("editable", [])

    def getFollowers(self):
        """
        Get the count of followers
        """
        return FoursquareFollowers(self.base.get("followers", []))

    def getFollowing(self):
        """
        Whether or not there are followers of the list
        """
        return self.base.get("following", [])

    def getId(self):
        """
        The id of the list
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
        Whether not the list is editable by others
        """
        return self.base.get("public", [])

    def getType(self):
        """
        The type of list
        """
        return self.base.get("type", [])

    def getUrl(self):
        """
        The list url
        """
        return self.base.get("url", [])

    def getUser(self):
        """
        Get the user who created this list
        """
        return FoursquareUser(self.base.get("user", []))

    def getVenueCount(self):
        """
        The venue count for this list
        """
        return self.base.get("venueCount", [])

    def getVisitedCount(self):
        """
        The count of visits
        """
        return self.base.get("visitedCount", [])

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

from temboo.outputs.Foursquare.FoursquareCategory import FoursquareCategory
from temboo.outputs.Foursquare.FoursquareCollaborator import FoursquareCollaborator
from temboo.outputs.Foursquare.FoursquareFollowers import FoursquareFollowers
from temboo.outputs.Foursquare.FoursquareItem import FoursquareItem
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser