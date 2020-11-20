from tap_hubspot import sync_deals
import unittest
from unittest.mock import patch, ANY


class TestDealsToSync(unittest.TestCase):

    @patch('tap_hubspot.Context.get_catalog_from_id', return_value={"metadata":""})
    @patch('singer.metadata.to_map', return_value={})
    @patch('singer.utils.strptime_with_tz')
    @patch('singer.utils.strftime')
    @patch('tap_hubspot.load_schema')
    @patch('tap_hubspot.gen_request', return_value=list())
    def test_associations_are_not_validated(self,
        mocked_gen_request,
        mocked_catalog_from_id,
        mocked_metadata_map,
        mocked_utils_strptime,
        mocked_utils_strftime,
        mocked_load_schema):

        sync_deals({}, mocked_catalog_from_id)

        expected_param = {'count': 250, 'includeAssociations': False, 'properties': []}

        mocked_gen_request.assert_called_once_with(ANY, ANY, ANY, expected_param, ANY, ANY, ANY, ANY)


    @patch('tap_hubspot.Context.get_catalog_from_id', return_value={"metadata":""})
    @patch('singer.metadata.to_map', return_value={"associations" :{"selected" : True}})
    @patch('singer.utils.strptime_with_tz')
    @patch('singer.utils.strftime')
    @patch('tap_hubspot.load_schema')
    @patch('tap_hubspot.gen_request', return_value=list())
    def test_associations_are_validated(self,
        mocked_gen_request,
        mocked_catalog_from_id,
        mocked_metadata_map,
        mocked_utils_strptime,
        mocked_utils_strftime,
        mocked_load_schema):

        sync_deals({}, mocked_catalog_from_id)

        expected_param = {'count': 250, 'includeAssociations': True, 'properties': []}

        mocked_gen_request.assert_called_once_with(ANY, ANY, ANY, expected_param, ANY, ANY, ANY, ANY)
