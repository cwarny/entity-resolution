# -*- coding: utf-8 -*-

###############################################################################
#
# ListThreadReactions
# Retrieve a list of reactions for a given thread.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListThreadReactions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListThreadReactions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Threads/ListThreadReactions')


    def new_input_set(self):
        return ListThreadReactionsInputSet()

    def _make_result_set(self, result, path):
        return ListThreadReactionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListThreadReactionsChoreographyExecution(session, exec_id, path)

class ListThreadReactionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListThreadReactions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) Default is set to null.)
        """
        InputSet._set_input(self, 'Cursor', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, integer) A Disqus forum ID (AKA a short name). If null, threads from all forums moderated by the authenticating user will be retrieved.)
        """
        InputSet._set_input(self, 'Forum', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of records to return. Maximum value is 100.  Defaults to 25.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((conditional, string) The ID of the Thread to list reactions for. Required unless specifying ThreadIdentifier or ThreadLink.)
        """
        InputSet._set_input(self, 'ThreadID', value)
    def set_ThreadIdentifier(self, value):
        """
        Set the value of the ThreadIdentifier input for this Choreo. ((conditional, string) An identifier for which thread reactions will be retrieved.  Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        InputSet._set_input(self, 'ThreadIdentifier', value)
    def set_ThreadLink(self, value):
        """
        Set the value of the ThreadLink input for this Choreo. ((conditional, string) A link pointing to the thread that is to be retrieved. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        InputSet._set_input(self, 'ThreadLink', value)

class ListThreadReactionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListThreadReactions Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class ListThreadReactionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListThreadReactionsResultSet(response, path)
