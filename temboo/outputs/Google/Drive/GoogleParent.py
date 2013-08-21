# coding: utf-8

class GoogleParent:
    """
     An object containing a parent resource

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getId(self):
        """
        The id of the folder
        """
        return self.base.get("id", [])

    def getIsRoot(self):
        """
        Whether or not this folder is the root
        """
        return self.base.get("isRoot", [])

    def getKind(self):
        """
        The type of resource
        """
        return self.base.get("kind", [])

    def getParentLink(self):
        """
        The link to the parent
        """
        return self.base.get("parentLink", [])

    def getSelfLink(self):
        """
        A link back to this reference
        """
        return self.base.get("selfLink", [])

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

