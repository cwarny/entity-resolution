# -*- coding: utf-8 -*-

###############################################################################
#
# CreateTicketNewRequester
# Creates a new ticket as well as a new requester account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateTicketNewRequester(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateTicketNewRequester Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Tickets/CreateTicketNewRequester')


    def new_input_set(self):
        return CreateTicketNewRequesterInputSet()

    def _make_result_set(self, result, path):
        return CreateTicketNewRequesterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateTicketNewRequesterChoreographyExecution(session, exec_id, path)

class CreateTicketNewRequesterInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateTicketNewRequester
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((required, string) The comment for the ticket that is being created.)
        """
        InputSet._set_input(self, 'Comment', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_LocaleID(self, value):
        """
        Set the value of the LocaleID input for this Choreo. ((required, integer) LocaleID for the new requester. Indicate 1 for English, 8 for Deutsch, etc.)
        """
        InputSet._set_input(self, 'LocaleID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) Name of new requester.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_RequesterEmail(self, value):
        """
        Set the value of the RequesterEmail input for this Choreo. ((required, string) Email of new requester.)
        """
        InputSet._set_input(self, 'RequesterEmail', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (i.e. temboocare.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) The subject for the ticket that is being created.)
        """
        InputSet._set_input(self, 'Subject', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((optional, string) The token associated with an upload to attach to this ticket. Note that tokens can be retrieved by running the UploadFile Choreo.)
        """
        InputSet._set_input(self, 'Token', value)

class CreateTicketNewRequesterResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateTicketNewRequester Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class CreateTicketNewRequesterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateTicketNewRequesterResultSet(response, path)
