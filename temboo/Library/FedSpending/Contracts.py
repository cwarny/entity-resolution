# -*- coding: utf-8 -*-

###############################################################################
#
# Contracts
# Allows access to the information in the Federal Procurement Data System (FPDS) database, which reports all federal contracts awarded. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Contracts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Contracts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/FedSpending/Contracts')


    def new_input_set(self):
        return ContractsInputSet()

    def _make_result_set(self, result, path):
        return ContractsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ContractsChoreographyExecution(session, exec_id, path)

class ContractsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Contracts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((conditional, string) The city within a contractor's address.)
        """
        InputSet._set_input(self, 'City', value)
    def set_CompanyName(self, value):
        """
        Set the value of the CompanyName input for this Choreo. ((conditional, string) The name of a a contractor or contractor parent company.)
        """
        InputSet._set_input(self, 'CompanyName', value)
    def set_Completion(self, value):
        """
        Set the value of the Completion input for this Choreo. ((conditional, string) The competition status of a contract. Valid values: c=Full competition, o=Full competition, one bid, p=Competition, exclusion of sources, n=Not complete, a=Not available, f=Follow-up, u=Unknown.)
        """
        InputSet._set_input(self, 'Completion', value)
    def set_Detail(self, value):
        """
        Set the value of the Detail input for this Choreo. ((optional, string) Controls the level of detail of the output. Acceptable values: -1 (summary), 0 (low), 1 (medium), 2 (high), and 3 (extensive). Defaults to -1. See docs for more information.)
        """
        InputSet._set_input(self, 'Detail', value)
    def set_FirstYearRange(self, value):
        """
        Set the value of the FirstYearRange input for this Choreo. ((conditional, integer) Specifies the first year in a range of years; if used, must be used with LastYearRange and without FiscalYear.)
        """
        InputSet._set_input(self, 'FirstYearRange', value)
    def set_FiscalYear(self, value):
        """
        Set the value of the FiscalYear input for this Choreo. ((conditional, integer) Specifies a single year; defaults to all years.)
        """
        InputSet._set_input(self, 'FiscalYear', value)
    def set_LastYearRange(self, value):
        """
        Set the value of the LastYearRange input for this Choreo. ((conditional, integer) Specifies the last year in a range of years; if used, must be used with FirstYearRange and without FiscalYear.)
        """
        InputSet._set_input(self, 'LastYearRange', value)
    def set_MajAgency(self, value):
        """
        Set the value of the MajAgency input for this Choreo. ((conditional, string) The 2-character code for a major governmental agency issuing contracts.)
        """
        InputSet._set_input(self, 'MajAgency', value)
    def set_MaxRecords(self, value):
        """
        Set the value of the MaxRecords input for this Choreo. ((optional, integer) Allows you to set the maximum number of records retrieved. Defaults to 100.)
        """
        InputSet._set_input(self, 'MaxRecords', value)
    def set_ModAgency(self, value):
        """
        Set the value of the ModAgency input for this Choreo. ((conditional, string) The 4-digit code for a specific governmental agency issuing contracts.)
        """
        InputSet._set_input(self, 'ModAgency', value)
    def set_PIID(self, value):
        """
        Set the value of the PIID input for this Choreo. ((conditional, integer) A Federal ID number for the contract.)
        """
        InputSet._set_input(self, 'PIID', value)
    def set_PSCCategory(self, value):
        """
        Set the value of the PSCCategory input for this Choreo. ((conditional, string) The 2-character code for a major product or service category.)
        """
        InputSet._set_input(self, 'PSCCategory', value)
    def set_PSC(self, value):
        """
        Set the value of the PSC input for this Choreo. ((conditional, string) The 4-character code for a product or service.)
        """
        InputSet._set_input(self, 'PSC', value)
    def set_PopCountryCode(self, value):
        """
        Set the value of the PopCountryCode input for this Choreo. ((conditional, string) The two-letter country code for the place of performance country.)
        """
        InputSet._set_input(self, 'PopCountryCode', value)
    def set_PopDistrict(self, value):
        """
        Set the value of the PopDistrict input for this Choreo. ((conditional, string) The Congressional District of the place of performance.)
        """
        InputSet._set_input(self, 'PopDistrict', value)
    def set_PopZipCode(self, value):
        """
        Set the value of the PopZipCode input for this Choreo. ((conditional, integer) The ZIP code of the place of performance.)
        """
        InputSet._set_input(self, 'PopZipCode', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Determines how records are sorted. Valid values: r (contractor/recipient name), f (dollars of awards),g (major contracting agency),p (Product or Service Category),d (date of award). Defaults to f.)
        """
        InputSet._set_input(self, 'SortBy', value)
    def set_StateCode(self, value):
        """
        Set the value of the StateCode input for this Choreo. ((conditional, string) The state abbreviation of the state of the place of performance.)
        """
        InputSet._set_input(self, 'StateCode', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((conditional, string) The state abbreviation within a contractor's address.)
        """
        InputSet._set_input(self, 'State', value)
    def set_TextSearch(self, value):
        """
        Set the value of the TextSearch input for this Choreo. ((conditional, string) Free text search within the text that describes what the contract is for.)
        """
        InputSet._set_input(self, 'TextSearch', value)
    def set_VendorCountryCode(self, value):
        """
        Set the value of the VendorCountryCode input for this Choreo. ((conditional, string) The two-letter country code for the country in a contractor's address.)
        """
        InputSet._set_input(self, 'VendorCountryCode', value)
    def set_VendorDistrict(self, value):
        """
        Set the value of the VendorDistrict input for this Choreo. ((conditional, string) The 4-character Congressional District within which a contractor is located.)
        """
        InputSet._set_input(self, 'VendorDistrict', value)
    def set_ZipCode(self, value):
        """
        Set the value of the ZipCode input for this Choreo. ((conditional, integer) The ZIP code within a contractor's address.)
        """
        InputSet._set_input(self, 'ZipCode', value)

class ContractsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Contracts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FedSpending.org.)
        """
        return self._output.get('Response', None)

class ContractsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ContractsResultSet(response, path)
