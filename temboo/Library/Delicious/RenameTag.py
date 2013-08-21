# -*- coding: utf-8 -*-

###############################################################################
#
# RenameTag
# Renames a specified tag.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RenameTag(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RenameTag Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Delicious/RenameTag')


    def new_input_set(self):
        return RenameTagInputSet()

    def _make_result_set(self, result, path):
        return RenameTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RenameTagChoreographyExecution(session, exec_id, path)

class RenameTagInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RenameTag
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_NewTag(self, value):
        """
        Set the value of the NewTag input for this Choreo. ((required, string) The new tag name.)
        """
        InputSet._set_input(self, 'NewTag', value)
    def set_OldTag(self, value):
        """
        Set the value of the OldTag input for this Choreo. ((required, string) The existing tag to rename.)
        """
        InputSet._set_input(self, 'OldTag', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        InputSet._set_input(self, 'Username', value)

class RenameTagResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RenameTag Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class RenameTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RenameTagResultSet(response, path)
