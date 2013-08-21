# -*- coding: utf-8 -*-

###############################################################################
#
# Shipment
# Returns information about the carbon footprint of shipping packages.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Shipment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Shipment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Shipment')


    def new_input_set(self):
        return ShipmentInputSet()

    def _make_result_set(self, result, path):
        return ShipmentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShipmentChoreographyExecution(session, exec_id, path)

class ShipmentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Shipment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Carrier(self, value):
        """
        Set the value of the Carrier input for this Choreo. ((optional, string) The carrier used for the shipment. Valid values are: FedEx, UPS, or USPS.)
        """
        InputSet._set_input(self, 'Carrier', value)
    def set_DestinationZipCode(self, value):
        """
        Set the value of the DestinationZipCode input for this Choreo. ((optional, string) The postal code of the destination address.)
        """
        InputSet._set_input(self, 'DestinationZipCode', value)
    def set_Destination(self, value):
        """
        Set the value of the Destination input for this Choreo. ((optional, string) The destination of the shipment.)
        """
        InputSet._set_input(self, 'Destination', value)
    def set_Distance(self, value):
        """
        Set the value of the Distance input for this Choreo. ((optional, decimal) The distance from the shipment origin to the shipment destination.)
        """
        InputSet._set_input(self, 'Distance', value)
    def set_Mode(self, value):
        """
        Set the value of the Mode input for this Choreo. ((optional, string) The mode or method of shipment. Valid values are: air, courier, or ground.)
        """
        InputSet._set_input(self, 'Mode', value)
    def set_OriginZipCode(self, value):
        """
        Set the value of the OriginZipCode input for this Choreo. ((optional, string) The postal code of the origin address.)
        """
        InputSet._set_input(self, 'OriginZipCode', value)
    def set_Origin(self, value):
        """
        Set the value of the Origin input for this Choreo. ((optional, string) The origin of the shipment.)
        """
        InputSet._set_input(self, 'Origin', value)
    def set_PackageCount(self, value):
        """
        Set the value of the PackageCount input for this Choreo. ((optional, integer) The number of packages in the shipment.)
        """
        InputSet._set_input(self, 'PackageCount', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Weight(self, value):
        """
        Set the value of the Weight input for this Choreo. ((optional, decimal) The weight of the shipment in kilograms.)
        """
        InputSet._set_input(self, 'Weight', value)

class ShipmentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Shipment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class ShipmentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShipmentResultSet(response, path)
