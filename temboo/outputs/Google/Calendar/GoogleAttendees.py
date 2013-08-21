# coding: utf-8

class GoogleAttendees:
    """
     The attendees of the event.
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEmail(self):
        """
        The attendee's email address, if available. This field must be present when adding an attendee.
        """
        return self.base.get("email", [])

    def getResponseStatus(self):
        """
        The attendee's response status: "needsAction" - The attendee has not responded to the invitation, "declined" - The attendee has declined the invitation, "tentative" - The attendee has tentatively accepted the invitation, "accepted" - The attendee has accepted the invitation.
        """
        return self.base.get("responseStatus", [])

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

