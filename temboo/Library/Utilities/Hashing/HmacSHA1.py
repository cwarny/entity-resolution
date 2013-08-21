# -*- coding: utf-8 -*-

###############################################################################
#
# HmacSHA1
# Generates a SHA1-encrypted HMAC signature for the specified message text using the specified secret key.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class HmacSHA1(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HmacSHA1 Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Hashing/HmacSHA1')


    def new_input_set(self):
        return HmacSHA1InputSet()

    def _make_result_set(self, result, path):
        return HmacSHA1ResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HmacSHA1ChoreographyExecution(session, exec_id, path)

class HmacSHA1InputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HmacSHA1
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) The secret key used to generate the SHA1-encrypted HMAC signature.)
        """
        InputSet._set_input(self, 'Key', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text that should be SHA1-encrypted.)
        """
        InputSet._set_input(self, 'Text', value)

class HmacSHA1ResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HmacSHA1 Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_HmacSignature(self):
        """
        Retrieve the value for the "HmacSignature" output from this Choreo execution. ((string) The HMAC Signature for the specified string.)
        """
        return self._output.get('HmacSignature', None)

class HmacSHA1ChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HmacSHA1ResultSet(response, path)
