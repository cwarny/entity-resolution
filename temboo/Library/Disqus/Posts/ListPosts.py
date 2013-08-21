# -*- coding: utf-8 -*-

###############################################################################
#
# ListPosts
# Retrieve a list of posts ordered by date of creation.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPosts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPosts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Posts/ListPosts')


    def new_input_set(self):
        return ListPostsInputSet()

    def _make_result_set(self, result, path):
        return ListPostsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPostsChoreographyExecution(session, exec_id, path)

class ListPostsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPosts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid OAuth 2.0 access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Category(self, value):
        """
        Set the value of the Category input for this Choreo. ((optional, integer) Specify a category ID for which posts wil be retrieved.)
        """
        InputSet._set_input(self, 'Category', value)
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) Default is set to null.)
        """
        InputSet._set_input(self, 'Cursor', value)
    def set_Forum(self, value):
        """
        Set the value of the Forum input for this Choreo. ((optional, string) A Disqus forum name to display all posts contained in that specified forum.  If null, posts from all forums moderated by the authenticating user will be retrieved.)
        """
        InputSet._set_input(self, 'Forum', value)
    def set_Include(self, value):
        """
        Set the value of the Include input for this Choreo. ((optional, string) A post status parameter to filter results by. Valid parameters include: unapproved, approved, spam, deleted, flagged, highlighted.  Default is set to: approved.)
        """
        InputSet._set_input(self, 'Include', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of records to return. Defaults to 25.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) The sort order of the results. Valid values are: asc or desc. Default is set to: asc.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search string to retrieve posts mathching the query.  Default is set to null.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_Related(self, value):
        """
        Set the value of the Related input for this Choreo. ((optional, string) Specify a related thread or forum that are to be included in the response.  Valid entries include: thread, or forum.)
        """
        InputSet._set_input(self, 'Related', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SinceID(self, value):
        """
        Set the value of the SinceID input for this Choreo. ((optional, integer) A Unix timestamp (or ISO datetime standard) to obtain results from. Default is set to null.)
        """
        InputSet._set_input(self, 'SinceID', value)
    def set_ThreadID(self, value):
        """
        Set the value of the ThreadID input for this Choreo. ((optional, string) The Thread ID to narrow post search results.)
        """
        InputSet._set_input(self, 'ThreadID', value)

class ListPostsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPosts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class ListPostsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPostsResultSet(response, path)
