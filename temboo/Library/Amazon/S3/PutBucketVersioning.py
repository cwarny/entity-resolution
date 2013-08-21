# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketVersioning
# Sets the versioning state of an existing bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutBucketVersioning(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketVersioning Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketVersioning')


    def new_input_set(self):
        return PutBucketVersioningInputSet()

    def _make_result_set(self, result, path):
        return PutBucketVersioningResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketVersioningChoreographyExecution(session, exec_id, path)

class PutBucketVersioningInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketVersioning
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to create a notification for.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((required, string) Indicates whether or not the bucket has versioning enabled. Valid values are: Enabled or Suspended (case-sensitive).)
        """
        InputSet._set_input(self, 'Status', value)

class PutBucketVersioningResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketVersioning Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful execution, no content is returned and this output variable should be empty.)
        """
        return self._output.get('Response', None)

class PutBucketVersioningChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketVersioningResultSet(response, path)
