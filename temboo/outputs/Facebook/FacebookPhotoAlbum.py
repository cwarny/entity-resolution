# coding: utf-8

class FacebookPhotoAlbum:
    """
     An object containing information about a user's photo album

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCanUpload(self):
        """
        Determines whether the UID can upload to the album and returns true if it allowed
        """
        return self.base.get("can_upload", [])

    def getCount(self):
        """
        The number of photos in this album
        """
        return self.base.get("count", [])

    def getCoverPhoto(self):
        """
        The album cover photo ID
        """
        return self.base.get("cover_photo", [])

    def getCreatedTime(self):
        """
        The time the photo album was initially created
        """
        return self.base.get("created_time", [])

    def getFrom(self):
        """
        Get the user that the photo is from
        """
        return FacebookFrom(self.base.get("from", []))

    def getId(self):
        """
        The album ID
        """
        return self.base.get("id", [])

    def getLink(self):
        """
        A link to this album on Facebook
        """
        return self.base.get("link", [])

    def getName(self):
        """
        The title of the album
        """
        return self.base.get("name", [])

    def getPrivacy(self):
        """
        The privacy settings for the album
        """
        return self.base.get("privacy", [])

    def getType(self):
        """
        The type of the album: profile, mobile, wall, normal or album
        """
        return self.base.get("type", [])

    def getUpdatedTime(self):
        """
        The last time the photo album was updated
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

from temboo.outputs.Facebook.FacebookFrom import FacebookFrom