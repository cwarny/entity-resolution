# coding: utf-8

class FacebookGroup:
    """
     An object containing information for the groups that the authenticated user belongs to

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAdministrator(self):
        """
        Whether or not the authenticated user is the adminstrator of the group
        """
        return self.base.get("administrator", [])

    def getBookmarkOrder(self):
        """
        The bookmark order for the group
        """
        return self.base.get("bookmark_order", [])

    def getId(self):
        """
        The group id
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The group name
        """
        return self.base.get("name", [])

    def getVersion(self):
        """
        The group version
        """
        return self.base.get("version", [])

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

