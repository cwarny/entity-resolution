# -*- coding: utf-8 -*-

###############################################################################
#
# ExpressMailServiceRequest
# Request USPS Express Mail shipping information for a given origin and destination.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ExpressMailServiceRequest(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ExpressMailServiceRequest Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/USPS/DeliveryInformationAPI/ExpressMailServiceRequest')


    def new_input_set(self):
        return ExpressMailServiceRequestInputSet()

    def _make_result_set(self, result, path):
        return ExpressMailServiceRequestResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExpressMailServiceRequestChoreographyExecution(session, exec_id, path)

class ExpressMailServiceRequestInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ExpressMailServiceRequest
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((required, date) Date the package is to be shipped. Must take the form 'MM/DD/YYYY'.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_DestinationZip(self, value):
        """
        Set the value of the DestinationZip input for this Choreo. ((required, integer) Five digit zip code.)
        """
        InputSet._set_input(self, 'DestinationZip', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_OriginZip(self, value):
        """
        Set the value of the OriginZip input for this Choreo. ((required, integer) Three or five digit zip code.)
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

class ExpressMailServiceRequestResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ExpressMailServiceRequest Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from USPS Web Service)
        """
        return self._output.get('Response', None)

class ExpressMailServiceRequestChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ExpressMailServiceRequestResultSet(response, path)
