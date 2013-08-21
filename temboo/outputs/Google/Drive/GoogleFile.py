# coding: utf-8

class GoogleFile:
    """
     A complete Google Drive file resource

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAlternateLink(self):
        """
        A link for opening the file in using a relevant Google editor or viewer
        """
        return self.base.get("alternateLink", [])

    def getCreatedDate(self):
        """
        Create time for this file (formatted ISO8601 timestamp)
        """
        return self.base.get("createdDate", [])

    def getEditable(self):
        """
        Whether the file can be edited by the current user
        """
        return self.base.get("editable", [])

    def getEmbedLink(self):
        """
        A link for embedding the file
        """
        return self.base.get("embedLink", [])

    def getEtag(self):
        """
        ETag of the file
        """
        return self.base.get("etag", [])

    def getExportLinks(self):
        """
        A Link for exporting Google Docs to specific formats
        """
        return GoogleExportLinks(self.base.get("exportLinks", []))

    def getIconLink(self):
        """
        A link to the file's icon
        """
        return self.base.get("iconLink", [])

    def getId(self):
        """
        The ID of the file
        """
        return self.base.get("id", [])

    def getKind(self):
        """
        The type of file (this is always drive#file)
        """
        return self.base.get("kind", [])

    def getLabels(self):
        return GoogleLabels(self.base.get("labels", []))

    def getLastModifyingUserName(self):
        """
        Name of the last user to modify this file. This will only be populated if a user has edited this file
        """
        return self.base.get("lastModifyingUserName", [])

    def getLastViewedByMeDate(self):
        """
        Last time this file was viewed by the user (formatted RFC 3339 timestamp)
        """
        return self.base.get("lastViewedByMeDate", [])

    def getMimeType(self):
        """
        The mimetype of the file
        """
        return self.base.get("mimeType", [])

    def getModifiedByMeDate(self):
        """
        Last time this file was modified by the user (formatted RFC 3339 timestamp)
        """
        return self.base.get("modifiedByMeDate", [])

    def getModifiedDate(self):
        """
        Last time this file was modified by anyone (formatted RFC 3339 timestamp)
        """
        return self.base.get("modifiedDate", [])

    def getOwnerNames(self):
        """
        Name(s) of the owner(s) of this file
        """
        return [le for le in self.base.get("ownerNames", [])]


    def getParents(self):
        """
        A parent folder which contain this file
        """
        return [GoogleParent(le) for le in self.base.get("parents", [])]


    def getQuotaBytesUsed(self):
        """
        The number of quota bytes used by this file
        """
        return self.base.get("quotaBytesUsed", [])

    def getSelfLink(self):
        """
        A link back to this file
        """
        return self.base.get("selfLink", [])

    def getShared(self):
        """
        Whether or not this file is shared
        """
        return self.base.get("shared", [])

    def getSharedWithMeDate(self):
        """
        Time at which this file was shared with the user (formatted RFC 3339 timestamp)
        """
        return self.base.get("sharedWithMeDate", [])

    def getThumbnailLink(self):
        """
        A link to the file's thumbnail
        """
        return self.base.get("thumbnailLink", [])

    def getTitle(self):
        """
        The title of the this file
        """
        return self.base.get("title", [])

    def getUserPermission(self):
        """
        The permissions for the authenticated user on this file.
        """
        return GoogleUserPermission(self.base.get("userPermission", []))

    def getWritersCanShare(self):
        """
        Whether writers can share the document with other users
        """
        return self.base.get("writersCanShare", [])

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

from temboo.outputs.Google.Drive.GoogleExportLinks import GoogleExportLinks
from temboo.outputs.Google.Drive.GoogleLabels import GoogleLabels
from temboo.outputs.Google.Drive.GoogleParent import GoogleParent
from temboo.outputs.Google.Drive.GoogleUserPermission import GoogleUserPermission