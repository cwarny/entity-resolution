# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteTag
# Deletes a specified tag.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteTag(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteTag Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Delicious/DeleteTag')


    def new_input_set(self):
        return DeleteTagInputSet()

    def _make_result_set(self, result, path):
        return DeleteTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteTagChoreographyExecution(session, exec_id, path)

class DeleteTagInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteTag
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password that corresponds to the specified Delicious account username.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((required, string) The tag to delete.)
        """
        InputSet._set_input(self, 'Tag', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Delicious account username.)
        """
        InputSet._set_input(self, 'Username', value)

class DeleteTagResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteTag Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Delicious.)
        """
        return self._output.get('Response', None)

class DeleteTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteTagResultSet(response, path)
