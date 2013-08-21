# -*- coding: utf-8 -*-

###############################################################################
#
# GetListEmailAddresses
# Retrieve email addresses associated with a specified Recipient List.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetListEmailAddresses(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetListEmailAddresses Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/NewsletterAPI/ListsEmail/GetListEmailAddresses')


    def new_input_set(self):
        return GetListEmailAddressesInputSet()

    def _make_result_set(self, result, path):
        return GetListEmailAddressesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetListEmailAddressesChoreographyExecution(session, exec_id, path)

class GetListEmailAddressesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetListEmailAddresses
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        InputSet._set_input(self, 'APIUser', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email address to search for in a recipient list.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_List(self, value):
        """
        Set the value of the List input for this Choreo. ((required, string) The recipient list from which email addresses will be retrieved.  Must be an existing recipient list.)
        """
        InputSet._set_input(self, 'List', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)


class GetListEmailAddressesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetListEmailAddresses Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class GetListEmailAddressesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetListEmailAddressesResultSet(response, path)
