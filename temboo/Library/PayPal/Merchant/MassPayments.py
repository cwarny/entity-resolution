# -*- coding: utf-8 -*-

###############################################################################
#
# MassPayments
# Generates multiple payments from your PayPal Premier account or Business account to existing PayPal account holders.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class MassPayments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MassPayments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/Merchant/MassPayments')


    def new_input_set(self):
        return MassPaymentsInputSet()

    def _make_result_set(self, result, path):
        return MassPaymentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MassPaymentsChoreographyExecution(session, exec_id, path)

class MassPaymentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MassPayments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_InputFile(self, value):
        """
        Set the value of the InputFile input for this Choreo. ((required, any) An input file containing the payments to process. This data can either be in CSV or XML format. The format should be indicated using the InputFormat input. See Choreo documentation for schema details.)
        """
        InputSet._set_input(self, 'InputFile', value)
    def set_EmailSubject(self, value):
        """
        Set the value of the EmailSubject input for this Choreo. ((optional, string) The subject line of the email that PayPal sends when the transaction is completed. This is the same for all recipients. Character length and limitations: 255 single-byte alphanumeric characters.)
        """
        InputSet._set_input(self, 'EmailSubject', value)
    def set_InputFormat(self, value):
        """
        Set the value of the InputFormat input for this Choreo. ((required, string) The type of input you are providing for this mass payment. Accepted values are "csv" or "xml". See Choreo documentation for expected schema details.)
        """
        InputSet._set_input(self, 'InputFormat', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((required, string) The API Signature provided by PayPal.)
        """
        InputSet._set_input(self, 'Signature', value)
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


class MassPaymentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MassPayments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Result(self):
        """
        Retrieve the value for the "Result" output from this Choreo execution. (The MassPayment result from PayPal returned in the same format you've submitted.)
        """
        return self._output.get('Result', None)

class MassPaymentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MassPaymentsResultSet(response, path)
