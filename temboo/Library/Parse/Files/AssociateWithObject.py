# -*- coding: utf-8 -*-

###############################################################################
#
# AssociateWithObject
# Allows you to associate a previously uploaded file with Parse objects.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AssociateWithObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AssociateWithObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Parse/Files/AssociateWithObject')


    def new_input_set(self):
        return AssociateWithObjectInputSet()

    def _make_result_set(self, result, path):
        return AssociateWithObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AssociateWithObjectChoreographyExecution(session, exec_id, path)

class AssociateWithObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AssociateWithObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Association(self, value):
        """
        Set the value of the Association input for this Choreo. ((required, json) A JSON string containing the file information that is to be associated with the Parse object. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'Association', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        InputSet._set_input(self, 'ApplicationID', value)
    def set_ClassName(self, value):
        """
        Set the value of the ClassName input for this Choreo. ((required, string) The name of the class that a file is being associated with.)
        """
        InputSet._set_input(self, 'ClassName', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        InputSet._set_input(self, 'RESTAPIKey', value)

class AssociateWithObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AssociateWithObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class AssociateWithObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AssociateWithObjectResultSet(response, path)
