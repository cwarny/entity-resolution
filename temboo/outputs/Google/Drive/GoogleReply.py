# coding: utf-8

class GoogleReply:
    """
     An object representing a reply to a comment

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

    def getContent(self):
        """
        The plain text content used to create this reply
        """
        return self.base.get("content", [])

    def getCreatedDate(self):
        """
        The date when this reply was first created (formatted RFC 3339 timestamp)
        """
        return self.base.get("createdDate", [])

    def getDeleted(self):
        """
        Whether this reply has been deleted
        """
        return self.base.get("deleted", [])

    def getHtmlContent(self):
        """
        HTML formatted content for this reply
        """
        return self.base.get("htmlContent", [])

    def getKind(self):
        """
        This is always drive#commentReply
        """
        return self.base.get("kind", [])

    def getModifiedDate(self):
        """
        The date when this reply was last modified (formatted RFC 3339 timestamp)
        """
        return self.base.get("modifiedDate", [])

    def getReplyId(self):
        """
        The ID of the reply
        """
        return self.base.get("replyId", [])

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