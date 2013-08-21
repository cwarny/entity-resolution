# -*- coding: utf-8 -*-

###############################################################################
#
# PackageServicesRequest
# Request USPS Parcel Post, Bound Printed Matter, Library Mail, or Media Mail shipping information for a given origin and destination.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PackageServicesRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PackageServicesRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/USPS/DeliveryInformationAPI/PackageServicesRequest')


    def new_input_set(self):
        return PackageServicesRequestInputSet()

    def _make_result_set(self, result, path):
        return PackageServicesRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PackageServicesRequestChoreographyExecution(session, exec_id, path)

class PackageServicesRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PackageServicesRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Response(self, value):
        """
        Set the value of the Response input for this Choreo. ((required, xml) The response from USPS Web Service)
        """
        InputSet._set_input(self, 'Response', value)
    def set_DestinationZip(self, value):
        """
        Set the value of the DestinationZip input for this Choreo. ((required, integer) First 3 digits of a 5-digit zip code.)
        """
        InputSet._set_input(self, 'DestinationZip', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_OriginZip(self, value):
        """
        Set the value of the OriginZip input for this Choreo. ((required, integer) First 3 digits of a 5-digit zip code.  Required value.)
        """
        InputSet._set_input(self, 'OriginZip', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password assigned by USPS)
        """
        InputSet._set_input(self, 'Password', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((required, string) Alphanumeric ID assigned by USPS)
        """
        InputSet._set_input(self, 'UserId', value)

class PackageServicesRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PackageServicesRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((required, xml) The response from USPS Web Service)
        """
        return self._output.get('Response', None)

class PackageServicesRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PackageServicesRequestResultSet(response, path)
