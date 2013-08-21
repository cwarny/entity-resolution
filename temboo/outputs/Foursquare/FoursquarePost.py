# coding: utf-8

class FoursquarePost:
    """
     Contains information about the checkin post including the id, text, timestamp, and source information

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedAt(self):
        """
        The timestamp that the post was created in epoch format
        """
        return self.base.get("createdAt", [])

    def getId(self):
        """
        The id of the post created
        """
        return self.base.get("id", [])

    def getSource(self):
        """
        Get the source for this post
        """
        return FoursquareSource(self.base.get("source", []))

    def getText(self):
        """
        The text of the post
        """
        return self.base.get("text", [])

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

from temboo.outputs.Foursquare.FoursquareSource import FoursquareSource