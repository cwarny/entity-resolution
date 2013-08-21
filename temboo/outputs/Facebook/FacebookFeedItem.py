# coding: utf-8

class FacebookFeedItem:
    """
     An item in a user's feed

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getActions(self):
        """
        Get the action link and name for the feed item
        """
        return [FacebookAction(le) for le in self.base.get("actions", [])]


    def getApplication(self):
        """
        Get the application that created this post
        """
        return FacebookApplication(self.base.get("application", []))

    def getCaption(self):
        """
        The feed item caption
        """
        return self.base.get("caption", [])

    def getComments(self):
        """
        The comment for this feed item
        """
        return [FacebookComment(le) for le in self.getJSONObject(self.base, "comments").get("data", [])]


    def getCreatedTime(self):
        """
        The date and time the feed item was created in ISO-8601 format
        """
        return self.base.get("created_time", [])

    def getFrom(self):
        """
        Get the user that created this feed item
        """
        return FacebookFrom(self.base.get("from", []))

    def getIcon(self):
        """
        The URL for the icon image
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        The id of the feed item
        """
        return self.base.get("id", [])

    def getLikes(self):
        """
        The users that liked this feed item
        """
        return [FacebookLike(le) for le in self.getJSONObject(self.base, "likes").get("data", [])]


    def getLink(self):
        """
        Link to the page on Facebook
        """
        return self.base.get("link", [])

    def getMessage(self):
        """
        The message text for the feed item
        """
        return self.base.get("message", [])

    def getName(self):
        """
        The Page's name
        """
        return self.base.get("name", [])

    def getPicture(self):
        """
        The source url for a picture in the feed
        """
        return self.base.get("picture", [])

    def getPlace(self):
        """
        A place associated with this feed item
        """
        return FacebookPlace(self.base.get("place", []))

    def getPrivacy(self):
        """
        The privacy setting for this feed item
        """
        return FacebookPrivacy(self.base.get("privacy", []))

    def getStatusType(self):
        """
        The type of status
        """
        return self.base.get("status_type", [])

    def getStory(self):
        """
        The text of stories not intentionally generated by users
        """
        return self.base.get("story", [])

    def getType(self):
        """
        The type of feed item
        """
        return self.base.get("type", [])

    def getUpdatedTime(self):
        """
        The last updated time for the feed
        """
        return self.base.get("updated_time", [])

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

from temboo.outputs.Facebook.FacebookAction import FacebookAction
from temboo.outputs.Facebook.FacebookApplication import FacebookApplication
from temboo.outputs.Facebook.FacebookComment import FacebookComment
from temboo.outputs.Facebook.FacebookFrom import FacebookFrom
from temboo.outputs.Facebook.FacebookLike import FacebookLike
from temboo.outputs.Facebook.FacebookPlace import FacebookPlace
from temboo.outputs.Facebook.FacebookPrivacy import FacebookPrivacy