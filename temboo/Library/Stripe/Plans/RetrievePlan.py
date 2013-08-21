# -*- coding: utf-8 -*-

###############################################################################
#
# RetrievePlan
# Retrieves plan details with a specified plan id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripePlan import StripePlan

import json

class RetrievePlan(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrievePlan Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Plans/RetrievePlan')


    def new_input_set(self):
        return RetrievePlanInputSet()

    def _make_result_set(self, result, path):
        return RetrievePlanResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrievePlanChoreographyExecution(session, exec_id, path)

class RetrievePlanInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrievePlan
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_PlanID(self, value):
        """
        Set the value of the PlanID input for this Choreo. ((required, string) The unique identifier of the plan you want to retrieve)
        """
        InputSet._set_input(self, 'PlanID', value)

class RetrievePlanResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrievePlan Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getPlan(self):
        """
        A subscription plan contains the pricing information for different products and feature levels on your site. For example, you might have a $10/month plan for basic features and a different $20/month plan for premium features.
        """
        return StripePlan(self.getJSONFromString(self._output.get('Response', [])))

class RetrievePlanChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrievePlanResultSet(response, path)
