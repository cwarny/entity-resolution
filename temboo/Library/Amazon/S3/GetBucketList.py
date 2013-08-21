# -*- coding: utf-8 -*-

###############################################################################
#
# GetBucketList
# Retrieves a list of the items that are in a specified Amazon S3 storage bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetBucketList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBucketList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/GetBucketList')


    def new_input_set(self):
        return GetBucketListInputSet()

    def _make_result_set(self, result, path):
        return GetBucketListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBucketListChoreographyExecution(session, exec_id, path)

class GetBucketListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBucketList
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that contains the list of objects that you want to retrieve.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_Delimiter(self, value):
        """
        Set the value of the Delimiter input for this Choreo. ((optional, string) A delimiter is a character you use to group keys. All keys that contain the delimiter are grouped under a single result element, Common Prefixes. For more information see Amazon documentation.)
        """
        InputSet._set_input(self, 'Delimiter', value)
    def set_Marker(self, value):
        """
        Set the value of the Marker input for this Choreo. ((optional, string) Specifies the key to start with when listing objects in a bucket. Amazon S3 lists objects in alphabetical order.)
        """
        InputSet._set_input(self, 'Marker', value)
    def set_MaxKeys(self, value):
        """
        Set the value of the MaxKeys input for this Choreo. ((optional, string) Lowers the max number of keys returned in the response from 1000 to specified value.The response will contain the key IsTruncated (true) if there are additional keys that exceed the # of MaxKeys.)
        """
        InputSet._set_input(self, 'MaxKeys', value)
    def set_Prefix(self, value):
        """
        Set the value of the Prefix input for this Choreo. ((optional, string) Limits the response to keys that begin with the specified prefix - useful for separating a bucket into different groupings of keys. Ex: specify 'test' to get a list of objects starting with 'test'.)
        """
        InputSet._set_input(self, 'Prefix', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetBucketListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBucketList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetBucketListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBucketListResultSet(response, path)
