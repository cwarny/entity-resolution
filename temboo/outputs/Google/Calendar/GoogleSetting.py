# coding: utf-8

class GoogleSetting:
    """
     Represents a Google Calendar user property setting.
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEtag(self):
        """
        Type of the resource ("calendar#setting").
        """
        return self.base.get("etag", [])

    def getId(self):
        """
        Name of the user setting.
        """
        return self.base.get("id", [])

    def getKind(self):
        """
        Type of the resource ("calendar#setting").
        """
        return self.base.get("kind", [])

    def getValue(self):
        """
        Value of the user setting. The format of the value depends on the ID of the setting.
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

