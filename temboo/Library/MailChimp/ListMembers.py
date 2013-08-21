# -*- coding: utf-8 -*-

###############################################################################
#
# ListMembers
# Retrieves the email addresses of members of a MailChimp list. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListMembers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMembers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListMembers')


    def new_input_set(self):
        return ListMembersInputSet()

    def _make_result_set(self, result, path):
        return ListMembersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMembersChoreographyExecution(session, exec_id, path)

class ListMembersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMembers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Mailchimp.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Specifies the number of records in a page to be returned. Must be greater than zero and less than or equal to 15000. Defaults to 100.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_ListId(self, value):
        """
        Set the value of the ListId input for this Choreo. ((required, string) The id of the Mailchimp list to retrieve members from.)
        """
        InputSet._set_input(self, 'ListId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Indicates the desired format for the response. Accepted values are "json" or "xml" (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) Retrieves records that have changed since this date/time. Formatted like 'YYYY-MM-DD HH:MM:SS.)
        """
        InputSet._set_input(self, 'Since', value)
    def set_Start(self, value):
        """
        Set the value of the Start input for this Choreo. ((optional, integer) Specifies the page at which to begin returning records. Page size is defined by the limit argument. Must be zero or greater. Defaults to 0.)
        """
        InputSet._set_input(self, 'Start', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((optional, string) Must be one of 'subscribed', 'unsubscribed', 'cleaned', or 'updated'. Defaults to 'subscribed'.)
        """
        InputSet._set_input(self, 'Status', value)

class ListMembersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMembers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Mailchimp. Corresponds to the format specified in the ResponseFormat parameter. Defaults to "xml".)
        """
        return self._output.get('Response', None)

class ListMembersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListMembersResultSet(response, path)
