# -*- coding: utf-8 -*-

###############################################################################
#
# SendMail
# Allows you to send emails.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SendMail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendMail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SendGrid/WebAPI/Mail/SendMail')


    def new_input_set(self):
        return SendMailInputSet()

    def _make_result_set(self, result, path):
        return SendMailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendMailChoreographyExecution(session, exec_id, path)

class SendMailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendMail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((optional, string) The Base64-encoded contents of the file you want to attach.)
        """
        InputSet._set_input(self, 'FileContents', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from SendGrid.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APIUser(self, value):
        """
        Set the value of the APIUser input for this Choreo. ((required, string) The username registered with SendGrid.)
        """
        InputSet._set_input(self, 'APIUser', value)
    def set_BCC(self, value):
        """
        Set the value of the BCC input for this Choreo. ((optional, string) Enter a BCC recipient.  Multiple recipients can also be passed in as an array of email addresses.)
        """
        InputSet._set_input(self, 'BCC', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) The timestamp of the Block records. Enter 1 to return a date in a MySQL timestamp format - YYYY-MM-DD HH:MM:SS)
        """
        InputSet._set_input(self, 'Date', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((optional, string) The name of the file you are attaching to your email.)
        """
        InputSet._set_input(self, 'FileName', value)
    def set_FromName(self, value):
        """
        Set the value of the FromName input for this Choreo. ((optional, string) The name to be appended to the from email.  For example, your company name, or your name.)
        """
        InputSet._set_input(self, 'FromName', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) The originating email address.  Must be from your domain.)
        """
        InputSet._set_input(self, 'From', value)
    def set_HTML(self, value):
        """
        Set the value of the HTML input for this Choreo. ((conditional, string) The HTML to be used in the body of your email message. Required unless specifying a plain text body in the Text input.)
        """
        InputSet._set_input(self, 'HTML', value)
    def set_Headers(self, value):
        """
        Set the value of the Headers input for this Choreo. ((optional, json) The collection of key/value pairs in JSON format. Each key represents a header name and the value the header value. For example: {"X-Accept-Language": "en", "X-Mailer": "MyApp"})
        """
        InputSet._set_input(self, 'Headers', value)
    def set_ReplyTo(self, value):
        """
        Set the value of the ReplyTo input for this Choreo. ((optional, string) The email address to append to the reply-to field of your email.)
        """
        InputSet._set_input(self, 'ReplyTo', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format of the response from SendGrid, in either json, or xml.  Default is set to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Subject(self, value):
        """
        Set the value of the Subject input for this Choreo. ((required, string) The subject of the email message.)
        """
        InputSet._set_input(self, 'Subject', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((conditional, string) The text of the email message. Required unless providing the message body using the HTML input.)
        """
        InputSet._set_input(self, 'Text', value)
    def set_ToName(self, value):
        """
        Set the value of the ToName input for this Choreo. ((optional, string) The name of the email recipient.)
        """
        InputSet._set_input(self, 'ToName', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) The valid recipient email address.  Multiple addresses can be entered as elements of an array.)
        """
        InputSet._set_input(self, 'To', value)
    def set_XSMTPAPI(self, value):
        """
        Set the value of the XSMTPAPI input for this Choreo. ((optional, json) Must be valid JSON format.  See here for additional info: http://docs.sendgrid.com/documentation/api/smtp-api/)
        """
        InputSet._set_input(self, 'XSMTPAPI', value)


class SendMailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendMail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from SendGrid. The format corresponds to the ResponseFormat input. Default is json.)
        """
        return self._output.get('Response', None)

class SendMailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendMailResultSet(response, path)
