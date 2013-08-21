# coding: utf-8

class GoogleUserPermission:
    """
     An object containing a permission resource

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEtag(self):
        """
        The ETag of the permission
        """
        return self.base.get("etag", [])

    def getId(self):
        """
        The ID of the permission
        """
        return self.base.get("id", [])

    def getKind(self):
        """
        The type of resource (this is always drive#permission)
        """
        return self.base.get("kind", [])

    def getRole(self):
        """
        The primary role for this user. Allowed values are: owner, reader, writer
        """
        return self.base.get("role", [])

    def getSelfLink(self):
        """
        A link back to this permission
        """
        return self.base.get("selfLink", [])

    def getType(self):
        """
        The account type. Allowed values are: user, group, domain, anyone
        """
        return self.base.get("type", [])

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

