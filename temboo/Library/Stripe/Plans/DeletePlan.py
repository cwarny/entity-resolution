# -*- coding: utf-8 -*-

###############################################################################
#
# DeletePlan
# Deletes a specified plan.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeDeleteResults import StripeDeleteResults

import json

class DeletePlan(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeletePlan Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Plans/DeletePlan')


    def new_input_set(self):
        return DeletePlanInputSet()

    def _make_result_set(self, result, path):
        return DeletePlanResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePlanChoreographyExecution(session, exec_id, path)

class DeletePlanInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeletePlan
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_PlanID(self, value):
        """
        Set the value of the PlanID input for this Choreo. ((required, string) The unique identifier of the plan you want to delete)
        """
        InputSet._set_input(self, 'PlanID', value)

class DeletePlanResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeletePlan Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getDeleteResults(self):
        """
        """
        return StripeDeleteResults(self.getJSONFromString(self._output.get('Response', [])))

class DeletePlanChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeletePlanResultSet(response, path)
