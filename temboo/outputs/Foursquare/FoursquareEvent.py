# coding: utf-8

class FoursquareEvent:
    """
     Contains details about venue events
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAllDay(self):
        """
        Whether or not this is an all day event
        """
        return self.base.get("allDay", [])

    def getCategories(self):
        """
        Get categories for this event
        """
        return [FoursquareCategory(le) for le in self.base.get("categories", [])]


    def getDate(self):
        """
        The date of the even as an epoch timestamp
        """
        return self.base.get("date", [])

    def getForeignIds(self):
        """
        Get foreign ids
        """
        return [FoursquareForeignIds(le) for le in self.getJSONObject(self.base, "foreignIds").get("items", [])]


    def getHereNow(self):
        """
        Get the people at this event now
        """
        return FoursquareHereNow(self.base.get("hereNow", []))

    def getId(self):
        """
        The event id
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of the event
        """
        return self.base.get("name", [])

    def getStats(self):
        """
        Get stats for the event
        """
        return FoursquareStats(self.base.get("stats", []))

    def getTimeZone(self):
        """
        The event timezone
        """
        return self.base.get("timeZone", [])

    def getUrl(self):
        """
        The url for the event
        """
        return self.base.get("url", [])

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
from temboo.outputs.Foursquare.FoursquareForeignIds import FoursquareForeignIds
from temboo.outputs.Foursquare.FoursquareHereNow import FoursquareHereNow
from temboo.outputs.Foursquare.FoursquareStats import FoursquareStats