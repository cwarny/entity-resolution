# -*- coding: utf-8 -*-

###############################################################################
#
# CopyObject
# Makes a copy of an existing object in S3 Storage.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CopyObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CopyObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/CopyObject')


    def new_input_set(self):
        return CopyObjectInputSet()

    def _make_result_set(self, result, path):
        return CopyObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CopyObjectChoreographyExecution(session, exec_id, path)

class CopyObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CopyObject
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that will be the file destination.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_CannedACL(self, value):
        """
        Set the value of the CannedACL input for this Choreo. ((optional, string) By default all objects are private (only owner has full access control). Valid values: private, public-read, public-read-write, authenticated-read, bucket-owner-read, bucket-owner-full-control.)
        """
        InputSet._set_input(self, 'CannedACL', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, string) ContentType. Default is application/octet-stream.)
        """
        InputSet._set_input(self, 'ContentType', value)
    def set_FileToCopy(self, value):
        """
        Set the value of the FileToCopy input for this Choreo. ((required, string) The name of the file to copy.)
        """
        InputSet._set_input(self, 'FileToCopy', value)
    def set_IfMatch(self, value):
        """
        Set the value of the IfMatch input for this Choreo. ((optional, string) Copies the object if its entity tag (ETag) matches the specified tag; otherwise returns a 412 HTTP status code error (failed precondition).)
        """
        InputSet._set_input(self, 'IfMatch', value)
    def set_IfModifiedSince(self, value):
        """
        Set the value of the IfModifiedSince input for this Choreo. ((optional, date) Copies if it has been modified since the specified time; otherwise returns a 412 HTTP status code error (failed precondition). Must be valid HTTP date. Can be used with IfMatch only.)
        """
        InputSet._set_input(self, 'IfModifiedSince', value)
    def set_IfNoneMatch(self, value):
        """
        Set the value of the IfNoneMatch input for this Choreo. ((optional, string) Copies the object if its entity tag (ETag) is different from the specified tag; otherwise returns a 412 HTTP status code error (failed precondition).)
        """
        InputSet._set_input(self, 'IfNoneMatch', value)
    def set_IfUnmodifiedSince(self, value):
        """
        Set the value of the IfUnmodifiedSince input for this Choreo. ((optional, date) Copies if it hasn't been modified since the specified time; otherwise returns a 412 HTTP status code error (failed precondition). Must be valid HTTP date. Can be used with IfMatch or IfNoneMatch only.)
        """
        InputSet._set_input(self, 'IfUnmodifiedSince', value)
    def set_NewFileName(self, value):
        """
        Set the value of the NewFileName input for this Choreo. ((required, string) The file name for the new copy.)
        """
        InputSet._set_input(self, 'NewFileName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ServerSideEncryption(self, value):
        """
        Set the value of the ServerSideEncryption input for this Choreo. ((optional, string) Specifies the server-side encryption algorithm to use when Amazon S3 creates the target object. Valid value: AES256.)
        """
        InputSet._set_input(self, 'ServerSideEncryption', value)
    def set_StorageClass(self, value):
        """
        Set the value of the StorageClass input for this Choreo. ((optional, string) Enables RRS customers to store their noncritical, reproducible data at lower levels of redundancy than Amazon S3's standard storage. Valid Values: STANDARD (default), REDUCED_REDUNDANCY.)
        """
        InputSet._set_input(self, 'StorageClass', value)
    def set_WebsiteRedirectLocation(self, value):
        """
        Set the value of the WebsiteRedirectLocation input for this Choreo. ((optional, string) If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Ex: /anotherPage.html, http://www.page.com. Length limit: 2 K.)
        """
        InputSet._set_input(self, 'WebsiteRedirectLocation', value)


class CopyObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CopyObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CopyObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CopyObjectResultSet(response, path)
