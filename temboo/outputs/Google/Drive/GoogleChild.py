# coding: utf-8

class GoogleChild:
    """
     A specific child reference

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getChildLink(self):
        """
        A link to the child
        """
        return self.base.get("childLink", [])

    def getId(self):
        """
        The ID of the child
        """
        return self.base.get("id", [])

    def getKind(self):
        """
        This is always drive#childReference
        """
        return self.base.get("kind", [])

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

