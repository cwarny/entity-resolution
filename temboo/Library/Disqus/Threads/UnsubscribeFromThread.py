# -*- coding: utf-8 -*-

###############################################################################
#
# UnsubscribeFromThread
# Unsubscribe from a thread.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UnsubscribeFromThread(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UnsubscribeFromThread Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Threads/UnsubscribeFromThread')


    def new_input_set(self):
        return UnsubscribeFromThreadInputSet()

    def _make_result_set(self, result, path):
        return UnsubscribeFromThreadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnsubscribeFromThreadChoreographyExecution(session, exec_id, path)

class UnsubscribeFromThreadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UnsubscribeFromThread
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The email address that will be unsubsribed from the thread.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, integer) The forum ID of a thread that is to be unsubscribed from. Required if setting either ThreadByIdentification, or ThreadByLink.)
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
        Set the value of the ThreadID input for this Choreo. ((conditional, integer) The ID of a thread that is to be unsubscribed from. Required unless specifying the ThreadIdentifier or ThreadLink. If using this parameter, ThreadIdentifier cannot be set.)
        """
        InputSet._set_input(self, 'ThreadID', value)
    def set_ThreadIdentifier(self, value):
        """
        Set the value of the ThreadIdentifier input for this Choreo. ((optional, string) The identifier for the thread that is to be unsubscribed from.  Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        InputSet._set_input(self, 'ThreadIdentifier', value)
    def set_ThreadLink(self, value):
        """
        Set the value of the ThreadLink input for this Choreo. ((optional, string) A link pointing to the thread that is to be unsubscribed from. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        InputSet._set_input(self, 'ThreadLink', value)


class UnsubscribeFromThreadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UnsubscribeFromThread Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class UnsubscribeFromThreadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UnsubscribeFromThreadResultSet(response, path)
