# -*- coding: utf-8 -*-

###############################################################################
#
# GetTerritoryIDFromZipcode
# Get a territoryID, by using a consumer's zipcode, LSE ID and master tariff ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTerritoryIDFromZipcode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTerritoryIDFromZipcode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/GetTerritoryIDFromZipcode')


    def new_input_set(self):
        return GetTerritoryIDFromZipcodeInputSet()

    def _make_result_set(self, result, path):
        return GetTerritoryIDFromZipcodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTerritoryIDFromZipcodeChoreographyExecution(session, exec_id, path)

class GetTerritoryIDFromZipcodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTerritoryIDFromZipcode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
    def set_LSEID(self, value):
        """
        Set the value of the LSEID input for this Choreo. ((required, string) An LSE ID.)
        """
        InputSet._set_input(self, 'LSEID', value)
    def set_MasterTariffID(self, value):
        """
        Set the value of the MasterTariffID input for this Choreo. ((required, string) A Genability tariff ID.)
        """
        InputSet._set_input(self, 'MasterTariffID', value)
    def set_Zipcode(self, value):
        """
        Set the value of the Zipcode input for this Choreo. ((required, integer) A zip code for which a territory ID is to be retrieved.)
        """
        InputSet._set_input(self, 'Zipcode', value)

class GetTerritoryIDFromZipcodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTerritoryIDFromZipcode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class GetTerritoryIDFromZipcodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTerritoryIDFromZipcodeResultSet(response, path)
