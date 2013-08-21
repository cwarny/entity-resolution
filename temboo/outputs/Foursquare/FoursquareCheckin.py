# coding: utf-8

class FoursquareCheckin:
    """
     A checkin object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBadges(self):
        return [FoursquareBadge(le) for le in self.getJSONObject(self.base, "badges").get("items", [])]


    def getComments(self):
        return [FoursquareComment(le) for le in self.getJSONObject(self.base, "comments").get("items", [])]


    def getCreatedAt(self):
        """
        The epoch timestamp for when the checkin was created
        """
        return self.base.get("createdAt", [])

    def getId(self):
        """
        The id the checkin
        """
        return self.base.get("id", [])

    def getLike(self):
        """
        Whether or not the checkin has been liked
        """
        return self.base.get("like", [])

    def getLikes(self):
        """
        Get likes for this checkin
        """
        return FoursquareLikes(self.base.get("likes", []))

    def getOverlaps(self):
        """
        Get information about overlapping checkins
        """
        return [FoursquareOverlap(le) for le in self.getJSONObject(self.base, "overlaps").get("items", [])]


    def getPhotos(self):
        """
        Get photos for this checkin
        """
        return [FoursquarePhoto(le) for le in self.getJSONObject(self.base, "photos").get("items", [])]


    def getPosts(self):
        """
        Get the posts for this checkin. May not be present.
        """
        return [FoursquarePost(le) for le in self.getJSONObject(self.base, "posts").get("items", [])]


    def getScores(self):
        """
        Get scores for this checkin
        """
        return [FoursquareScore(le) for le in self.getJSONObject(self.base, "score").get("scores", [])]


    def getShout(self):
        """
        The message from check-in
        """
        return self.base.get("shout", [])

    def getSource(self):
        """
        Get the source information for the app that created the checkin
        """
        return FoursquareSource(self.base.get("source", []))

    def getTimeZone(self):
        """
        The timezone associated with this checkin
        """
        return self.base.get("timeZone", [])

    def getTimeZoneOffset(self):
        """
        A string representation of the time zone where this check-in occurred
        """
        return self.base.get("timeZoneOffset", [])

    def getType(self):
        """
        The type of foursquare object. One of checkin, shout, or venueless.
        """
        return self.base.get("type", [])

    def getUser(self):
        """
        Get the user associated with this checkin
        """
        return FoursquareUser(self.base.get("user", []))

    def getVenue(self):
        """
        Get the venue for this checkin
        """
        return FoursquareVenue(self.base.get("venue", []))

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

from temboo.outputs.Foursquare.FoursquareBadge import FoursquareBadge
from temboo.outputs.Foursquare.FoursquareComment import FoursquareComment
from temboo.outputs.Foursquare.FoursquareLikes import FoursquareLikes
from temboo.outputs.Foursquare.FoursquareOverlap import FoursquareOverlap
from temboo.outputs.Foursquare.FoursquarePhoto import FoursquarePhoto
from temboo.outputs.Foursquare.FoursquarePost import FoursquarePost
from temboo.outputs.Foursquare.FoursquareScore import FoursquareScore
from temboo.outputs.Foursquare.FoursquareSource import FoursquareSource
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser
from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue