# -*- coding: utf-8 -*-

###############################################################################
#
# RSVPEvent
# RSVP to an event as "attending", "maybe", or "declined".
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RSVPEvent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RSVPEvent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/RSVPEvent')


    def new_input_set(self):
        return RSVPEventInputSet()

    def _make_result_set(self, result, path):
        return RSVPEventResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RSVPEventChoreographyExecution(session, exec_id, path)

class RSVPEventInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RSVPEvent
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_EventID(self, value):
        """
        Set the value of the EventID input for this Choreo. ((required, string) The id for the event  to rsvp for.)
        """
        InputSet._set_input(self, 'EventID', value)
    def set_RSVP(self, value):
        """
        Set the value of the RSVP input for this Choreo. ((required, string) The RSVP for the event. Valid values are: attending, maybe, or declined.)
        """
        InputSet._set_input(self, 'RSVP', value)

class RSVPEventResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RSVPEvent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class RSVPEventChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RSVPEventResultSet(response, path)
