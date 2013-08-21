# -*- coding: utf-8 -*-

###############################################################################
#
# DisassociateAddress
# Disassociates an Elastic IP address from the instance or network interface it's associated with.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DisassociateAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DisassociateAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DisassociateAddress')


    def new_input_set(self):
        return DisassociateAddressInputSet()

    def _make_result_set(self, result, path):
        return DisassociateAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DisassociateAddressChoreographyExecution(session, exec_id, path)

class DisassociateAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DisassociateAddress
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
    def set_AssociationId(self, value):
        """
        Set the value of the AssociationId input for this Choreo. ((conditional, string) [EC2-VPC] The association ID corresponding to the Elastic IP address.)
        """
        InputSet._set_input(self, 'AssociationId', value)
    def set_PublicIp(self, value):
        """
        Set the value of the PublicIp input for this Choreo. ((conditional, string) [EC2-Classic] The Elastic IP address.)
        """
        InputSet._set_input(self, 'PublicIp', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class DisassociateAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DisassociateAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DisassociateAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DisassociateAddressResultSet(response, path)
