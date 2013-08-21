# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketPolicy
# Allows you to add to or replace a policy on a bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutBucketPolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketPolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketPolicy')


    def new_input_set(self):
        return PutBucketPolicyInputSet()

    def _make_result_set(self, result, path):
        return PutBucketPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketPolicyChoreographyExecution(session, exec_id, path)

class PutBucketPolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketPolicy
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Policy(self, value):
        """
        Set the value of the Policy input for this Choreo. ((required, json) A JSON string containing the policy information.  See Choreo documentation for a sample JSON policy.)
        """
        InputSet._set_input(self, 'Policy', value)
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to create or update a policy for.)
        """
        InputSet._set_input(self, 'BucketName', value)

class PutBucketPolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketPolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful policy creation, no content is returned and this output variable is empty.)
        """
        return self._output.get('Response', None)

class PutBucketPolicyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketPolicyResultSet(response, path)
