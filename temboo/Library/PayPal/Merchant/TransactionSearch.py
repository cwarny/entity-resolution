# -*- coding: utf-8 -*-

###############################################################################
#
# TransactionSearch
# Retrieves transaction history for transactions that meet a specified criteria.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TransactionSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TransactionSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/Merchant/TransactionSearch')


    def new_input_set(self):
        return TransactionSearchInputSet()

    def _make_result_set(self, result, path):
        return TransactionSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TransactionSearchChoreographyExecution(session, exec_id, path)

class TransactionSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TransactionSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Account(self, value):
        """
        Set the value of the Account input for this Choreo. ((optional, string) Search by credit card number.)
        """
        InputSet._set_input(self, 'Account', value)
    def set_AuctionItemNumber(self, value):
        """
        Set the value of the AuctionItemNumber input for this Choreo. ((optional, string) Search by auction item number of the purchased item.)
        """
        InputSet._set_input(self, 'AuctionItemNumber', value)
    def set_CurrencyCode(self, value):
        """
        Set the value of the CurrencyCode input for this Choreo. ((optional, string) Search by currency code (i.e. USD).)
        """
        InputSet._set_input(self, 'CurrencyCode', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) Search by email.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) The latest transaction date to return. Must be an epoch timestamp in milliseconds or formatted in UTC like: 2011-05-19T00:00:00Z.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_InvoiceNumber(self, value):
        """
        Set the value of the InvoiceNumber input for this Choreo. ((optional, string) Search by invoice number.)
        """
        InputSet._set_input(self, 'InvoiceNumber', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ReceiptId(self, value):
        """
        Set the value of the ReceiptId input for this Choreo. ((optional, string) Search by the PayPal receipt ID.)
        """
        InputSet._set_input(self, 'ReceiptId', value)
    def set_Receiver(self, value):
        """
        Set the value of the Receiver input for this Choreo. ((optional, string) Search by the email address of the receiver.)
        """
        InputSet._set_input(self, 'Receiver', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((required, string) The API Signature provided by PayPal.)
        """
        InputSet._set_input(self, 'Signature', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((required, date) The earliest transaction date to return. Must be an epoch timestamp in milliseconds or formatted in UTC like: 2011-05-19T00:00:00Z.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_TransactionAmount(self, value):
        """
        Set the value of the TransactionAmount input for this Choreo. ((optional, decimal) Search by transaction amount.)
        """
        InputSet._set_input(self, 'TransactionAmount', value)
    def set_TransactionClass(self, value):
        """
        Set the value of the TransactionClass input for this Choreo. ((optional, string) Search by classification of transaction (i.e. All, Sent, Recieved, etc).)
        """
        InputSet._set_input(self, 'TransactionClass', value)
    def set_TransactionId(self, value):
        """
        Set the value of the TransactionId input for this Choreo. ((optional, string) Search by the transaction ID)
        """
        InputSet._set_input(self, 'TransactionId', value)
    def set_TransactionStatus(self, value):
        """
        Set the value of the TransactionStatus input for this Choreo. ((optional, string) Search by transaction status (i.e. Pending, Processing, Success, Denied, Reversed).)
        """
        InputSet._set_input(self, 'TransactionStatus', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((optional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        InputSet._set_input(self, 'UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The API Username provided by PayPal.)
        """
        InputSet._set_input(self, 'Username', value)

class TransactionSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TransactionSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) Response from PayPal formatted in name/value pairs.)
        """
        return self._output.get('Response', None)

class TransactionSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TransactionSearchResultSet(response, path)
