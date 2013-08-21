"""
Copyright 2012, Temboo Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http:#www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


This simple Python application demonstrates how to get started building apps 
that integrate Last.fm and Google Calendar. To run the demo, you'll need a 
Temboo account, a Last.fm API Key, and oAuth 2.0 credentials for Google 
Calendar.

The demo uses Temboo SDK functions to retrieve an XML list of Last.fm "events"
associated with a list of your favorite bands, extracts the artist name, 
venue, city, and date for each event item, and adds an event to your Google 
Calendar if the event occurs in the city that you specify.

@author Joaquin Maguire
"""

from xml.etree import ElementTree

from temboo.core.session import TembooSession
from temboo.Library.Google import Calendar
from temboo.Library.LastFm import Artist

"""
UPDATE THE VALUES OF THESE CONSTANTS WITH YOUR OWN CREDENTIALS
"""

# Use this constant to specify your city. If events are found in this city, 
# it will be added to your Google Calendar.
MY_CITY = "New York"

# For this constant, specify a list of band names that may have events on 
# Last.fm that you want to add to Google Calendar.
BAND_NAMES = ["First Aid Kit", "Slow Club", "Beach House"]

# Use this constant to define your Last.fm API KEY.
# You can apply for an API Key by going here: http:#www.last.fm/api/account.
# (Replace with your own Last.fm API Key.)
LAST_FM_API_KEY = "YOUR LAST.FM API KEY"

# Use this constant to define your Google oAuth 2.0 credentials.
# If you don't already have the oAuth credentials associated with your Google 
# account, login to your Google account, create a project and generate your 
# oAuth 2.0 ClientID and ClientSecret at https:#code.google.com/apis/console/.
# After doing that, use Google's oAuth playground to generate your AccessToken
# and RefreshToken here: https:#code.google.com/oauthplayground/.
GOOGLE_CLIENT_ID = "YOUR GOOGLE CLIENT ID"
GOOGLE_CLIENT_SECRET = "YOUR GOOGLE CLIENT SECRET"
GOOGLE_ACCESS_TOKEN = "YOUR GOOGLE ACCESS TOKEN"
GOOGLE_REFRESH_TOKEN = "YOUR GOOGLE REFRESH TOKEN"

# Set your calendar name here. Make sure you provide the name of an existing
# Google calendar. Note, if there are multiple calendars with the same name, 
# the first one returned will be used.
GOOGLE_CALENDAR_NAME = "MyConcerts"

# Use these constants to define the set of credentials that will be used to 
# connect with Temboo. (Replace with your own Temboo Application Key.)
TEMBOO_ACCOUNT_NAME = "YOUR ACCOUNT NAME"
TEMBOO_APPLICATIONKEY_NAME = "YOUR TEMBOO APP KEY NAME"
TEMBOO_APPLICATIONKEY = "YOUR TEMBOO APP KEY"

"""
END CONSTANTS: NOTHING BELOW THIS POINT SHOULD NEED TO BE CHANGED
"""

# For the simplest possible conversion, let's go ahead and enumerate dates.
DATELIST = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", 
            "Oct", "Nov", "Dec"]

class LastFMtoGoogleCal:

    def __init__(self):
        """ Set up a Temboo session. """
        self.session = TembooSession(TEMBOO_ACCOUNT_NAME, TEMBOO_APPLICATIONKEY_NAME, 
                                TEMBOO_APPLICATIONKEY)

        # Has the user's Google Calendar been modified within this instance's
        # lifetime?
        self.modified = False
        # ID of calendar to which we want to add events.
        self.calendar_id = None

    def get_target_calendar(self):
        """
        Store the ID of the target calendar.
        """
        choreo = Calendar.SearchCalendarsByName(self.session)
        inputs = Calendar.SearchCalendarsByNameInputSet()
        inputs.set_AccessToken(GOOGLE_ACCESS_TOKEN)
        inputs.set_CalendarName(GOOGLE_CALENDAR_NAME)
        inputs.set_ClientID(GOOGLE_CLIENT_ID)
        inputs.set_ClientSecret(GOOGLE_CLIENT_SECRET)
        inputs.set_RefreshToken(GOOGLE_REFRESH_TOKEN)

        results = choreo.execute_with_results(inputs)
        self.calendar_id = results.get_CalendarId()

    def get_concert_list(self):
        """
        Find local events associated with bands that you like.
        """
        for band in BAND_NAMES:
            # Set up event-retrieving choreo.
            choreo = Artist.GetEvents(self.session)
            inputs = Artist.GetEventsInputSet()
            inputs.set_APIKey(LAST_FM_API_KEY)
            inputs.set_Artist(band)
            inputs.set_Limit("50")

            # Retrieve event list for the current artist.
            artist_events = choreo.execute_with_results(inputs)
            print("Retrieved xml listing of eventf from", band, 
                  "from Last.fm.")
            event_xml = artist_events.get_Response().encode("utf-8")
            event_tree = ElementTree.fromstring(event_xml)
            event_list = event_tree.getchildren()[0].findall("event")

            for event in event_list:
                city = event.find("venue").find("location").find("city").text
                if city.find(MY_CITY) >= 0:
                    print("Found an event for", band, "in", MY_CITY)
                    venue_name = event.find("venue").find("name").text
                    date_string = event.find("startDate").text
                    self.create_calendar_event(band, venue_name, date_string)


    def create_calendar_event(self, artist_name, venue_name, date_string):
        """
        Add an event to your Google calendar.
        """
        choreo = Calendar.CreateEvent(self.session)
        inputs = choreo.new_input_set()

        # Separate date_string into the format expected by Google Calendar.
        date_components = date_string.split()
        formatted_date = "{0}-{1}-{2}".format(date_components[3],
                                str(DATELIST.index(date_components[2]) + 1),
                                date_components[1])
        formatted_time = date_components[4]

        inputs.set_AccessToken(GOOGLE_ACCESS_TOKEN)
        inputs.set_ClientID(GOOGLE_CLIENT_ID)
        inputs.set_ClientSecret(GOOGLE_CLIENT_SECRET)
        inputs.set_RefreshToken(GOOGLE_REFRESH_TOKEN)
        inputs.set_CalendarID(self.calendar_id)
        inputs.set_EventTitle(artist_name)
        inputs.set_EventDescription(venue_name)
        inputs.set_StartDate(formatted_date)
        inputs.set_StartTime(formatted_time)
        # Since this is a notification, go ahead and set the duration to 0.
        inputs.set_EndDate(formatted_date)
        inputs.set_EndTime(formatted_time)

        try:
            choreo.execute_with_results(inputs)
            print("Created event for ", artist_name, "on", formatted_date,
                  "at", formatted_time)
            self.modified = True
        except Exception, e:
            print("An error occurred trying to create a calendar event for",
                  artist_name)
            raise e

    def main(self):
        """
        Idenfity target calendar and upload events. Report if no events were 
        found.
        """
        self.get_target_calendar()
        self.get_concert_list()
        if not self.modified:
            print("We were unable to find any events for specified bands in",
                  MY_CITY)

if __name__ == "__main__":
    instance = LastFMtoGoogleCal()
    instance.main()















