# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteInvoiceItem
# Deletes a specified invoice item.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeDeleteResults import StripeDeleteResults

import json

class DeleteInvoiceItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteInvoiceItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/InvoiceItems/DeleteInvoiceItem')


    def new_input_set(self):
        return DeleteInvoiceItemInputSet()

    def _make_result_set(self, result, path):
        return DeleteInvoiceItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteInvoiceItemChoreographyExecution(session, exec_id, path)

class DeleteInvoiceItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteInvoiceItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_InvoiceItemID(self, value):
        """
        Set the value of the InvoiceItemID input for this Choreo. ((required, string) The unique identifier of the invoice item you want to delete)
        """
        InputSet._set_input(self, 'InvoiceItemID', value)

class DeleteInvoiceItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteInvoiceItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getDeleteResults(self):
        """
        """
        return StripeDeleteResults(self.getJSONFromString(self._output.get('Response', [])))

class DeleteInvoiceItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteInvoiceItemResultSet(response, path)
