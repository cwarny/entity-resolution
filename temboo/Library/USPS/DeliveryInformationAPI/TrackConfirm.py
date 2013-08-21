# -*- coding: utf-8 -*-

###############################################################################
#
# TrackConfirm
# Request tracking information for a package with a given tracking id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TrackConfirm(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TrackConfirm Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/USPS/DeliveryInformationAPI/TrackConfirm')


    def new_input_set(self):
        return TrackConfirmInputSet()

    def _make_result_set(self, result, path):
        return TrackConfirmResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TrackConfirmChoreographyExecution(session, exec_id, path)

class TrackConfirmInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TrackConfirm
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
        Set the value of the TrackID input for this Choreo. ((required, string) The tracking number.  Can be alphanumeric characters.  Required value.)
        """
        InputSet._set_input(self, 'TrackID', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((required, string) Alphanumeric ID assigned by USPS)
        """
        InputSet._set_input(self, 'UserId', value)

class TrackConfirmResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TrackConfirm Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from USPS Web Service)
        """
        return self._output.get('Response', None)

class TrackConfirmChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TrackConfirmResultSet(response, path)
