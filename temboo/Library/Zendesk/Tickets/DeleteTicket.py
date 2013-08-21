# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteTicket
# Deletes an existing ticket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteTicket(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteTicket Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Tickets/DeleteTicket')


    def new_input_set(self):
        return DeleteTicketInputSet()

    def _make_result_set(self, result, path):
        return DeleteTicketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteTicketChoreographyExecution(session, exec_id, path)

class DeleteTicketInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteTicket
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email to authenticate the Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The ID number of a ticket.)
        """
        InputSet._set_input(self, 'ID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password matching the email to authenticate the Zendesk account.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) The server URL associated with your Zendesk account. In many cases this looks like: temboo.zendesk.com but may also be customized: support.temboo.com)
        """
        InputSet._set_input(self, 'Server', value)

class DeleteTicketResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteTicket Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class DeleteTicketChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteTicketResultSet(response, path)
