# -*- coding: utf-8 -*-

###############################################################################
#
# AllExercises
# Retrieves a list of all exercises in the Khan Academy library.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AllExercises(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AllExercises Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/KhanAcademy/Exercises/AllExercises')


    def new_input_set(self):
        return AllExercisesInputSet()

    def _make_result_set(self, result, path):
        return AllExercisesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AllExercisesChoreographyExecution(session, exec_id, path)

class AllExercisesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AllExercises
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    pass

class AllExercisesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AllExercises Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Khan Academy.)
        """
        return self._output.get('Response', None)

class AllExercisesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AllExercisesResultSet(response, path)
