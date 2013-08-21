# -*- coding: utf-8 -*-

###############################################################################
#
# CampaignContribution
# Retrieve detailed information on political campaign contributions, filtered by date, contributor, state, employer, campaign, etc.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CampaignContribution(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CampaignContribution Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/CampaignContribution')


    def new_input_set(self):
        return CampaignContributionInputSet()

    def _make_result_set(self, result, path):
        return CampaignContributionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CampaignContributionChoreographyExecution(session, exec_id, path)

class CampaignContributionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CampaignContribution
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((conditional, string) Enter the amount of dollars spent on lobbying.  Valid formats include: 500 (exactly $500); >|500 (greater than, or equal to 500); <|500 (less than or equal to 500).)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_ContributorName(self, value):
        """
        Set the value of the ContributorName input for this Choreo. ((conditional, string) Specfiy the name of an individual, PAC, organization, or employer for which a full-text search will be performed.)
        """
        InputSet._set_input(self, 'ContributorName', value)
    def set_ContributorsByState(self, value):
        """
        Set the value of the ContributorsByState input for this Choreo. ((conditional, string) Enter a two-letter state designation from which the contribution is made.)
        """
        InputSet._set_input(self, 'ContributorsByState', value)
    def set_Cycle(self, value):
        """
        Set the value of the Cycle input for this Choreo. ((conditional, string) Specify a yyyy-formatted election cycle. Example: 2012, or 2008|2012 to limit results between 2008 and 2012.)
        """
        InputSet._set_input(self, 'Cycle', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((conditional, string) Specify a date of the contribution in ISO date format.  For example: 2006-08-06.  Or, ><|2006-08-06|2006-09-12 to limit results between specific dates.)
        """
        InputSet._set_input(self, 'Date', value)
    def set_OrganizationName(self, value):
        """
        Set the value of the OrganizationName input for this Choreo. ((conditional, string) Specify a full-text search on employer, organization, and parent organization.)
        """
        InputSet._set_input(self, 'OrganizationName', value)
    def set_RecipientName(self, value):
        """
        Set the value of the RecipientName input for this Choreo. ((conditional, string) Enter the full-text search on name of PAC or candidate receiving the contribution.)
        """
        InputSet._set_input(self, 'RecipientName', value)
    def set_RecipientState(self, value):
        """
        Set the value of the RecipientState input for this Choreo. ((conditional, string) Specify a two-letter state abbreviation for the state in which the recipient of contributions is running a campaign.)
        """
        InputSet._set_input(self, 'RecipientState', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Indicates the desired format for the response. Accepted values are: json (the default), csv, and xls. Note when specifying xls, restults are returned as Base64 encoded data.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Seat(self, value):
        """
        Set the value of the Seat input for this Choreo. ((conditional, string) Specify the type of political office being sought.  Examples: federal:senate (US Senate), federal:president (US President), state:governor.  For more info see documentation.)
        """
        InputSet._set_input(self, 'Seat', value)
    def set_TransactionNamespace(self, value):
        """
        Set the value of the TransactionNamespace input for this Choreo. ((optional, string) Filters on federal or state contributions. Valid namespaces are: urn:fec:transaction (for federal) or urn:nimsp:transaction (for state).)
        """
        InputSet._set_input(self, 'TransactionNamespace', value)

class CampaignContributionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CampaignContribution Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Influence Explorer. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)

class CampaignContributionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CampaignContributionResultSet(response, path)
