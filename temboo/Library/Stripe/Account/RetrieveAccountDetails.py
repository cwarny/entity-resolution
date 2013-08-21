# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveAccountDetails
# Retrieves the details of the account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeAccountDetails import StripeAccountDetails

import json

class RetrieveAccountDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveAccountDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Account/RetrieveAccountDetails')


    def new_input_set(self):
        return RetrieveAccountDetailsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveAccountDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveAccountDetailsChoreographyExecution(session, exec_id, path)

class RetrieveAccountDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveAccountDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)

class RetrieveAccountDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveAccountDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getAccountDetails(self):
        """
        Object representing your Stripe Account
        """
        return StripeAccountDetails(self.getJSONFromString(self._output.get('Response', [])))

class RetrieveAccountDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveAccountDetailsResultSet(response, path)
