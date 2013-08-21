# -*- coding: utf-8 -*-

###############################################################################
#
# AddURL
# Add a document to an Instapaper account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddURL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddURL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instapaper/AddURL')


    def new_input_set(self):
        return AddURLInputSet()

    def _make_result_set(self, result, path):
        return AddURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddURLChoreographyExecution(session, exec_id, path)

class AddURLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddURL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) Your Instapaper password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Selection(self, value):
        """
        Set the value of the Selection input for this Choreo. ((optional, string) Enter a description of the URL being added.)
        """
        InputSet._set_input(self, 'Selection', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) Enter a titile for the uploaded URL. If no title is provided, Instapaper will crawl the URL to detect a title.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) Enter the URL of the document that is being added to an Instapaper account.)
        """
        InputSet._set_input(self, 'URL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Instapaper username.)
        """
        InputSet._set_input(self, 'Username', value)

class AddURLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddURL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((integer) The response from Instapaper. Successful reqests will return a 201 status code.)
        """
        return self._output.get('Response', None)

class AddURLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddURLResultSet(response, path)
