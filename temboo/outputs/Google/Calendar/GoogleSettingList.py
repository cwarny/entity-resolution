# coding: utf-8

class GoogleSettingList:
    """
     A listing of all Google Calendar Settings

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEtag(self):
        """
        ETag of the resource.
        """
        return self.base.get("etag", [])

    def getSettings(self):
        """
        A list of all Google Calendar Settings.
        """
        return [GoogleSetting(le) for le in self.base.get("items", [])]


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

from temboo.outputs.Google.Calendar.GoogleSetting import GoogleSetting