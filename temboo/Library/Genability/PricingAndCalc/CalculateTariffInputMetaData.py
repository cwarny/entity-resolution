# -*- coding: utf-8 -*-

###############################################################################
#
# CalculateTariffInputMetaData
# Retrieve inputs required to run a calculation for the specified tariff, within a specified period of time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CalculateTariffInputMetaData(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CalculateTariffInputMetaData Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Genability/PricingAndCalc/CalculateTariffInputMetaData')


    def new_input_set(self):
        return CalculateTariffInputMetaDataInputSet()

    def _make_result_set(self, result, path):
        return CalculateTariffInputMetaDataResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CalculateTariffInputMetaDataChoreographyExecution(session, exec_id, path)

class CalculateTariffInputMetaDataInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CalculateTariffInputMetaData
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
    def set_BillingPeriod(self, value):
        """
        Set the value of the BillingPeriod input for this Choreo. ((optional, string) Specify whether results retireved should be based on a billing period, or not.  Default is set to: false.)
        """
        InputSet._set_input(self, 'BillingPeriod', value)
    def set_CityLimits(self, value):
        """
        Set the value of the CityLimits input for this Choreo. ((optional, string) Specify whether electricity pricing information should be restricted to city limits, or not.  Example input value: Inside.)
        """
        InputSet._set_input(self, 'CityLimits', value)
    def set_ConnectionType(self, value):
        """
        Set the value of the ConnectionType input for this Choreo. ((optional, string) The connection type.  For example: Primary.)
        """
        InputSet._set_input(self, 'ConnectionType', value)
    def set_FromDateTime(self, value):
        """
        Set the value of the FromDateTime input for this Choreo. ((required, string) The date and time of the requested start of the price query. Must be in ISO 8601 format.  Example: 2012-06-12T00:00:00.0-0700)
        """
        InputSet._set_input(self, 'FromDateTime', value)
    def set_GroupBy(self, value):
        """
        Set the value of the GroupBy input for this Choreo. ((optional, string) Specify how calculation details are displayed.  For example retrieved details can be grouped by month, or year. Options include: Daily, Weekly, Month, Year.)
        """
        InputSet._set_input(self, 'GroupBy', value)
    def set_KeyName(self, value):
        """
        Set the value of the KeyName input for this Choreo. ((optional, string) An applicability value.  If an error is returned, indicating the need for an extra applicability parameter, use this variable to set the parameter name.  For example: territoryID.)
        """
        InputSet._set_input(self, 'KeyName', value)
    def set_KeyValue(self, value):
        """
        Set the value of the KeyValue input for this Choreo. ((conditional, string) The value for the specified KeyName variable. For example if KeyName is set to territoryID, you could provide 3385 for the KeyValue input.)
        """
        InputSet._set_input(self, 'KeyValue', value)
    def set_MasterTariffID(self, value):
        """
        Set the value of the MasterTariffID input for this Choreo. ((required, string) A Genability tariff ID.)
        """
        InputSet._set_input(self, 'MasterTariffID', value)
    def set_ToDateTime(self, value):
        """
        Set the value of the ToDateTime input for this Choreo. ((required, string) The date and time of the requested start of the price query. Must be in ISO 8601 format.  Example: 2012-06-12T00:00:00.0-0700)
        """
        InputSet._set_input(self, 'ToDateTime', value)

class CalculateTariffInputMetaDataResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CalculateTariffInputMetaData Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Genability.)
        """
        return self._output.get('Response', None)

class CalculateTariffInputMetaDataChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CalculateTariffInputMetaDataResultSet(response, path)
