# -*- coding: utf-8 -*-

###############################################################################
#
# Residence
# Returns information about the annual carbon footprint of a home.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Residence(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Residence Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Residence')


    def new_input_set(self):
        return ResidenceInputSet()

    def _make_result_set(self, result, path):
        return ResidenceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ResidenceChoreographyExecution(session, exec_id, path)

class ResidenceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Residence
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Acquisition(self, value):
        """
        Set the value of the Acquisition input for this Choreo. ((optional, date) Date of acquisition in YYYY-MM-DD format.)
        """
        InputSet._set_input(self, 'Acquisition', value)
    def set_AirConditionerUse(self, value):
        """
        Set the value of the AirConditionerUse input for this Choreo. ((optional, string) The frequency of air conditioner use. Accepted values are: "Not used at all", "Turned on just about all summer", "Turned on only a few days or nights when really needed", or "Turned on quite a bit")
        """
        InputSet._set_input(self, 'AirConditionerUse', value)
    def set_AnnualCoalVolumeEstimate(self, value):
        """
        Set the value of the AnnualCoalVolumeEstimate input for this Choreo. ((optional, decimal) An estimate for amount of coal used annually.)
        """
        InputSet._set_input(self, 'AnnualCoalVolumeEstimate', value)
    def set_AnnualFuelOilCost(self, value):
        """
        Set the value of the AnnualFuelOilCost input for this Choreo. ((optional, decimal) Annual cost of oil fuel in dollars.)
        """
        InputSet._set_input(self, 'AnnualFuelOilCost', value)
    def set_AnnualFuelOilVolumeEstimate(self, value):
        """
        Set the value of the AnnualFuelOilVolumeEstimate input for this Choreo. ((optional, decimal) An estimate for the volume oil used annually.)
        """
        InputSet._set_input(self, 'AnnualFuelOilVolumeEstimate', value)
    def set_AnnualPropaneCost(self, value):
        """
        Set the value of the AnnualPropaneCost input for this Choreo. ((optional, decimal) The annual cost of propane annually in dollars.)
        """
        InputSet._set_input(self, 'AnnualPropaneCost', value)
    def set_AnnualPropaneVolumeEstimate(self, value):
        """
        Set the value of the AnnualPropaneVolumeEstimate input for this Choreo. ((optional, decimal) An estimate of the amount of propane used annually in litres.)
        """
        InputSet._set_input(self, 'AnnualPropaneVolumeEstimate', value)
    def set_AnnualWoodVolumeEstimate(self, value):
        """
        Set the value of the AnnualWoodVolumeEstimate input for this Choreo. ((optional, decimal) An estimate of the amount of wood used for heating annually (in Joulses).)
        """
        InputSet._set_input(self, 'AnnualWoodVolumeEstimate', value)
    def set_Bathrooms(self, value):
        """
        Set the value of the Bathrooms input for this Choreo. ((optional, decimal) The amount of bathrooms in the residence.)
        """
        InputSet._set_input(self, 'Bathrooms', value)
    def set_Bedrooms(self, value):
        """
        Set the value of the Bedrooms input for this Choreo. ((optional, decimal) The number of bedrooms in the residence.)
        """
        InputSet._set_input(self, 'Bedrooms', value)
    def set_ClothesMachineUse(self, value):
        """
        Set the value of the ClothesMachineUse input for this Choreo. ((optional, string) The number laundry loads per week. Valid values are: "1 load or less each week", "10 to 15 loads", "2 to 4 loads", "5 to 9 loads", "More than 15 loads")
        """
        InputSet._set_input(self, 'ClothesMachineUse', value)
    def set_ConstructionYear(self, value):
        """
        Set the value of the ConstructionYear input for this Choreo. ((optional, integer) The year the residence was constructed.)
        """
        InputSet._set_input(self, 'ConstructionYear', value)
    def set_DishwasherUse(self, value):
        """
        Set the value of the DishwasherUse input for this Choreo. ((optional, string) Number of times the dishwasher is used per week. Valid values: "2 or 3 times a week", "4 to 6 times a week", "At least once each day", "Less than once each week", "Once each week".)
        """
        InputSet._set_input(self, 'DishwasherUse', value)
    def set_Floors(self, value):
        """
        Set the value of the Floors input for this Choreo. ((optional, integer) The number of floors.)
        """
        InputSet._set_input(self, 'Floors', value)
    def set_FloorspaceEstimate(self, value):
        """
        Set the value of the FloorspaceEstimate input for this Choreo. ((optional, decimal) An estimate of the amount of floorspace that the residence has.)
        """
        InputSet._set_input(self, 'FloorspaceEstimate', value)
    def set_FreezerCount(self, value):
        """
        Set the value of the FreezerCount input for this Choreo. ((optional, integer) The number of freezers in the residence.)
        """
        InputSet._set_input(self, 'FreezerCount', value)
    def set_FullBathrooms(self, value):
        """
        Set the value of the FullBathrooms input for this Choreo. ((optional, integer) The number of full bathrooms in the residence.)
        """
        InputSet._set_input(self, 'FullBathrooms', value)
    def set_GreenElectricty(self, value):
        """
        Set the value of the GreenElectricty input for this Choreo. ((optional, decimal) The amount green electricity that the residence uses.)
        """
        InputSet._set_input(self, 'GreenElectricty', value)
    def set_HalfBathrooms(self, value):
        """
        Set the value of the HalfBathrooms input for this Choreo. ((optional, integer) The number of half bathrooms in the residence.)
        """
        InputSet._set_input(self, 'HalfBathrooms', value)
    def set_LightingEfficiency(self, value):
        """
        Set the value of the LightingEfficiency input for this Choreo. ((optional, decimal) A numeric value representing the lighting efficiency of the residence.)
        """
        InputSet._set_input(self, 'LightingEfficiency', value)
    def set_MonthlyElectricityCost(self, value):
        """
        Set the value of the MonthlyElectricityCost input for this Choreo. ((optional, decimal) The montly cost of electricity for the residence.)
        """
        InputSet._set_input(self, 'MonthlyElectricityCost', value)
    def set_MonthlyElectricityUseEstimate(self, value):
        """
        Set the value of the MonthlyElectricityUseEstimate input for this Choreo. ((optional, decimal) An estimate for the amount of electricity used monthly in kilowatt hours.)
        """
        InputSet._set_input(self, 'MonthlyElectricityUseEstimate', value)
    def set_MonthlyNaturalGasCost(self, value):
        """
        Set the value of the MonthlyNaturalGasCost input for this Choreo. ((optional, decimal) The monthly cost of natural gas for the residence.)
        """
        InputSet._set_input(self, 'MonthlyNaturalGasCost', value)
    def set_MonthlyNaturalGasVolumeEstimate(self, value):
        """
        Set the value of the MonthlyNaturalGasVolumeEstimate input for this Choreo. ((optional, decimal) An estimate of the amount of natural gas used monthly.)
        """
        InputSet._set_input(self, 'MonthlyNaturalGasVolumeEstimate', value)
    def set_Occupation(self, value):
        """
        Set the value of the Occupation input for this Choreo. ((optional, decimal) Refers to the percentage of time a residence is occupied during a year. Defaults to 0.937.)
        """
        InputSet._set_input(self, 'Occupation', value)
    def set_Ownership(self, value):
        """
        Set the value of the Ownership input for this Choreo. ((optional, boolean) Indicates whether the residence is owned or rented. Set to "true" if you own the residence.)
        """
        InputSet._set_input(self, 'Ownership', value)
    def set_RefrigeratorCount(self, value):
        """
        Set the value of the RefrigeratorCount input for this Choreo. ((optional, integer) The number of refrigerators in the residence.)
        """
        InputSet._set_input(self, 'RefrigeratorCount', value)
    def set_ResidentialClass(self, value):
        """
        Set the value of the ResidentialClass input for this Choreo. ((optional, string) Valid values: "Apartment in a building with 5 or more units", "Apartment in a house or a building with 2-4 units", "Mobile home", "Single-family attached house", or "Single-family detached house".)
        """
        InputSet._set_input(self, 'ResidentialClass', value)
    def set_Residents(self, value):
        """
        Set the value of the Residents input for this Choreo. ((optional, integer) The number of people living in the residence.)
        """
        InputSet._set_input(self, 'Residents', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Retirement(self, value):
        """
        Set the value of the Retirement input for this Choreo. ((optional, date) A date of retirement.)
        """
        InputSet._set_input(self, 'Retirement', value)
    def set_Timeframe(self, value):
        """
        Set the value of the Timeframe input for this Choreo. ((optional, string) A date range specified in the following format: 2008-01-01/2008-07-09)
        """
        InputSet._set_input(self, 'Timeframe', value)
    def set_Urbanity(self, value):
        """
        Set the value of the Urbanity input for this Choreo. ((optional, string) Can be set to: City, Rural, Suburbs, or Town.)
        """
        InputSet._set_input(self, 'Urbanity', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((optional, string) The postal code of the residence.)
        """
        InputSet._set_input(self, 'ZipCode', value)

class ResidenceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Residence Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class ResidenceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ResidenceResultSet(response, path)
