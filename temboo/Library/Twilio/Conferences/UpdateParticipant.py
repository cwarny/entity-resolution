# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateParticipant
# Updates the status of a conference participant.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateParticipant(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateParticipant Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twilio/Conferences/UpdateParticipant')


    def new_input_set(self):
        return UpdateParticipantInputSet()

    def _make_result_set(self, result, path):
        return UpdateParticipantResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateParticipantChoreographyExecution(session, exec_id, path)

class UpdateParticipantInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateParticipant
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AccountSID', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        InputSet._set_input(self, 'AuthToken', value)
    def set_CallSID(self, value):
        """
        Set the value of the CallSID input for this Choreo. ((required, string) The call id associated with the participant to update.)
        """
        InputSet._set_input(self, 'CallSID', value)
    def set_ConferenceSID(self, value):
        """
        Set the value of the ConferenceSID input for this Choreo. ((required, string) The id of the conference that the participant is in.)
        """
        InputSet._set_input(self, 'ConferenceSID', value)
    def set_Muted(self, value):
        """
        Set the value of the Muted input for this Choreo. ((required, string) Specifying true will mute the participant, while false will un-mute. Anything other than true or false is interpreted as false.)
        """
        InputSet._set_input(self, 'Muted', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with the conference. If not specified, the main AccountSID used to authenticate is used in the request.)
        """
        InputSet._set_input(self, 'SubAccountSID', value)

class UpdateParticipantResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateParticipant Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class UpdateParticipantChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateParticipantResultSet(response, path)
