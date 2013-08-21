# coding: utf-8

class FacebookVideoMetadata:
    """
     An object containing video tags and video metadata 

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedTime(self):
        """
        The time that the video was created in ISO-8601 format
        """
        return self.base.get("created_time", [])

    def getDescription(self):
        """
        The description of the video
        """
        return self.base.get("description", [])

    def getEmbedHtml(self):
        """
        The html element that may be embedded in an Web page to play the video
        """
        return self.base.get("embed_html", [])

    def getFormat(self):
        """
        Get the formats for this video
        """
        return [FacebookFormat(le) for le in self.base.get("format", [])]


    def getFrom(self):
        """
        The profile (user or page) that created the video
        """
        return FacebookFrom(self.base.get("from", []))

    def getIcon(self):
        """
        The icon that Facebook displays when video are published to the Feed
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        The id of the video
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of the video
        """
        return self.base.get("name", [])

    def getPicture(self):
        """
        The URL for the thumbnail picture for the video
        """
        return self.base.get("picture", [])

    def getSource(self):
        """
        The source url for the video
        """
        return self.base.get("source", [])

    def getVideoTags(self):
        """
        Get the tags for this video
        """
        return [FacebookVideoTag(le) for le in self.getJSONObject(self.base, "tags").get("data", [])]


    def getUpdatedTime(self):
        """
        The last time the video or video caption was updated in ISO-8601 format
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

from temboo.outputs.Facebook.FacebookFormat import FacebookFormat
from temboo.outputs.Facebook.FacebookFrom import FacebookFrom
from temboo.outputs.Facebook.FacebookVideoTag import FacebookVideoTag