# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeImageAttribute
# Retrieves information about an attribute of an AMI.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DescribeImageAttribute(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeImageAttribute Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/DescribeImageAttribute')


    def new_input_set(self):
        return DescribeImageAttributeInputSet()

    def _make_result_set(self, result, path):
        return DescribeImageAttributeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeImageAttributeChoreographyExecution(session, exec_id, path)

class DescribeImageAttributeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DescribeImageAttribute
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
    def set_Attribute(self, value):
        """
        Set the value of the Attribute input for this Choreo. ((required, string) The AMI attribute to get. Valid Values are: description | kernel | ramdisk | launchPermission | productCodes | blockDeviceMapping.)
        """
        InputSet._set_input(self, 'Attribute', value)
    def set_ImageId(self, value):
        """
        Set the value of the ImageId input for this Choreo. ((required, string) The AMI ID.)
        """
        InputSet._set_input(self, 'ImageId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class DescribeImageAttributeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DescribeImageAttribute Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DescribeImageAttributeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DescribeImageAttributeResultSet(response, path)
