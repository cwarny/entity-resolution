# -*- coding: utf-8 -*-

###############################################################################
#
# MakeCall
# Initiates a call from the specified Twilio account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class MakeCall(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MakeCall Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/Calls/MakeCall')


    def new_input_set(self):
        return MakeCallInputSet()

    def _make_result_set(self, result, path):
        return MakeCallResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MakeCallChoreographyExecution(session, exec_id, path)

class MakeCallInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MakeCall
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AccountSID', value)
    def set_ApplicationSID(self, value):
        """
        Set the value of the ApplicationSID input for this Choreo. ((conditional, string) The 34 character sid of the application Twilio should use to handle this phone call. Required unless providing the URL parameter.)
        """
        InputSet._set_input(self, 'ApplicationSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AuthToken', value)
    def set_FallbackMethod(self, value):
        """
        Set the value of the FallbackMethod input for this Choreo. ((optional, string) )
        """
        InputSet._set_input(self, 'FallbackMethod', value)
    def set_FallbackURL(self, value):
        """
        Set the value of the FallbackURL input for this Choreo. ((optional, string) A URL that Twilio will request if an error occurs making a request to the URL provided. This is ignored when ApplicationSID is provided.)
        """
        InputSet._set_input(self, 'FallbackURL', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) The Twilio phone number or client identifier to use as the caller id.)
        """
        InputSet._set_input(self, 'From', value)
    def set_IfMachine(self, value):
        """
        Set the value of the IfMachine input for this Choreo. ((optional, string) Indicates if Twilio should to try and determine if a machine (like voicemail) or a human has answered the call. Possible values are "Continue" and "Hangup".)
        """
        InputSet._set_input(self, 'IfMachine', value)
    def set_Method(self, value):
        """
        Set the value of the Method input for this Choreo. ((optional, string) This the HTTP method Twilio will use when making its request to the URL (when the URL input is provided). Defaults to POST. This is ignored when ApplicationSID is provided.)
        """
        InputSet._set_input(self, 'Method', value)
    def set_Record(self, value):
        """
        Set the value of the Record input for this Choreo. ((optional, boolean) Set this parameter to 'true' to record the entirety of a phone call.)
        """
        InputSet._set_input(self, 'Record', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SendDigits(self, value):
        """
        Set the value of the SendDigits input for this Choreo. ((optional, string) A string of keys to dial after connecting to the number. Valid digits in the string include: any digit (0-9), '#', '*' and 'w' (to insert a half second pause).)
        """
        InputSet._set_input(self, 'SendDigits', value)
    def set_StatusCallbackMethod(self, value):
        """
        Set the value of the StatusCallbackMethod input for this Choreo. ((optional, string) The HTTP method Twilio should use when requesting the StatusCallback URL. Defaults to POST. If an ApplicationSid parameter is present, this parameter is ignored.)
        """
        InputSet._set_input(self, 'StatusCallbackMethod', value)
    def set_StatusCallback(self, value):
        """
        Set the value of the StatusCallback input for this Choreo. ((optional, string) A URL that Twilio will request when the call ends to notify your app. This is ignored when ApplicationSID is provided.)
        """
        InputSet._set_input(self, 'StatusCallback', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with this call. If not specified, the main AccountSID used to authenticate is used in request.)
        """
        InputSet._set_input(self, 'SubAccountSID', value)
    def set_Timeout(self, value):
        """
        Set the value of the Timeout input for this Choreo. ((optional, integer) The integer number of seconds that Twilio should allow the phone to ring before assuming there is no answer. Default is 60 seconds, the maximum is 999 seconds.)
        """
        InputSet._set_input(self, 'Timeout', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) The phone number or client identifier to call.)
        """
        InputSet._set_input(self, 'To', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((conditional, string) The fully qualified URL that should be consulted when the call connects. Required unless providing the ApplicationSID parameter.)
        """
        InputSet._set_input(self, 'URL', value)

class MakeCallResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MakeCall Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class MakeCallChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MakeCallResultSet(response, path)
