# coding: utf-8

class GoogleComment:
    """
     An object representing a comment on a file

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAuthor(self):
        """
        Get the user who wronte this comment
        """
        return GoogleAuthor(self.base.get("author", []))

    def getCommentId(self):
        """
        The ID of the comment
        """
        return self.base.get("commentId", [])

    def getContent(self):
        """
        The plain text content used to create this comment
        """
        return self.base.get("content", [])

    def getCreatedDate(self):
        """
        The date when this comment was first created (formatted RFC 3339 timestamp)
        """
        return self.base.get("createdDate", [])

    def getDeleted(self):
        """
        Whether this comment has been deleted
        """
        return self.base.get("deleted", [])

    def getFileId(self):
        """
        The file which this comment is addressing
        """
        return self.base.get("fileId", [])

    def getFileTitle(self):
        """
        The title of the file which this comment is addressing
        """
        return self.base.get("fileTitle", [])

    def getHtmlContent(self):
        """
        HTML formatted content for this comment
        """
        return self.base.get("htmlContent", [])

    def getKind(self):
        """
        This is always drive#comment
        """
        return self.base.get("kind", [])

    def getModifiedDate(self):
        """
        The date when this comment or any of its replies were last modified (formatted RFC 3339 timestamp)
        """
        return self.base.get("modifiedDate", [])

    def getReplies(self):
        """
        Get replies for this comment
        """
        return [GoogleReply(le) for le in self.base.get("replies", [])]


    def getStatus(self):
        """
        The status of this comment (open or resolved)
        """
        return self.base.get("status", [])

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

from temboo.outputs.Google.Drive.GoogleAuthor import GoogleAuthor
from temboo.outputs.Google.Drive.GoogleReply import GoogleReply