# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketTagging
# Adds a set of billing tags to an existing bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutBucketTagging(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketTagging Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketTagging')


    def new_input_set(self):
        return PutBucketTaggingInputSet()

    def _make_result_set(self, result, path):
        return PutBucketTaggingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketTaggingChoreographyExecution(session, exec_id, path)

class PutBucketTaggingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketTagging
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Tags(self, value):
        """
        Set the value of the Tags input for this Choreo. ((optional, xml) An XML file describing the key/values for the tag set. Note - if you use this input, the Key and Value input variables will be ignored.)
        """
        InputSet._set_input(self, 'Tags', value)
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket to add tags to.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((conditional, string) The tag name.)
        """
        InputSet._set_input(self, 'Key', value)
    def set_Value(self, value):
        """
        Set the value of the Value input for this Choreo. ((conditional, string) The tag value.)
        """
        InputSet._set_input(self, 'Value', value)

class PutBucketTaggingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketTagging Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Stores the response from Amazon. Note that for a successful execution, no content is returned and this output variable should be empty.)
        """
        return self._output.get('Response', None)

class PutBucketTaggingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketTaggingResultSet(response, path)
