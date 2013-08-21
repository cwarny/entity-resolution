# -*- coding: utf-8 -*-

###############################################################################
#
# RemoveWhiteSpace
# Returns the specified formatted text as a compact string with no new lines, tabs, or preceding/trailing white space.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RemoveWhiteSpace(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RemoveWhiteSpace Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Formatting/RemoveWhiteSpace')


    def new_input_set(self):
        return RemoveWhiteSpaceInputSet()

    def _make_result_set(self, result, path):
        return RemoveWhiteSpaceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RemoveWhiteSpaceChoreographyExecution(session, exec_id, path)

class RemoveWhiteSpaceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RemoveWhiteSpace
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FormattedText(self, value):
        """
        Set the value of the FormattedText input for this Choreo. ((required, multiline) The formatted text that should have line breaks and tabs removed.)
        """
        InputSet._set_input(self, 'FormattedText', value)

class RemoveWhiteSpaceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RemoveWhiteSpace Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_CompactText(self):
        """
        Retrieve the value for the "CompactText" output from this Choreo execution. ((string) )
        """
        return self._output.get('CompactText', None)

class RemoveWhiteSpaceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RemoveWhiteSpaceResultSet(response, path)
