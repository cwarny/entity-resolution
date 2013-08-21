# -*- coding: utf-8 -*-

###############################################################################
#
# SendSMS
# Sends an SMS to a specified phone number using the Twilio API.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SendSMS(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendSMS Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/SMSMessages/SendSMS')


    def new_input_set(self):
        return SendSMSInputSet()

    def _make_result_set(self, result, path):
        return SendSMSResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendSMSChoreographyExecution(session, exec_id, path)

class SendSMSInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendSMS
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, string) The text of your SMS message.)
        """
        InputSet._set_input(self, 'Body', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) The purchased Twilio phone number (or Twilio Sandbox number) to send the message from.)
        """
        InputSet._set_input(self, 'From', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount to send the message from. If not specified, the main AccountSID used to authenticate is used in request.)
        """
        InputSet._set_input(self, 'SubAccountSID', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) The destination phone number for the SMS message.)
        """
        InputSet._set_input(self, 'To', value)

class SendSMSResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendSMS Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The Twilio response.)
        """
        return self._output.get('Response', None)

class SendSMSChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendSMSResultSet(response, path)
