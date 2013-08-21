# coding: utf-8

class FoursquareLeaderboardItem:
    """
     Contains leaderboard items for the authenticated user
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getRank(self):
        """
        """
        return self.base.get("rank", [])

    def getLeaderboardScores(self):
        """
        Get statitics related to the leaderboard score
        """
        return FoursquareLeaderboardScores(self.base.get("scores", []))

    def getUser(self):
        """
        Get the user on this leaderboard
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

from temboo.outputs.Foursquare.FoursquareLeaderboardScores import FoursquareLeaderboardScores
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser