# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucket
# Creates a new bucket in your Amazon S3 account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutBucket(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucket Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucket')


    def new_input_set(self):
        return PutBucketInputSet()

    def _make_result_set(self, result, path):
        return PutBucketResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketChoreographyExecution(session, exec_id, path)

class PutBucketInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucket
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that will be created.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_CannedACL(self, value):
        """
        Set the value of the CannedACL input for this Choreo. ((optional, string) By default all objects are private (only owner has full access control). Valid values: private, public-read, public-read-write, authenticated-read, bucket-owner-read, bucket-owner-full-control.)
        """
        InputSet._set_input(self, 'CannedACL', value)
    def set_LocationConstraint(self, value):
        """
        Set the value of the LocationConstraint input for this Choreo. ((optional, string) The region to create the bucket in. Valid Values: EU, eu-west-1, us-west-1, us-west-2, ap-southeast-1, ap-southeast-2, ap-northeast-1, sa-east-1, empty string (Default US Classic Region). )
        """
        InputSet._set_input(self, 'LocationConstraint', value)

class PutBucketResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucket Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. Note that no content is returned for successful uploads.)
        """
        return self._output.get('Response', None)

class PutBucketChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketResultSet(response, path)
