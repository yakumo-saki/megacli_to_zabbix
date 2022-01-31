import unittest
from modules.const import Keys, AttrKey
import modules.zabbix_smart as zabbix_smart
import json
import glob
import tests.util as util
import os
import tests.const as const

class TestZabbixSmartListNvme(unittest.TestCase):

    def test_create_attribute_list_nvme(self):
        """ 
        create_attribute_list_nvmeの単体テスト
        """

        files = util.get_sata_json_paths()
        for filename in files:
            with self.subTest(filename=filename):
                with open(filename) as f:
                    jsonStr = f.read()

                detail = json.loads(jsonStr)
                discovery = {AttrKey.DEV_NAME: "dummy", AttrKey.DISK_NAME: filename}

                zabbix_smart.create_attribute_list_nvme(discovery, detail["nvme_smart_health_information_log"])
                
                self.assertTrue(True)
    

    def test_create_value_list_nvme(self):
        """ 
        create_value_list_nvmeの単体テスト
        """

        files = util.get_sata_json_paths()
        for filename in files:
            with self.subTest(filename=filename):
                with open(filename) as f:
                    jsonStr = f.read()

                detail = json.loads(jsonStr)

                zabbix_smart.create_value_list_nvme("dummy", detail["nvme_smart_health_information_log"])
                
                self.assertTrue(True)
                