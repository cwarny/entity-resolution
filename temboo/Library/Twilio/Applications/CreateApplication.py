# -*- coding: utf-8 -*-

###############################################################################
#
# CreateApplication
# Creates a new application within your account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateApplication(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateApplication Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/Applications/CreateApplication')


    def new_input_set(self):
        return CreateApplicationInputSet()

    def _make_result_set(self, result, path):
        return CreateApplicationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateApplicationChoreographyExecution(session, exec_id, path)

class CreateApplicationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateApplication
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIVersion(self, value):
        """
        Set the value of the APIVersion input for this Choreo. ((optional, string) Requests to this application's URLs will start a new TwiML session with this API version. Either 2010-04-01 or 2008-08-01. Defaults to your account's default API version.)
        """
        InputSet._set_input(self, 'APIVersion', value)
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AuthToken', value)
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((required, string) A human readable description of the new application. Maximum 64 characters.)
        """
        InputSet._set_input(self, 'FriendlyName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SmsFallbackMethod(self, value):
        """
        Set the value of the SmsFallbackMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the SmsFallbackUrl. Must be either GET or POST. Defaults to POST.)
        """
        InputSet._set_input(self, 'SmsFallbackMethod', value)
    def set_SmsFallbackURL(self, value):
        """
        Set the value of the SmsFallbackURL input for this Choreo. ((optional, string) A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl.)
        """
        InputSet._set_input(self, 'SmsFallbackURL', value)
    def set_SmsMethod(self, value):
        """
        Set the value of the SmsMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the SmsUrl. Must be either GET or POST. Defaults to POST.)
        """
        InputSet._set_input(self, 'SmsMethod', value)
    def set_SmsStatusCallback(self, value):
        """
        Set the value of the SmsStatusCallback input for this Choreo. ((optional, string) Twilio will make a POST request to this URL to pass status parameters (such as sent or failed) to your application.)
        """
        InputSet._set_input(self, 'SmsStatusCallback', value)
    def set_SmsURL(self, value):
        """
        Set the value of the SmsURL input for this Choreo. ((optional, string) The URL that Twilio should request when somebody sends an SMS to a phone number assigned to this application.)
        """
        InputSet._set_input(self, 'SmsURL', value)
    def set_StatusCallbackMethod(self, value):
        """
        Set the value of the StatusCallbackMethod input for this Choreo. ((optional, string) The HTTP method Twilio will use to make requests to the StatusCallback URL. Either GET or POST. Defaults to POST.)
        """
        InputSet._set_input(self, 'StatusCallbackMethod', value)
    def set_StatusCallback(self, value):
        """
        Set the value of the StatusCallback input for this Choreo. ((optional, string) The URL that Twilio will request to pass status parameters (such as call ended) to your application.)
        """
        InputSet._set_input(self, 'StatusCallback', value)
    def set_VoiceApplicationSID(self, value):
        """
        Set the value of the VoiceApplicationSID input for this Choreo. ((optional, string) The 34 character sid of the application Twilio should use to handle phone calls to this number.)
        """
        InputSet._set_input(self, 'VoiceApplicationSID', value)
    def set_VoiceCallerIDLookup(self, value):
        """
        Set the value of the VoiceCallerIDLookup input for this Choreo. ((optional, string) Do a lookup of a caller's name from the CNAM database and post it to your app. Either true or false. Defaults to false.)
        """
        InputSet._set_input(self, 'VoiceCallerIDLookup', value)
    def set_VoiceFallbackMethod(self, value):
        """
        Set the value of the VoiceFallbackMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the VoiceFallbackUrl. Either GET or POST. Defaults to POST.)
        """
        InputSet._set_input(self, 'VoiceFallbackMethod', value)
    def set_VoiceFallbackURL(self, value):
        """
        Set the value of the VoiceFallbackURL input for this Choreo. ((optional, string) A URL that Twilio will request if an error occurs requesting or executing the TwiML at Url.)
        """
        InputSet._set_input(self, 'VoiceFallbackURL', value)
    def set_VoiceMethod(self, value):
        """
        Set the value of the VoiceMethod input for this Choreo. ((optional, string) The HTTP method that should be used to request the VoiceUrl. Must be either GET or POST. Defaults to POST.)
        """
        InputSet._set_input(self, 'VoiceMethod', value)
    def set_VoiceURL(self, value):
        """
        Set the value of the VoiceURL input for this Choreo. ((optional, string) The URL that Twilio should request when somebody dials a phone number assigned to this application.)
        """
        InputSet._set_input(self, 'VoiceURL', value)

class CreateApplicationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateApplication Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class CreateApplicationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateApplicationResultSet(response, path)
