# -*- coding: utf-8 -*-

###############################################################################
#
# TrackConfirmFields
# Track a package sent via USPS and return tracking information with details in separate XML tags.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TrackConfirmFields(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TrackConfirmFields Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/USPS/DeliveryInformationAPI/TrackConfirmFields')


    def new_input_set(self):
        return TrackConfirmFieldsInputSet()

    def _make_result_set(self, result, path):
        return TrackConfirmFieldsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrackConfirmFieldsChoreographyExecution(session, exec_id, path)

class TrackConfirmFieldsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TrackConfirmFields
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) If you are accessing the production server, set to 'production'. Defaults to 'testing' which indicates that you are using the sandbox.)
        """
        InputSet._set_input(self, 'Endpoint', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password assigned by USPS)
        """
        InputSet._set_input(self, 'Password', value)
    def set_TrackID(self, value):
        """
        Set the value of the TrackID input for this Choreo. ((required, string) The tracking number.  Can be alphanumeric characters.)
        """
        InputSet._set_input(self, 'TrackID', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((required, string) Alphanumeric ID assigned by USPS)
        """
        InputSet._set_input(self, 'UserId', value)

class TrackConfirmFieldsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TrackConfirmFields Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from USPS Web Service)
        """
        return self._output.get('Response', None)

class TrackConfirmFieldsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TrackConfirmFieldsResultSet(response, path)
