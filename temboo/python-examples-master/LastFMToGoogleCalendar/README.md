
###USING THE TEMBOO SDK: SEARCH LAST.FM ARTIST EVENTS AND ADD THEM TO YOUR GOOGLE CALENDAR (Python)

This example is a working Python application that uses the Temboo SDK to retrieve a list of Last.fm events for bands that you specify,
and creates new events in your Google Calendar when they are located in your city. The application:

 * Allows you to specify a list of band names that will be searched on Last.fm for events
 * Allows you to specify the city that you're in
 * Retrieves the set of Last.fm events for each band you specified and iterates over the list of results 
 * Adds the event to your Google Calendar if the artist event is in your city

###TO RUN THIS EXAMPLE:

 * Sign up for a free Temboo account (if you don't already have one) and Download the Temboo Python SDK
at https://www.temboo.com/download. Add the SDK as a library to your Java project. You can find instructions
for this process on the Temboo site, under "getting started" (https://www.temboo.com/public/support/getting-started).

 * Create a Last.fm account (if you don't already have one) and apply for an API Key by going here: http://www.last.fm/api/account.

 * Create a Google account (if you don't already have one). If you don't have the oAuth 2.0 credentials associated with your Google account, 
login to your Google account, create a project and generate your oAuth 2.0 ClientID and ClientSecret here https://code.google.com/apis/console/. 
After doing that, use Google's oAuth playground to generate your AccessToken and RefreshToken here: https://code.google.com/oauthplayground/

 * Edit the Python code to contain your Temboo, Last.fm, and Google Calendar credentials. 

 * Run it!

###ABOUT TEMBOO

The Temboo SDK Library allows you to implement complex interactions with 3rd party services 
without worrying about the specific syntax of a 3rd-party API, by providing simple, 
native-language functions that trigger Temboo choreos. Temboo choreos are reusable
code snippets that can do almost anything, from updating your status on Facebook, to creating
a new Amazon RDS DB instance, to checking the weather in your neighborhood. 
