# coding: utf-8

class GoogleCalendar:
    """
     Represents a Google Calendar
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDescription(self):
        """
        Description of the calendar.
        """
        return self.base.get("description", [])

    def getEtag(self):
        """
        ETag of the resource.
        """
        return self.base.get("etag", [])

    def getId(self):
        """
        Identifier of the calendar.
        """
        return self.base.get("id", [])

    def getKind(self):
        """
        Type of the resource ("calendar#calendar").
        """
        return self.base.get("kind", [])

    def getLocation(self):
        """
        Geographic location of the calendar as free-form text
        """
        return self.base.get("location", [])

    def getSummary(self):
        """
        Title of the calendar.
        """
        return self.base.get("summary", [])

    def getTimeZone(self):
        """
        The time zone of the calendar.
        """
        return self.base.get("timeZone", [])

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

