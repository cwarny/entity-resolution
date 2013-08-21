# coding: utf-8

class FoursquareCategory:
    """
      Contains information about the categories that have been applied to this foursquare object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getIcon(self):
        """
        The icon for this category
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        The id of the category
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of the category
        """
        return self.base.get("name", [])

    def getParents(self):
        """
        """
        return [le for le in self.base.get("parents", [])]


    def getPluralName(self):
        """
        The plural name for the category
        """
        return self.base.get("pluralName", [])

    def getPrimary(self):
        """
        Whether or not this category is tagged as the primary category
        """
        return self.base.get("primary", [])

    def getShortName(self):
        """
        The short name for the category
        """
        return self.base.get("shortName", [])

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

