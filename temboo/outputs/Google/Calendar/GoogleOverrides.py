# coding: utf-8

class GoogleOverrides:
    """
     f the event doesn't use the default reminders, this lists the reminders specific to the event, or, if not set, indicates that no reminders are set for this event.
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getMethod(self):
        """
        The method used by this reminder: "email" - Reminders are sent via email, "sms" - Reminders are sent via SMS, "popup" - Reminders are sent via a UI popup.
        """
        return self.base.get("method", [])

    def getMinutes(self):
        """
        Number of minutes before the start of the event when the reminder should trigger.
        """
        return self.base.get("minutes", [])

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

