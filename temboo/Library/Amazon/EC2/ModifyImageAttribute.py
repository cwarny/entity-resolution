# -*- coding: utf-8 -*-

###############################################################################
#
# ModifyImageAttribute
# Modifies an attribute of an AMI.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ModifyImageAttribute(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ModifyImageAttribute Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/EC2/ModifyImageAttribute')


    def new_input_set(self):
        return ModifyImageAttributeInputSet()

    def _make_result_set(self, result, path):
        return ModifyImageAttributeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ModifyImageAttributeChoreographyExecution(session, exec_id, path)

class ModifyImageAttributeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ModifyImageAttribute
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
    def set_AddGroup(self, value):
        """
        Set the value of the AddGroup input for this Choreo. ((optional, string) Adds the specified group to the image's list of launch permissions. The only valid value is "all".)
        """
        InputSet._set_input(self, 'AddGroup', value)
    def set_AddUserId(self, value):
        """
        Set the value of the AddUserId input for this Choreo. ((optional, string) Adds the specified AWS account ID to the AMI's list of launch permissions.)
        """
        InputSet._set_input(self, 'AddUserId', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) Changes the AMI's description to the specified value.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_ImageId(self, value):
        """
        Set the value of the ImageId input for this Choreo. ((required, string) The AMI ID.)
        """
        InputSet._set_input(self, 'ImageId', value)
    def set_ProductCode(self, value):
        """
        Set the value of the ProductCode input for this Choreo. ((optional, string) Adds the specified product code to the specified Amazon S3-backed AMI. Once you add a product code to an AMI, it can't be removed.)
        """
        InputSet._set_input(self, 'ProductCode', value)
    def set_RemoveGroup(self, value):
        """
        Set the value of the RemoveGroup input for this Choreo. ((optional, string) Removes the specified group from the image's list of launch permissions. The only valid value is "all".)
        """
        InputSet._set_input(self, 'RemoveGroup', value)
    def set_RemoveUserId(self, value):
        """
        Set the value of the RemoveUserId input for this Choreo. ((optional, string) Removes the specified AWS account ID from the AMI's list of launch permissions.)
        """
        InputSet._set_input(self, 'RemoveUserId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ModifyImageAttributeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ModifyImageAttribute Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ModifyImageAttributeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ModifyImageAttributeResultSet(response, path)
