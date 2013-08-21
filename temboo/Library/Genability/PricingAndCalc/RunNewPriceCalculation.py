# -*- coding: utf-8 -*-

###############################################################################
#
# RunNewPriceCalculation
# Calculate electricity costs based on a POSTed calculation criteria. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RunNewPriceCalculation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RunNewPriceCalculation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/RunNewPriceCalculation')


    def new_input_set(self):
        return RunNewPriceCalculationInputSet()

    def _make_result_set(self, result, path):
        return RunNewPriceCalculationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RunNewPriceCalculationChoreographyExecution(session, exec_id, path)

class RunNewPriceCalculationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RunNewPriceCalculation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_POSTData(self, value):
        """
        Set the value of the POSTData input for this Choreo. ((required, json) The POST payload in JSON format.)
        """
        InputSet._set_input(self, 'POSTData', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The App ID provided by Genability.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_MasterTariffID(self, value):
        """
        Set the value of the MasterTariffID input for this Choreo. ((required, string) A Genability tariff ID.)
        """
        InputSet._set_input(self, 'MasterTariffID', value)

class RunNewPriceCalculationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RunNewPriceCalculation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class RunNewPriceCalculationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RunNewPriceCalculationResultSet(response, path)
