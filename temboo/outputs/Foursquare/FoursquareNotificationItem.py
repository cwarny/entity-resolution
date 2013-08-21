# coding: utf-8

class FoursquareNotificationItem:
    """
     Contains
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCheckins(self):
        """
        The number of checkins
        """
        return self.base.get("checkins", [])

    def getImage(self):
        """
        The url for the user image
        """
        return self.base.get("image", [])

    def getInsights(self):
        """
        Get insights
        """
        return [FoursquareInsight(le) for le in self.getJSONObject(self.base, "insights").get("items", [])]


    def getScores(self):
        """
        Get the scores for this checkin
        """
        return [FoursquareScore(le) for le in self.getJSONObject(self.base, "item").get("scores", [])]


    def getLeaderboard(self):
        """
        Get the leadboard object for the authenticated user
        """
        return [FoursquareLeaderboard(le) for le in self.base.get("leaderboard", [])]


    def getMessage(self):
        """
        The notification message
        """
        return self.base.get("message", [])

    def getTotal(self):
        """
        The total number of items
        """
        return self.base.get("total", [])

    def getType(self):
        """
        The type of notification item
        """
        return self.base.get("type", [])

    def getUnreadCount(self):
        """
        The number of unread notifications
        """
        return self.base.get("unreadCount", [])

    def getUser(self):
        """
        Get the user information for this notification item
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

from temboo.outputs.Foursquare.FoursquareInsight import FoursquareInsight
from temboo.outputs.Foursquare.FoursquareLeaderboard import FoursquareLeaderboard
from temboo.outputs.Foursquare.FoursquareScore import FoursquareScore
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser