# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllCharges
# Returns a list of all charges or a list of charges for a specified customer.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeChargeList import StripeChargeList

import json

class ListAllCharges(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllCharges Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Charges/ListAllCharges')


    def new_input_set(self):
        return ListAllChargesInputSet()

    def _make_result_set(self, result, path):
        return ListAllChargesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllChargesChoreographyExecution(session, exec_id, path)

class ListAllChargesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllCharges
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The limit of charges to be returned. Can range from 1 to 100. Defaults to 10.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((optional, string) The unique identifier of the customer whose charges to return. If not specified, all charges will be returned.)
        """
        InputSet._set_input(self, 'CustomerID', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Stripe will return a list of charges starting at the specified offset. Defaults to 0.)
        """
        InputSet._set_input(self, 'Offset', value)

class ListAllChargesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllCharges Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getChargeList(self):
        """
        A list of all charges
        """
        return StripeChargeList(self.getJSONFromString(self._output.get('Response', [])))

class ListAllChargesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllChargesResultSet(response, path)
