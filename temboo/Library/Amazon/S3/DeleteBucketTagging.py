# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteBucketTagging
# Removes a billing tag set from the specified bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteBucketTagging(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteBucketTagging Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/DeleteBucketTagging')


    def new_input_set(self):
        return DeleteBucketTaggingInputSet()

    def _make_result_set(self, result, path):
        return DeleteBucketTaggingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteBucketTaggingChoreographyExecution(session, exec_id, path)

class DeleteBucketTaggingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteBucketTagging
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to remove tags from.)
        """
        InputSet._set_input(self, 'BucketName', value)

class DeleteBucketTaggingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteBucketTagging Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. A successful execution returns an empty 204 response.)
        """
        return self._output.get('Response', None)

class DeleteBucketTaggingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteBucketTaggingResultSet(response, path)
