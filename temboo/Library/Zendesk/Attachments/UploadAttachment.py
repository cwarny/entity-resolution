# -*- coding: utf-8 -*-

###############################################################################
#
# UploadAttachment
# Uploads a file to be used as an attachment to a ticket.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UploadAttachment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UploadAttachment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Attachments/UploadAttachment')


    def new_input_set(self):
        return UploadAttachmentInputSet()

    def _make_result_set(self, result, path):
        return UploadAttachmentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadAttachmentChoreographyExecution(session, exec_id, path)

class UploadAttachmentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UploadAttachment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email address you use to login to your Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_ExistingToken(self, value):
        """
        Set the value of the ExistingToken input for this Choreo. ((optional, string) Allows you to pass in an existing token when uploading multiple attachments to associate with a ticket creation.)
        """
        InputSet._set_input(self, 'ExistingToken', value)
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((required, string) The Base64 encoded file contents of the attachment you want to upload.)
        """
        InputSet._set_input(self, 'FileContents', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) )
        """
        InputSet._set_input(self, 'FileName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Zendesk password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) Your Zendesk domain and subdomain (i.e. support.temboo.com or temboo.zendesk.com).)
        """
        InputSet._set_input(self, 'Server', value)


class UploadAttachmentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadAttachment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((string) The token returned from Zendesk for the upload. This can be passed to the ExistingToken input when associating  multiple attachments to the same upload token.)
        """
        return self._output.get('Token', None)

class UploadAttachmentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadAttachmentResultSet(response, path)
