# -*- coding: utf-8 -*-

###############################################################################
#
# TestAccount
# Allows you to perform simple test to verify connectivity with your Google Checkout account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TestAccount(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TestAccount Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Checkout/TestAccount')


    def new_input_set(self):
        return TestAccountInputSet()

    def _make_result_set(self, result, path):
        return TestAccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TestAccountChoreographyExecution(session, exec_id, path)

class TestAccountInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TestAccount
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) Set to checkout.google.com when running in production. Defaults to sandbox.google.com for sandbox testing.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_MerchantId(self, value):
        """
        Set the value of the MerchantId input for this Choreo. ((required, integer) The Merchant Id provided by Google)
        """
        InputSet._set_input(self, 'MerchantId', value)
    def set_MerchantKey(self, value):
        """
        Set the value of the MerchantKey input for this Choreo. ((required, string) The Merchant Key provided by Google)
        """
        InputSet._set_input(self, 'MerchantKey', value)

class TestAccountResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TestAccount Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class TestAccountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TestAccountResultSet(response, path)
