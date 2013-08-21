# coding: utf-8

class FacebookPhotoTag:
    """
     A photo objects including tagged users and their positions in this photo

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getComments(self):
        """
        Get comments for this photo object
        """
        return [FacebookComment(le) for le in self.getJSONObject(self.base, "comments").get("data", [])]


    def getCreatedTime(self):
        """
        The time the photo was initially published in ISO-8601 format
        """
        return self.base.get("created_time", [])

    def getFrom(self):
        """
        The profile (user or page) that posted this photo
        """
        return FacebookFrom(self.base.get("from", []))

    def getHeight(self):
        """
        The height of the photo in pixels
        """
        return self.base.get("height", [])

    def getIcon(self):
        """
        The icon that Facebook displays when photos are published to the Feed
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        The id of the photo
        """
        return self.base.get("id", [])

    def getImages(self):
        """
        Get a representation fo this photo
        """
        return [FacebookImage(le) for le in self.base.get("images", [])]


    def getLikes(self):
        """
        The users that have liked this photo
        """
        return [FacebookLike(le) for le in self.getJSONObject(self.base, "likes").get("data", [])]


    def getLink(self):
        """
        A link to the photo
        """
        return self.base.get("link", [])

    def getName(self):
        """
        The user provided caption given to this photo
        """
        return self.base.get("name", [])

    def getPicture(self):
        """
        The thumbnail-sized source of the photo
        """
        return self.base.get("picture", [])

    def getPosition(self):
        """
        The position of this photo in the album
        """
        return self.base.get("position", [])

    def getSource(self):
        """
        The source image of the photo
        """
        return self.base.get("source", [])

    def getTags(self):
        """
        Get a tag in this photo
        """
        return [FacebookTag(le) for le in self.getJSONObject(self.base, "tags").get("data", [])]


    def getUpdatedTime(self):
        """
        The last time the photo or its caption was updated in ISO-8601 format
        """
        return self.base.get("updated_time", [])

    def getWidth(self):
        """
        The width of the photo in pixels
        """
        return self.base.get("width", [])

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

from temboo.outputs.Facebook.FacebookComment import FacebookComment
from temboo.outputs.Facebook.FacebookFrom import FacebookFrom
from temboo.outputs.Facebook.FacebookImage import FacebookImage
from temboo.outputs.Facebook.FacebookLike import FacebookLike
from temboo.outputs.Facebook.FacebookTag import FacebookTag