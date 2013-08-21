# -*- coding: utf-8 -*-

###############################################################################
#
# FundingSourcesByID
# Retrieves the account information for the user associated with the given authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FundingSourcesByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FundingSourcesByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/FundingSources/FundingSourcesByID')


    def new_input_set(self):
        return FundingSourcesByIDInputSet()

    def _make_result_set(self, result, path):
        return FundingSourcesByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FundingSourcesByIDChoreographyExecution(session, exec_id, path)

class FundingSourcesByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FundingSourcesByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_FundingID(self, value):
        """
        Set the value of the FundingID input for this Choreo. ((required, string) Funding source identifier of the funding source being requested.)
        """
        InputSet._set_input(self, 'FundingID', value)

class FundingSourcesByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FundingSourcesByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class FundingSourcesByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FundingSourcesByIDResultSet(response, path)
