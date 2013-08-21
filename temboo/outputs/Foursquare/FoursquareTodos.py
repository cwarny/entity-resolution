# coding: utf-8

class FoursquareTodos:
    """
     Contains information about a todo list for the venue
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCanonicalUrl(self):
        """
        The canonical url for the todo
        """
        return self.base.get("canonicalUrl", [])

    def getTodoCategories(self):
        return [FoursquareTodoCategory(le) for le in self.getJSONObject(self.getJSONObject(self.base, "categories"), "items").get("category", [])]


    def getCollaborative(self):
        """
        Whether or not other users have edited this todo
        """
        return self.base.get("collaborative", [])

    def getCollaborators(self):
        """
        Get collaborators for the todo item
        """
        return [FoursquareCollaborator(le) for le in self.getJSONObject(self.base, "collaborators").get("items", [])]


    def getDescription(self):
        """
        A description of the todo
        """
        return self.base.get("description", [])

    def getDoneCount(self):
        """
        The count of todos marked done
        """
        return self.base.get("doneCount", [])

    def getEditable(self):
        """
        Whether or not this todo is editable
        """
        return self.base.get("editable", [])

    def getFollowers(self):
        """
        Get the number of followers for this to do
        """
        return FoursquareFollowers(self.base.get("followers", []))

    def getFollowing(self):
        """
        Whether or not the acting user is following the list
        """
        return self.base.get("following", [])

    def getId(self):
        """
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of the todo item
        """
        return self.base.get("name", [])

    def getPublic(self):
        """
        Whether or not this todo is public
        """
        return self.base.get("public", [])

    def getType(self):
        """
        The type of todo
        """
        return self.base.get("type", [])

    def getUrl(self):
        """
        The url of the todo
        """
        return self.base.get("url", [])

    def getUser(self):
        """
        The user that created the todo for this venue
        """
        return FoursquareUser(self.base.get("user", []))

    def getVenueCount(self):
        """
        The venue count for the todo
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

from temboo.outputs.Foursquare.FoursquareCollaborator import FoursquareCollaborator
from temboo.outputs.Foursquare.FoursquareFollowers import FoursquareFollowers
from temboo.outputs.Foursquare.FoursquareTodoCategory import FoursquareTodoCategory
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser