# -*- coding: utf-8 -*-

###############################################################################
#
# ThreadDetails
# Obtain thread details.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ThreadDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ThreadDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Threads/ThreadDetails')


    def new_input_set(self):
        return ThreadDetailsInputSet()

    def _make_result_set(self, result, path):
        return ThreadDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ThreadDetailsChoreographyExecution(session, exec_id, path)

class ThreadDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ThreadDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, integer) A forum ID.  Required if setting either ThreadByIdentification, or ThreadByLink.)
        """
        InputSet._set_input(self, 'Forum', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_Related(self, value):
        """
        Set the value of the Related input for this Choreo. ((optional, string) Specify a related thread or forum that are to be included in the response.  Valid entries include: author, category, or forum.)
        """
        InputSet._set_input(self, 'Related', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((conditional, integer) The ID of a thread that is to be retrieved. Required unless specifying ThreadIdentifier or ThreadLink. If using this parameter, ThreadIdentifier cannot be set.)
        """
        InputSet._set_input(self, 'ThreadID', value)
    def set_ThreadIdentifier(self, value):
        """
        Set the value of the ThreadIdentifier input for this Choreo. ((conditional, string) The identifier to retrieve associated thread details. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadLink cannot be used.)
        """
        InputSet._set_input(self, 'ThreadIdentifier', value)
    def set_ThreadLink(self, value):
        """
        Set the value of the ThreadLink input for this Choreo. ((conditional, string) A link pointing to the thread that is to be retrieved. Note that a Forum must also be provided when using this parameter. If set, ThreadID and ThreadIdentifier cannot be set.)
        """
        InputSet._set_input(self, 'ThreadLink', value)


class ThreadDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ThreadDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class ThreadDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ThreadDetailsResultSet(response, path)
