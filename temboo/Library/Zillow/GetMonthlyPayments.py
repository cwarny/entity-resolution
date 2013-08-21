# -*- coding: utf-8 -*-

###############################################################################
#
# GetMonthlyPayments
# Retrieve estimated monthly payments, including principal and interest based on current interest rates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetMonthlyPayments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMonthlyPayments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zillow/GetMonthlyPayments')


    def new_input_set(self):
        return GetMonthlyPaymentsInputSet()

    def _make_result_set(self, result, path):
        return GetMonthlyPaymentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMonthlyPaymentsChoreographyExecution(session, exec_id, path)

class GetMonthlyPaymentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMonthlyPayments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DollarsDown(self, value):
        """
        Set the value of the DollarsDown input for this Choreo. ((optional, integer) Specify the dollar amount that is placed for a down payment. This variable can be used in place of DownPaymentAmount.)
        """
        InputSet._set_input(self, 'DollarsDown', value)
    def set_DownPaymentAmount(self, value):
        """
        Set the value of the DownPaymentAmount input for this Choreo. ((optional, integer) Enter the percentage of the total properly price that will be used as a down payment. If < 20%, mortage insurance info is also returned.)
        """
        InputSet._set_input(self, 'DownPaymentAmount', value)
    def set_OutputFormat(self, value):
        """
        Set the value of the OutputFormat input for this Choreo. ((optional, string) Enter the desired query output format.  Enter: xml, or json.  Default output is set to: xml.)
        """
        InputSet._set_input(self, 'OutputFormat', value)
    def set_Price(self, value):
        """
        Set the value of the Price input for this Choreo. ((required, integer) Enter the price for which the monthly payment is to be calculated.)
        """
        InputSet._set_input(self, 'Price', value)
    def set_ZWSID(self, value):
        """
        Set the value of the ZWSID input for this Choreo. ((required, string) Enter a Zillow Web Service Identifier (ZWS ID).)
        """
        InputSet._set_input(self, 'ZWSID', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((optional, integer) Enter the zip code of the property.  If null, no property tax, or hazard insurance data will be returned.)
        """
        InputSet._set_input(self, 'Zip', value)

class GetMonthlyPaymentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMonthlyPayments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Zillow.)
        """
        return self._output.get('Response', None)

class GetMonthlyPaymentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMonthlyPaymentsResultSet(response, path)
