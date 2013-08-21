# coding: utf-8

class FacebookEvent:
    """
     An object representing an event on Facebook

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEndTime(self):
        """
        The date and time the event will end
        """
        return self.base.get("end_time", [])

    def getId(self):
        """
        The id of the event
        """
        return self.base.get("id", [])

    def getLocation(self):
        """
        The location of the event
        """
        return self.base.get("location", [])

    def getName(self):
        """
        The name of the event
        """
        return self.base.get("name", [])

    def getRsvpStatus(self):
        """
        The RSVP status for the authenticated user
        """
        return self.base.get("rsvp_status", [])

    def getStartTime(self):
        """
        The date and time that the even will begin
        """
        return self.base.get("start_time", [])

    def getTimezone(self):
        """
        The timezone for the event
        """
        return self.base.get("timezone", [])

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

