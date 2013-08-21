# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllPlans
# Returns a list of all plans. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripePlanList import StripePlanList

import json

class ListAllPlans(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllPlans Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Plans/ListAllPlans')


    def new_input_set(self):
        return ListAllPlansInputSet()

    def _make_result_set(self, result, path):
        return ListAllPlansResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllPlansChoreographyExecution(session, exec_id, path)

class ListAllPlansInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllPlans
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The limit of plans to be returned. Can range from 1 to 100. Defaults to 10.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Stripe will return a list of plans starting at the specified offset. Defaults to 0.)
        """
        InputSet._set_input(self, 'Offset', value)

class ListAllPlansResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllPlans Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getPlanList(self):
        """
        A list of plans
        """
        return StripePlanList(self.getJSONFromString(self._output.get('Response', [])))

class ListAllPlansChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllPlansResultSet(response, path)
