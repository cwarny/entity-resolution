# -*- coding: utf-8 -*-

###############################################################################
#
# PutObject
# Uploads a file to your Amazon S3 storage bucket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class PutObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PutObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/PutObject')


    def new_input_set(self):
        return PutObjectInputSet()

    def _make_result_set(self, result, path):
        return PutObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PutObjectChoreographyExecution(session, exec_id, path)

class PutObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PutObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((required, string) The Base64-encoded file contents that you want to upload to an AmazonS3 bucket.)
        """
        InputSet._set_input(self, 'FileContents', value)
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
        Set the value of the ContentType input for this Choreo. ((optional, string) Sets the content-type (text/html, image/jpeg, etc.). Default is application/octet-stream.)
        """
        InputSet._set_input(self, 'ContentType', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the file to put in S3 Storage. Ex.: file.txt or folder/file.txt)
        """
        InputSet._set_input(self, 'FileName', value)
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
        Set the value of the WebsiteRedirectLocation input for this Choreo. ((optional, string) If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Ex: /anotherPage.html, http://www.page.com. Max length: 2 K.)
        """
        InputSet._set_input(self, 'WebsiteRedirectLocation', value)


class PutObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PutObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon. Note that no content is returned for successful uploads.)
        """
        return self._output.get('Response', None)

class PutObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PutObjectResultSet(response, path)
