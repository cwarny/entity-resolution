# coding: utf-8

class FoursquareVenue:
    """
     An containing information about foursquare venue

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBeenHere(self):
        """
        Contains count of the number of times the acting user has been here. Absent if there is no acting user
        """
        return FoursquareBeenHere(self.base.get("beenHere", []))

    def getCanonicalUrl(self):
        """
        """
        return self.base.get("canonicalUrl", [])

    def getCategories(self):
        """
        Categories that have been applied to this venue
        """
        return [FoursquareCategory(le) for le in self.base.get("categories", [])]


    def getContact(self):
        """
        An object containing twitter, phone, and formattedPhone of the user or venue contact. All can be present, and all can be absent from the response.
        """
        return FoursquareContact(self.base.get("contact", []))

    def getCreatedAt(self):
        """
        The date the venue was created in epoch format
        """
        return self.base.get("createdAt", [])

    def getHasMenu(self):
        """
        Whether or not a menu is available for this venue
        """
        return self.base.get("hasMenu", [])

    def getHereNow(self):
        """
        Contains information about who is here now
        """
        return FoursquareHereNow(self.base.get("hereNow", []))

    def getHours(self):
        """
        Get the hours that the venue is open
        """
        return FoursquareHours(self.base.get("hours", []))

    def getId(self):
        """
        The id of the venue
        """
        return self.base.get("id", [])

    def getLikes(self):
        """
        The count of users who have liked this object, and groups containing any friends and others who have liked it
        """
        return FoursquareLikes(self.base.get("likes", []))

    def getListed(self):
        """
        A grouped response of lists that contain this venue
        """
        return FoursquareListed(self.base.get("listed", []))

    def getLocation(self):
        """
        An object containing the location information for the venue
        """
        return FoursquareLocation(self.base.get("location", []))

    def getMayor(self):
        """
        An object containing information about the mayor of the venue
        """
        return FoursquareMayor(self.base.get("mayor", []))

    def getMenu(self):
        """
        An object containing url and mobileUrl that display the menu information for this venue
        """
        return FoursquareMenu(self.base.get("menu", []))

    def getName(self):
        """
        The name of the venue
        """
        return self.base.get("name", [])

    def getPageUpdates(self):
        """
        Get the count of page updates
        """
        return FoursquarePageUpdates(self.base.get("pageUpdates", []))

    def getPhotoGroups(self):
        """
        Contain information about photos for this venue
        """
        return [FoursquarePhotoGroup(le) for le in self.getJSONObject(self.base, "photos").get("groups", [])]


    def getPrice(self):
        """
        Get price information for this venue
        """
        return FoursquarePrice(self.base.get("price", []))

    def getRating(self):
        """
        The venue rating
        """
        return self.base.get("rating", [])

    def getShortUrl(self):
        """
        The short url for the venue
        """
        return self.base.get("shortUrl", [])

    def getSpecials(self):
        """
        Contains information about specials offered by the venue
        """
        return [FoursquareSpecial(le) for le in self.base.get("specials", [])]


    def getStats(self):
        """
        Contains statistics for the venue including checkinsCount, tipCount, and userCount
        """
        return FoursquareStats(self.base.get("stats", []))

    def getTags(self):
        """
        Contains tags for this venue
        """
        return [le for le in self.base.get("tags", [])]


    def getTimeZone(self):
        """
        The timezone for this venue
        """
        return self.base.get("timeZone", [])

    def getTipGroups(self):
        """
        Get tips from others and friends
        """
        return [FoursquareTipGroup(le) for le in self.getJSONObject(self.base, "tips").get("groups", [])]


    def getTodos(self):
        return FoursquareTodos(self.base.get("todos", []))

    def getUrl(self):
        """
        The url for this venue
        """
        return self.base.get("url", [])

    def getVerified(self):
        """
        Whether or not the venue has been verified
        """
        return self.base.get("verified", [])

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

from temboo.outputs.Foursquare.FoursquareBeenHere import FoursquareBeenHere
from temboo.outputs.Foursquare.FoursquareCategory import FoursquareCategory
from temboo.outputs.Foursquare.FoursquareContact import FoursquareContact
from temboo.outputs.Foursquare.FoursquareHereNow import FoursquareHereNow
from temboo.outputs.Foursquare.FoursquareHours import FoursquareHours
from temboo.outputs.Foursquare.FoursquareLikes import FoursquareLikes
from temboo.outputs.Foursquare.FoursquareListed import FoursquareListed
from temboo.outputs.Foursquare.FoursquareLocation import FoursquareLocation
from temboo.outputs.Foursquare.FoursquareMayor import FoursquareMayor
from temboo.outputs.Foursquare.FoursquareMenu import FoursquareMenu
from temboo.outputs.Foursquare.FoursquarePageUpdates import FoursquarePageUpdates
from temboo.outputs.Foursquare.FoursquarePhotoGroup import FoursquarePhotoGroup
from temboo.outputs.Foursquare.FoursquarePrice import FoursquarePrice
from temboo.outputs.Foursquare.FoursquareSpecial import FoursquareSpecial
from temboo.outputs.Foursquare.FoursquareStats import FoursquareStats
from temboo.outputs.Foursquare.FoursquareTipGroup import FoursquareTipGroup
from temboo.outputs.Foursquare.FoursquareTodos import FoursquareTodos