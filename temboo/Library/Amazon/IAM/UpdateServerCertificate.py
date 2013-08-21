# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateServerCertificate
# Updates the name and/or the path of the specified server certificate.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateServerCertificate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateServerCertificate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/UpdateServerCertificate')


    def new_input_set(self):
        return UpdateServerCertificateInputSet()

    def _make_result_set(self, result, path):
        return UpdateServerCertificateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateServerCertificateChoreographyExecution(session, exec_id, path)

class UpdateServerCertificateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateServerCertificate
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
    def set_NewPath(self, value):
        """
        Set the value of the NewPath input for this Choreo. ((conditional, string) The new path for the server certificate. Include this only if you are updating the server certificate's path.)
        """
        InputSet._set_input(self, 'NewPath', value)
    def set_NewServerCertificateName(self, value):
        """
        Set the value of the NewServerCertificateName input for this Choreo. ((conditional, string) The new name for the server certificate. Include this only if you are updating the server certificate's name.)
        """
        InputSet._set_input(self, 'NewServerCertificateName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ServerCertificateName(self, value):
        """
        Set the value of the ServerCertificateName input for this Choreo. ((required, string) The name for the server certificate. Do not include the path in this value.)
        """
        InputSet._set_input(self, 'ServerCertificateName', value)

class UpdateServerCertificateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateServerCertificate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateServerCertificateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateServerCertificateResultSet(response, path)
