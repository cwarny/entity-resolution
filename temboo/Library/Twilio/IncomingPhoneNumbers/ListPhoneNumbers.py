# -*- coding: utf-8 -*-

###############################################################################
#
# ListPhoneNumbers
# Returns a list of Twilio phone numbers purchased from Twilio or ported to Twilio.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPhoneNumbers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPhoneNumbers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/IncomingPhoneNumbers/ListPhoneNumbers')


    def new_input_set(self):
        return ListPhoneNumbersInputSet()

    def _make_result_set(self, result, path):
        return ListPhoneNumbersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPhoneNumbersChoreographyExecution(session, exec_id, path)

class ListPhoneNumbersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPhoneNumbers
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
    def set_FriendlyName(self, value):
        """
        Set the value of the FriendlyName input for this Choreo. ((optional, string) Only return the incoming phone number resources with friendly names that exactly match this name.)
        """
        InputSet._set_input(self, 'FriendlyName', value)
    def set_PageSize(self, value):
        """
        Set the value of the PageSize input for this Choreo. ((optional, integer) The number of results per page.)
        """
        InputSet._set_input(self, 'PageSize', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page of results to retrieve. Defaults to 0.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_PhoneNumber(self, value):
        """
        Set the value of the PhoneNumber input for this Choreo. ((optional, string) Only return the incoming phone number resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.)
        """
        InputSet._set_input(self, 'PhoneNumber', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with the list of phone numbers. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        InputSet._set_input(self, 'SubAccountSID', value)

class ListPhoneNumbersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPhoneNumbers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class ListPhoneNumbersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPhoneNumbersResultSet(response, path)
