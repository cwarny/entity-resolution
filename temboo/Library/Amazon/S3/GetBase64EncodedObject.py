# -*- coding: utf-8 -*-

###############################################################################
#
# GetBase64EncodedObject
# Retrieves a specified item from an Amazon S3 bucket, returns the file content as base64-encoded data, and returns the values of key response headers as output variables if available.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetBase64EncodedObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetBase64EncodedObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/S3/GetBase64EncodedObject')


    def new_input_set(self):
        return GetBase64EncodedObjectInputSet()

    def _make_result_set(self, result, path):
        return GetBase64EncodedObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetBase64EncodedObjectChoreographyExecution(session, exec_id, path)

class GetBase64EncodedObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetBase64EncodedObject
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
        Set the value of the BucketName input for this Choreo. ((required, string) The name of the bucket that contains the object to retrieve.)
        """
        InputSet._set_input(self, 'BucketName', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the file to retrieve.)
        """
        InputSet._set_input(self, 'FileName', value)
    def set_IfMatch(self, value):
        """
        Set the value of the IfMatch input for this Choreo. ((optional, string) Returns the object only if its entity tag (ETag) is the same as the one specified, otherwise returns a 412 (precondition failed) error.)
        """
        InputSet._set_input(self, 'IfMatch', value)
    def set_IfModifiedSince(self, value):
        """
        Set the value of the IfModifiedSince input for this Choreo. ((optional, date) Returns the object only if it has been modified since the specific time, otherwise returns a 304 (not modified) error.)
        """
        InputSet._set_input(self, 'IfModifiedSince', value)
    def set_IfNoneMatch(self, value):
        """
        Set the value of the IfNoneMatch input for this Choreo. ((optional, string) Returns the object only if its entity tag (ETag) is different from the one specified, otherwise retuns a 304 (not modified) error. Will not work correctly with IfModifiedSince.)
        """
        InputSet._set_input(self, 'IfNoneMatch', value)
    def set_IfUnmodifiedSince(self, value):
        """
        Set the value of the IfUnmodifiedSince input for this Choreo. ((optional, date) Returns the object only if it has not been modified since the specified time, otherwise returns a 412 (precondition failed) error.)
        """
        InputSet._set_input(self, 'IfUnmodifiedSince', value)
    def set_Range(self, value):
        """
        Set the value of the Range input for this Choreo. ((optional, string) Downloads the specific range of bytes of an object. Ex: 0-9 (returns the first 10 bytes of an object), 100-1000, etc. If the range value exceeds the end of file, it will return up to the end of file.)
        """
        InputSet._set_input(self, 'Range', value)

class GetBase64EncodedObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetBase64EncodedObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_DeleteMarker(self):
        """
        Retrieve the value for the "DeleteMarker" output from this Choreo execution. ((boolean) Returns true if the object retrieved was a Delete Marker otherwise no value.)
        """
        return self._output.get('DeleteMarker', None)
    def get_Expiration(self):
        """
        Retrieve the value for the "Expiration" output from this Choreo execution. ((string) Appears if the object expiration is configured. It includes expiry-date and URL-encoded rule-id key value pairs providing object expiration information.)
        """
        return self._output.get('Expiration', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The base64-encoded contents of the file you are retrieving.)
        """
        return self._output.get('Response', None)
    def get_Restore(self):
        """
        Retrieve the value for the "Restore" output from this Choreo execution. ((string) Provides information about the object restoration operation and expiration time of the restored object copy.)
        """
        return self._output.get('Restore', None)
    def get_ServerSideEncryption(self):
        """
        Retrieve the value for the "ServerSideEncryption" output from this Choreo execution. ((string) If the object is stored using server-side encryption, response includes this header with value of the encryption algorithm used. Valid Values: AES256.)
        """
        return self._output.get('ServerSideEncryption', None)
    def get_VersionID(self):
        """
        Retrieve the value for the "VersionID" output from this Choreo execution. ((string) Returns the version ID of the retrieved object if it has a unique version ID.)
        """
        return self._output.get('VersionID', None)
    def get_WebsiteRedirectLocation(self):
        """
        Retrieve the value for the "WebsiteRedirectLocation" output from this Choreo execution. ((string) For a bucket configured as a website, this metadata can be set so the website will evaluate the request for the object as a 301 redirect to another object in the same bucket or an external URL.)
        """
        return self._output.get('WebsiteRedirectLocation', None)

class GetBase64EncodedObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetBase64EncodedObjectResultSet(response, path)
