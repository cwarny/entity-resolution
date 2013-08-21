# -*- coding: utf-8 -*-

###############################################################################
#
# Checksum
# Returns a checksum of the specified text calculated using the specified algorithm. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Checksum(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Checksum Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Hashing/Checksum')


    def new_input_set(self):
        return ChecksumInputSet()

    def _make_result_set(self, result, path):
        return ChecksumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChecksumChoreographyExecution(session, exec_id, path)

class ChecksumInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Checksum
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Algorithm(self, value):
        """
        Set the value of the Algorithm input for this Choreo. ((required, string) Algorithm used to calculate the checksum. Valid values are: FIX44,  MD5+BASE64, or MD5+HEX (the default). MD5+BASE64 and MD5+HEX return the result in Base64 and hexadecimal encoding, respectively.)
        """
        InputSet._set_input(self, 'Algorithm', value)
    def set_Base64DecodeValue(self, value):
        """
        Set the value of the Base64DecodeValue input for this Choreo. ((optional, boolean) Setting this parameter to 1 indicates that the Text is Base64 encoded, and that the choreo should decode the value before calculating the checksum. Defaults to 0.)
        """
        InputSet._set_input(self, 'Base64DecodeValue', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text to return a checksum for.)
        """
        InputSet._set_input(self, 'Text', value)

class ChecksumResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Checksum Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Checksum(self):
        """
        Retrieve the value for the "Checksum" output from this Choreo execution. ((string) The checksum result.)
        """
        return self._output.get('Checksum', None)

class ChecksumChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ChecksumResultSet(response, path)
