# coding: utf-8

class FoursquareLeaderboardScores:
    """
     Cotains leaderboard scores for the authenticated user
          
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCheckinsCount(self):
        """
        The user's total checkin count over the past 7 days
        """
        return self.base.get("checkinsCount", [])

    def getGoal(self):
        """
        If the user has never scored more than a certain number of points, then this field is returned (current value is 50)
        """
        return self.base.get("goal", [])

    def getMax(self):
        """
        The highest 7-day score the user has ever achieved
        """
        return self.base.get("max", [])

    def getRecent(self):
        """
        The user's total score over the past 7 days
        """
        return self.base.get("recent", [])

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

