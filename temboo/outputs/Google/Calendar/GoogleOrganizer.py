# coding: utf-8

class GoogleOrganizer:
    """
     The organizer of the event. If the organizer is also an attendee, this is indicated with a separate entry in 'attendees' with the 'organizer' field set to True.
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDisplayName(self):
        """
        The organizer's name, if available.
        """
        return self.base.get("displayName", [])

    def getEmail(self):
        """
        The organizer's email address, if available.
        """
        return self.base.get("email", [])

    def getSelf(self):
        """
        Whether the organizer corresponds to the calendar on which this copy of the event appears.  The default is False.
        """
        return self.base.get("self", [])

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

