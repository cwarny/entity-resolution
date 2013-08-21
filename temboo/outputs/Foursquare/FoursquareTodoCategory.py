# coding: utf-8

class FoursquareTodoCategory:
    """
     Contains categories of todos associated with the venue
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getIcon(self):
        """
        The icon for the todo category
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        The id of the todo category
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of the todo category
        """
        return self.base.get("name", [])

    def getPluralName(self):
        """
        The plural name of the todo category
        """
        return self.base.get("pluralName", [])

    def getShortName(self):
        """
        The short name of the todo category
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

