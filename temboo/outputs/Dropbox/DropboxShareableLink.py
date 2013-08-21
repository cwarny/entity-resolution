# coding: utf-8

class DropboxShareableLink:
    """
     A Dropbox link to the given path. The link can be used publicly and directs to a preview page of the file. For compatibility reasons, it returns the link's expiration date in Dropbox's usual date format. All links are currently set to expire far enough in the future so that expiration is effectively not an issue.

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getExpires(self):
        """
        timestamp of when this link expires
        """
        return self.base.get("expires", [])

    def getUrl(self):
        """
        the url to the link
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

