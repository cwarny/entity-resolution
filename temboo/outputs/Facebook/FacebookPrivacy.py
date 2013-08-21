# coding: utf-8

class FacebookPrivacy:
    """
     An object containing the privacy settings of the graph object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAllow(self):
        """
        The allow field for the privacy setting
        """
        return self.base.get("allow", [])

    def getDeny(self):
        """
        The deny field for the privacy setting
        """
        return self.base.get("deny", [])

    def getDescription(self):
        """
        The description field for the privacy setting
        """
        return self.base.get("description", [])

    def getFriends(self):
        """
        The friends field for the privacy setting
        """
        return self.base.get("friends", [])

    def getNetworks(self):
        """
        The networks field for the privacy setting
        """
        return self.base.get("networks", [])

    def getValue(self):
        """
        The value field for the privacy setting
        """
        return self.base.get("value", [])

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

