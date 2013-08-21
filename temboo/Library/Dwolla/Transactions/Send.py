# -*- coding: utf-8 -*-

###############################################################################
#
# Send
# Use this method to send funds to a destination user, from the user associated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Send(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Send Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Transactions/Send')


    def new_input_set(self):
        return SendInputSet()

    def _make_result_set(self, result, path):
        return SendResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendChoreographyExecution(session, exec_id, path)

class SendInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Send
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, decimal) Amount of funds to transfer to the destination user.)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_AssumeCosts(self, value):
        """
        Set the value of the AssumeCosts input for this Choreo. ((required, boolean) Set to true if the user will assume the Dwolla fee. Set to false if the destination user will assume the Dwolla fee. Does not affect facilitator fees. Defaults to false.)
        """
        InputSet._set_input(self, 'AssumeCosts', value)
    def set_DestinationId(self, value):
        """
        Set the value of the DestinationId input for this Choreo. ((required, string) Identification of the user to send funds to. Must be the Dwolla identifier, Facebook identifier, Twitter identifier, phone number, or email address.)
        """
        InputSet._set_input(self, 'DestinationId', value)
    def set_DestinationType(self, value):
        """
        Set the value of the DestinationType input for this Choreo. ((optional, string) Type of destination user. Defaults to Dwolla. Can be Dwolla, Facebook, Twitter, Email, or Phone.)
        """
        InputSet._set_input(self, 'DestinationType', value)
    def set_FacillitatorAmount(self, value):
        """
        Set the value of the FacillitatorAmount input for this Choreo. ((required, string) Amount of the facilitator fee to override. Only applicable if the facilitator fee feature is enabled. If set to 0, facilitator fee is disabled for transaction. Cannot exceed 25% of the 'amount'.)
        """
        InputSet._set_input(self, 'FacillitatorAmount', value)
    def set_FundsSource(self, value):
        """
        Set the value of the FundsSource input for this Choreo. ((required, string) Id of funding source to send funds from. Defaults to Balance.  Balance sourced transfers process immediately. Non-balanced sourced transfers may process immediately or take up to five business days.)
        """
        InputSet._set_input(self, 'FundsSource', value)
    def set_Notes(self, value):
        """
        Set the value of the Notes input for this Choreo. ((required, multiline) Note to attach to the transaction. Limited to 250 characters.)
        """
        InputSet._set_input(self, 'Notes', value)
    def set_Pin(self, value):
        """
        Set the value of the Pin input for this Choreo. ((required, integer) User's PIN associated with their account)
        """
        InputSet._set_input(self, 'Pin', value)

class SendResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Send Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class SendChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendResultSet(response, path)
