# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateTicket
# Updates an existing ticket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateTicket(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateTicket Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Tickets/UpdateTicket')


    def new_input_set(self):
        return UpdateTicketInputSet()

    def _make_result_set(self, result, path):
        return UpdateTicketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateTicketChoreographyExecution(session, exec_id, path)

class UpdateTicketInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateTicket
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((conditional, string) The text for a ticket comment.)
        """
        InputSet._set_input(self, 'Comment', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Metadata(self, value):
        """
        Set the value of the Metadata input for this Choreo. ((optional, json) Ticket metadata formatted in JSON. See docs for more information on the input format.)
        """
        InputSet._set_input(self, 'Metadata', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Public(self, value):
        """
        Set the value of the Public input for this Choreo. ((optional, boolean) A flag indicating if this update is public or not. Defaults to "true")
        """
        InputSet._set_input(self, 'Public', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (i.e. temboocare.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((conditional, string) The status of the ticket (i.e. solved, pending, open).)
        """
        InputSet._set_input(self, 'Status', value)
    def set_TicketData(self, value):
        """
        Set the value of the TicketData input for this Choreo. ((optional, json) A JSON string containing the ticket information. This can be used as an alternative to the serialized ticket inputs in case you need to update tickets that have custom fields.)
        """
        InputSet._set_input(self, 'TicketData', value)
    def set_TicketID(self, value):
        """
        Set the value of the TicketID input for this Choreo. ((required, integer) The id of the ticket being updated.)
        """
        InputSet._set_input(self, 'TicketID', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((optional, string) The token associated with an upload to attach to this ticket. Note that tokens can be retrieved by running the UploadFile Choreo.)
        """
        InputSet._set_input(self, 'Token', value)

class UpdateTicketResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateTicket Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class UpdateTicketChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateTicketResultSet(response, path)
