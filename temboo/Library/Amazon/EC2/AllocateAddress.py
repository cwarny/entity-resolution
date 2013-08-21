# -*- coding: utf-8 -*-

###############################################################################
#
# AllocateAddress
# Acquires an Elastic IP address for use with your AWS account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AllocateAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AllocateAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/AllocateAddress')


    def new_input_set(self):
        return AllocateAddressInputSet()

    def _make_result_set(self, result, path):
        return AllocateAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AllocateAddressChoreographyExecution(session, exec_id, path)

class AllocateAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AllocateAddress
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
    def set_Domain(self, value):
        """
        Set the value of the Domain input for this Choreo. ((conditional, string) Set to "vpc" to allocate the address for use with instances in a VPC.)
        """
        InputSet._set_input(self, 'Domain', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class AllocateAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AllocateAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class AllocateAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AllocateAddressResultSet(response, path)
