# -*- coding: utf-8 -*-

###############################################################################
#
# GetTariff
# Returns an individual Tariff object with a given id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTariff(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTariff Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/TariffData/GetTariff')


    def new_input_set(self):
        return GetTariffInputSet()

    def _make_result_set(self, result, path):
        return GetTariffResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTariffChoreographyExecution(session, exec_id, path)

class GetTariffInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTariff
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) The App ID provided by Genability.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Genability.)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_MasterTariffID(self, value):
        """
        Set the value of the MasterTariffID input for this Choreo. ((required, integer) The master tariff id. This can be retrieved in the output of the GetTariffs Choreo.)
        """
        InputSet._set_input(self, 'MasterTariffID', value)
    def set_PopulateProperties(self, value):
        """
        Set the value of the PopulateProperties input for this Choreo. ((optional, boolean) Set to "true" to populate the properties for the returned Tariffs.)
        """
        InputSet._set_input(self, 'PopulateProperties', value)
    def set_PopulateRates(self, value):
        """
        Set the value of the PopulateRates input for this Choreo. ((optional, boolean) Set to "true" to populate the rate details for the returned Tariffs.)
        """
        InputSet._set_input(self, 'PopulateRates', value)

class GetTariffResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTariff Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTariffChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTariffResultSet(response, path)
