# -*- coding: utf-8 -*-

###############################################################################
#
# Update
# Updates the metadata or content of an existing file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Google.Drive.GoogleFile import GoogleFile

import json

class Update(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Update Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Files/Update')


    def new_input_set(self):
        return UpdateInputSet()

    def _make_result_set(self, result, path):
        return UpdateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateChoreographyExecution(session, exec_id, path)

class UpdateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Update
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RequestBody(self, value):
        """
        Set the value of the RequestBody input for this Choreo. ((conditional, json) A JSON representation of fields in a file resource. File metadata information (such as the title) can be updated using this input. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'RequestBody', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((conditional, string) The Content-Type of the file that is being updated (i.e. image/jpeg). Required if modifying the file content.)
        """
        InputSet._set_input(self, 'ContentType', value)
    def set_Convert(self, value):
        """
        Set the value of the Convert input for this Choreo. ((optional, boolean) Whether to convert this file to the corresponding Google Docs format. (Default: false).)
        """
        InputSet._set_input(self, 'Convert', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying which fields to include in a partial response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FileContent(self, value):
        """
        Set the value of the FileContent input for this Choreo. ((conditional, string) The new Base64 encoded contents of the file that is being updated.)
        """
        InputSet._set_input(self, 'FileContent', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The id of the file to update.)
        """
        InputSet._set_input(self, 'FileID', value)
    def set_OCR(self, value):
        """
        Set the value of the OCR input for this Choreo. ((optional, boolean) Whether to attempt OCR on .jpg, .png, .gif, or .pdf uploads. (Default: false))
        """
        InputSet._set_input(self, 'OCR', value)
    def set_OcrLanguage(self, value):
        """
        Set the value of the OcrLanguage input for this Choreo. ((optional, string) If ocr is true, hints at the language to use. Valid values are ISO 639-1 codes.)
        """
        InputSet._set_input(self, 'OcrLanguage', value)
    def set_Pinned(self, value):
        """
        Set the value of the Pinned input for this Choreo. ((optional, boolean) Whether to pin the new revision. (Default: false).)
        """
        InputSet._set_input(self, 'Pinned', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_SetModifiedDate(self, value):
        """
        Set the value of the SetModifiedDate input for this Choreo. ((optional, boolean) Whether to set the modified date with the supplied modified date.)
        """
        InputSet._set_input(self, 'SetModifiedDate', value)
    def set_SourceLanguage(self, value):
        """
        Set the value of the SourceLanguage input for this Choreo. ((optional, string) The language of the original file to be translated.)
        """
        InputSet._set_input(self, 'SourceLanguage', value)
    def set_TargetLanguage(self, value):
        """
        Set the value of the TargetLanguage input for this Choreo. ((optional, string) Target language to translate the file to. If no sourceLanguage is provided, the API will attempt to detect the language.)
        """
        InputSet._set_input(self, 'TargetLanguage', value)
    def set_TimedTextLanguage(self, value):
        """
        Set the value of the TimedTextLanguage input for this Choreo. ((optional, string) The language of the timed text.)
        """
        InputSet._set_input(self, 'TimedTextLanguage', value)
    def set_TimedTextTrackName(self, value):
        """
        Set the value of the TimedTextTrackName input for this Choreo. ((optional, string) The timed text track name.)
        """
        InputSet._set_input(self, 'TimedTextTrackName', value)
    def set_UpdateViewedDate(self, value):
        """
        Set the value of the UpdateViewedDate input for this Choreo. ((optional, boolean) Whether to update the view date after successfully updating the file.)
        """
        InputSet._set_input(self, 'UpdateViewedDate', value)


class UpdateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Update Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def getFile(self):
        """
        A Google Drive file resource
        """
        return GoogleFile(self.getJSONFromString(self._output.get('Response', [])))

class UpdateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateResultSet(response, path)
