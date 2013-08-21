# -*- coding: utf-8 -*-

###############################################################################
#
# FundingSourcesListing
# Retrieves a list of verified funding sources for the user associated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FundingSourcesListing(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FundingSourcesListing Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/FundingSources/FundingSourcesListing')


    def new_input_set(self):
        return FundingSourcesListingInputSet()

    def _make_result_set(self, result, path):
        return FundingSourcesListingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FundingSourcesListingChoreographyExecution(session, exec_id, path)

class FundingSourcesListingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FundingSourcesListing
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        InputSet._set_input(self, 'AccessToken', value)

class FundingSourcesListingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FundingSourcesListing Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class FundingSourcesListingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FundingSourcesListingResultSet(response, path)
