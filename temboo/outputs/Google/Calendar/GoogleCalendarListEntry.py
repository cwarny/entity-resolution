# coding: utf-8
from temboo.outputs.Google.Calendar.GoogleCalendar import GoogleCalendar

class GoogleCalendarListEntry(GoogleCalendar):
    """
     Represents a Google Calendar List Entry
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAccessRole(self):
        """
        The effective access role that the authenticated user has on the calendar: "freeBusyReader" - Provides read access to free/busy information, "reader" - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden, "writer" - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible, "owner" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs.
        """
        return self.base.get("accessRole", [])

    def getBackgroundColor(self):
        """
        The main color of the calendar in the format '#0088aa'. This property supersedes the index-based colorId property
        """
        return self.base.get("backgroundColor", [])

    def getColorId(self):
        """
        The color of the calendar. This is an ID referring to an entry in the "calendar" section of the colors definition (see the "colors" endpoint).
        """
        return self.base.get("colorId", [])

    def getDefaultReminders(self):
        """
        The default reminders that the authenticated user has for this calendar.
        """
        return [GoogleDefaultReminders(le) for le in self.base.get("defaultReminders", [])]


    def getForegroundColor(self):
        """
        The foreground color of the calendar in the format '#ffffff'. This property supersedes the index-based colorId property.
        """
        return self.base.get("foregroundColor", [])

    def getKind(self):
        """
        Type of the resource ("calendar#calendarListEntry").
        """
        return self.base.get("kind", [])

    def getSelected(self):
        """
        Whether the calendar content shows up in the calendar UI.
        """
        return self.base.get("selected", [])

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