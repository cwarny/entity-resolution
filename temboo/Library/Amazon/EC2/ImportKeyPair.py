# -*- coding: utf-8 -*-

###############################################################################
#
# ImportKeyPair
# Imports the public key from an RSA key pair that you created with a third-party tool.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ImportKeyPair(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ImportKeyPair Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/ImportKeyPair')


    def new_input_set(self):
        return ImportKeyPairInputSet()

    def _make_result_set(self, result, path):
        return ImportKeyPairResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ImportKeyPairChoreographyExecution(session, exec_id, path)

class ImportKeyPairInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ImportKeyPair
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_KeyName(self, value):
        """
        Set the value of the KeyName input for this Choreo. ((required, string) A unique name for the key pair.)
        """
        InputSet._set_input(self, 'KeyName', value)
    def set_PublicKeyMaterial(self, value):
        """
        Set the value of the PublicKeyMaterial input for this Choreo. ((required, string) The public key. You must Base64-encode the public key material before sending it to AWS.)
        """
        InputSet._set_input(self, 'PublicKeyMaterial', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ImportKeyPairResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ImportKeyPair Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ImportKeyPairChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ImportKeyPairResultSet(response, path)
