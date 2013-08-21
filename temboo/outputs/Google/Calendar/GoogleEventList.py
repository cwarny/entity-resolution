# coding: utf-8

class GoogleEventList:
    """
     A listing of Google Calendar Events

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAccessRole(self):
        """
        The user's access role for this calendar: "none" - The user has no access, "freeBusyReader" - The user has read access to free/busy information, "reader" - The user has read access to the calendar. Private events will appear to users with reader access, but event details will be hidden, "writer" - The user has read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible, "owner" - The user has ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs.
        """
        return self.base.get("accessRole", [])

    def getDefaultReminders(self):
        """
        """
        return [GoogleDefaultReminders(le) for le in self.base.get("defaultReminders", [])]


    def getDescription(self):
        """
        Description of the calendar.
        """
        return self.base.get("description", [])

    def getEtag(self):
        """
        ETag of the collection.
        """
        return self.base.get("etag", [])

    def getEvents(self):
        """
        A list of Google Calendar Events.
        """
        return [GoogleEvent(le) for le in self.base.get("items", [])]


    def getKind(self):
        """
        Type of the collection ("calendar#events").
        """
        return self.base.get("kind", [])

    def getSummary(self):
        """
        Title of the calendar
        """
        return self.base.get("summary", [])

    def getTimeZone(self):
        """
        The time zone of the calendar.
        """
        return self.base.get("timeZone", [])

    def getUpdated(self):
        """
        Last modification time of the calendar (as a RFC 3339 timestamp)
        """
        return self.base.get("updated", [])

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

from temboo.outputs.Google.Calendar.GoogleDefaultReminders import GoogleDefaultReminders
from temboo.outputs.Google.Calendar.GoogleEvent import GoogleEvent