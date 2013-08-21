# -*- coding: utf-8 -*-

###############################################################################
#
# Listing
# Retrieves a list of transactions for the user associated with the authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Listing(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Listing Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Transactions/Listing')


    def new_input_set(self):
        return ListingInputSet()

    def _make_result_set(self, result, path):
        return ListingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListingChoreographyExecution(session, exec_id, path)

class ListingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Listing
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of transactions to retrieve. Defaults to 10. Can be between 1 and 200 transactions.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_SinceDate(self, value):
        """
        Set the value of the SinceDate input for this Choreo. ((optional, string) Earliest date and time for which to retrieve transactions. Defaults to 7 days prior to current date and time in UTC.)
        """
        InputSet._set_input(self, 'SinceDate', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Number of transactions to skip. Defaults to 0.)
        """
        InputSet._set_input(self, 'Skip', value)
    def set_Types(self, value):
        """
        Set the value of the Types input for this Choreo. ((optional, string) Transaction types to retrieve. Must be delimited by a '|'. Options are money_sent, money_received, deposit, withdrawal, and fee. Defaults to include all transaction types.)
        """
        InputSet._set_input(self, 'Types', value)

class ListingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Listing Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class ListingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListingResultSet(response, path)
