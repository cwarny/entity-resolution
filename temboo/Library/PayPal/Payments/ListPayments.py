# -*- coding: utf-8 -*-

###############################################################################
#
# ListPayments
# Retrieves a list of payments.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPayments(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPayments Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/Payments/ListPayments')


    def new_input_set(self):
        return ListPaymentsInputSet()

    def _make_result_set(self, result, path):
        return ListPaymentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPaymentsChoreographyExecution(session, exec_id, path)

class ListPaymentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPayments
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved from PayPal. Required unless providing the ClientID and ClientSecret which can be used to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by PayPal. Required unless a valid Access Token is provided.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by PayPal. Required unless a valid Access Token is provided.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Number of items to return. Default is 10 with a maximum value of 20.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_Scope(self, value):
        """
        Set the value of the Scope input for this Choreo. ((optional, string) A space delimited list of resource URL endpoints that the token should have access for. This is only used when providing the ClientID and Client Secret in order to generate a new access token.)
        """
        InputSet._set_input(self, 'Scope', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) The field to sort results by. Valid values are: create_time and update_time.)
        """
        InputSet._set_input(self, 'SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) The sort order of the results. Valid values are asc and desc (the default).)
        """
        InputSet._set_input(self, 'SortOrder', value)
    def set_StartID(self, value):
        """
        Set the value of the StartID input for this Choreo. ((optional, string) The resource ID that indicates the starting resource to return. When results are paged, you can use the next_id response value as the StartID to continue with the next set of results.)
        """
        InputSet._set_input(self, 'StartID', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) The start index of the resources to be returned. Used to jump to a specific position in the results.)
        """
        InputSet._set_input(self, 'StartIndex', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((optional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        InputSet._set_input(self, 'UseSandbox', value)

class ListPaymentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPayments Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) The new access token retrieved from PayPal when providing the Client ID and Client Secret.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal.)
        """
        return self._output.get('Response', None)

class ListPaymentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPaymentsResultSet(response, path)
