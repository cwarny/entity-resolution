# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCharge
# Retrieves the details of an existing charge.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeCharge import StripeCharge

import json

class RetrieveCharge(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCharge Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Charges/RetrieveCharge')


    def new_input_set(self):
        return RetrieveChargeInputSet()

    def _make_result_set(self, result, path):
        return RetrieveChargeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveChargeChoreographyExecution(session, exec_id, path)

class RetrieveChargeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCharge
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ChargeID(self, value):
        """
        Set the value of the ChargeID input for this Choreo. ((required, string) The unique identifier of the charge you want to retrieve)
        """
        InputSet._set_input(self, 'ChargeID', value)

class RetrieveChargeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCharge Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getCharge(self):
        """
        A stripe charge
        """
        return StripeCharge(self.getJSONFromString(self._output.get('Response', [])))

class RetrieveChargeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveChargeResultSet(response, path)
