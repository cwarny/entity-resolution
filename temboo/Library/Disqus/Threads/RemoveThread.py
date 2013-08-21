# -*- coding: utf-8 -*-

###############################################################################
#
# RemoveThread
# Remove a thread.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RemoveThread(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RemoveThread Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Threads/RemoveThread')


    def new_input_set(self):
        return RemoveThreadInputSet()

    def _make_result_set(self, result, path):
        return RemoveThreadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RemoveThreadChoreographyExecution(session, exec_id, path)

class RemoveThreadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RemoveThread
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, integer) The forum ID of a thread that is to be removed.  Required if setting either ThreadByIdentification, or ThreadByLink.)
        """
        InputSet._set_input(self, 'Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((conditional, integer) The ID of a thread that is to be removed. Required unless specifying ThreadIdentifier or ThreadLink. If using this parameter, ThreadIdentifier cannot be set.)
        """
        InputSet._set_input(self, 'ThreadID', value)
    def set_ThreadIdentifier(self, value):
        """
        Set the value of the ThreadIdentifier input for this Choreo. ((optional, string) The identifier for the thread that is to be removed.  Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        InputSet._set_input(self, 'ThreadIdentifier', value)
    def set_ThreadLink(self, value):
        """
        Set the value of the ThreadLink input for this Choreo. ((optional, string) A link pointing to the thread that is to be removed. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        InputSet._set_input(self, 'ThreadLink', value)


class RemoveThreadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RemoveThread Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class RemoveThreadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RemoveThreadResultSet(response, path)
