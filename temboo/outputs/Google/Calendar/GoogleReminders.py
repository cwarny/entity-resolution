# coding: utf-8

class GoogleReminders:
    """
     Information about the event's reminders for the authenticated user.
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getOverrides(self):
        """
        If the event doesn't use the default reminders, this lists the reminders specific to the event, or, if not set, indicates that no reminders are set for this event.
        """
        return [GoogleOverrides(le) for le in self.base.get("overrides", [])]


    def getUseDefault(self):
        """
        Whether the default reminders of the calendar apply to the event.
        """
        return self.base.get("useDefault", [])

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

from temboo.outputs.Google.Calendar.GoogleOverrides import GoogleOverrides