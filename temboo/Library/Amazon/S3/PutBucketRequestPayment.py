# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketRequestPayment
# Sets the request payment configuration of a bucket. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutBucketRequestPayment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketRequestPayment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketRequestPayment')


    def new_input_set(self):
        return PutBucketRequestPaymentInputSet()

    def _make_result_set(self, result, path):
        return PutBucketRequestPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketRequestPaymentChoreographyExecution(session, exec_id, path)

class PutBucketRequestPaymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketRequestPayment
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
    def set_BucketName(self, value):
        """
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to create a request payment configuration for.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_Payer(self, value):
        """
        Set the value of the Payer input for this Choreo. ((required, string) Specifies who pays for the download and request fees. Valid values:  Requester or BucketOwner.)
        """
        InputSet._set_input(self, 'Payer', value)

class PutBucketRequestPaymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketRequestPayment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful execution, no content is returned and this output variable should be empty.)
        """
        return self._output.get('Response', None)

class PutBucketRequestPaymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketRequestPaymentResultSet(response, path)
