# -*- coding: utf-8 -*-

###############################################################################
#
# PutBucketLogging
# Sets the logging parameters for a bucket and specifies permissions for who can view and modify the logging parameters. Can also be used to disable logging.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutBucketLogging(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutBucketLogging Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutBucketLogging')


    def new_input_set(self):
        return PutBucketLoggingInputSet()

    def _make_result_set(self, result, path):
        return PutBucketLoggingResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutBucketLoggingChoreographyExecution(session, exec_id, path)

class PutBucketLoggingInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutBucketLogging
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BucketLoggingStatus(self, value):
        """
        Set the value of the BucketLoggingStatus input for this Choreo. ((optional, xml) An XML file that allows custom config, this can be used as an alternative to the other bucket logging inputs. If provided, the Choreo will ignore all inputs except your AWS Key/Secret and BucketName.)
        """
        InputSet._set_input(self, 'BucketLoggingStatus', value)
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that you are setting the logging for.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((conditional, string) The email address of the person being granted logging permissions.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_Permission(self, value):
        """
        Set the value of the Permission input for this Choreo. ((conditional, string) The logging permissions given to the Grantee for the bucket. Valid values are: FULL_CONTROL, READ, or WRITE.)
        """
        InputSet._set_input(self, 'Permission', value)
    def set_TargetBucket(self, value):
        """
        Set the value of the TargetBucket input for this Choreo. ((conditional, string) The name of the target bucket. To disable logging, just leave this blank.)
        """
        InputSet._set_input(self, 'TargetBucket', value)
    def set_TargetPrefix(self, value):
        """
        Set the value of the TargetPrefix input for this Choreo. ((conditional, string) Lets you specify a prefix for the keys that the log files will be stored under. Defaults to "/logs")
        """
        InputSet._set_input(self, 'TargetPrefix', value)

class PutBucketLoggingResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutBucketLogging Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. A successful execution returns an empty 200 response.)
        """
        return self._output.get('Response', None)

class PutBucketLoggingChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutBucketLoggingResultSet(response, path)
