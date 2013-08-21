# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCardToken
# Retrieves a card token based on a given id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeToken import StripeToken

import json

class RetrieveCardToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCardToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Tokens/RetrieveCardToken')


    def new_input_set(self):
        return RetrieveCardTokenInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCardTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCardTokenChoreographyExecution(session, exec_id, path)

class RetrieveCardTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCardToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_TokenID(self, value):
        """
        Set the value of the TokenID input for this Choreo. ((required, string) The unique identifier of the token you want to retrieve)
        """
        InputSet._set_input(self, 'TokenID', value)

class RetrieveCardTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCardToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getToken(self):
        """
        Reference to Stripe Token object
        """
        return StripeToken(self.getJSONFromString(self._output.get('Response', [])))

class RetrieveCardTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveCardTokenResultSet(response, path)
