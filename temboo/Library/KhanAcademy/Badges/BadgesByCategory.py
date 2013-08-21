# -*- coding: utf-8 -*-

###############################################################################
#
# BadgesByCategory
# Retrieves all badges for a specific category.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class BadgesByCategory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the BadgesByCategory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Badges/BadgesByCategory')


    def new_input_set(self):
        return BadgesByCategoryInputSet()

    def _make_result_set(self, result, path):
        return BadgesByCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BadgesByCategoryChoreographyExecution(session, exec_id, path)

class BadgesByCategoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the BadgesByCategory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CategoryID(self, value):
        """
        Set the value of the CategoryID input for this Choreo. ((required, string) The category of badges to retrieve. A full list of CategoryIds can be obtained by running the AllCategories Choreo.)
        """
        InputSet._set_input(self, 'CategoryID', value)

class BadgesByCategoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the BadgesByCategory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class BadgesByCategoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BadgesByCategoryResultSet(response, path)
