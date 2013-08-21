# -*- coding: utf-8 -*-

###############################################################################
#
# PasswordCriteria
# Verifies that a given password matches a standard pattern for passwords.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PasswordCriteria(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PasswordCriteria Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Validation/PasswordCriteria')


    def new_input_set(self):
        return PasswordCriteriaInputSet()

    def _make_result_set(self, result, path):
        return PasswordCriteriaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PasswordCriteriaChoreographyExecution(session, exec_id, path)

class PasswordCriteriaInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PasswordCriteria
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_MaxLength(self, value):
        """
        Set the value of the MaxLength input for this Choreo. ((optional, integer) The max length you want to allow for the password. Defaults to 14.)
        """
        InputSet._set_input(self, 'MaxLength', value)
    def set_MinLength(self, value):
        """
        Set the value of the MinLength input for this Choreo. ((optional, integer) The minimum length you want to allow for the password. Defaults to 6.)
        """
        InputSet._set_input(self, 'MinLength', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The password to validate.)
        """
        InputSet._set_input(self, 'Password', value)

class PasswordCriteriaResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PasswordCriteria Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Match(self):
        """
        Retrieve the value for the "Match" output from this Choreo execution. ((string) Contains a string indicating the result of the match -- "valid" or "invalid".)
        """
        return self._output.get('Match', None)

class PasswordCriteriaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PasswordCriteriaResultSet(response, path)
