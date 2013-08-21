# coding: utf-8

class GoogleStart:
    """
     The (inclusive) start time of the event. For a recurring event, this is the start time of the first instance.
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDateTime(self):
        """
        The time, as a combined date-time value (formatted according to RFC 3339). A time zone offset is required unless a time zone is explicitly specified in 'timeZone'.
        """
        return self.base.get("dateTime", [])

    def getTimeZone(self):
        """
        The name of the time zone in which the time is specified (e.g. "Europe/Zurich"). Optional. The default is the time zone of the calendar.
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

