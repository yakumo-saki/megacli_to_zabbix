import unittest
from modules.const import Keys, AttrKey
import modules.zabbix_smart as zabbix_smart
import json
import tests.util as util

class TestZabbixSmartListSata(unittest.TestCase):

    def test_create_attribute_list_sata(self):
        """ 
        create_attribute_list_sataの単体テスト
        """

        files = util.get_nvme_json_paths()
        for filename in files:
            with self.subTest(filename=filename):
                with open(filename) as f:
                    jsonStr = f.read()

                detail = json.loads(jsonStr)
                discovery = {AttrKey.DEV_NAME: "dummy", AttrKey.DISK_NAME: filename}

                zabbix_smart.create_attribute_list_non_nvme(
                    discovery,
                    detail["ata_smart_attributes"]
                )
                
                self.assertTrue(True)
    

    def test_create_value_list_nvme(self):
        """ 
        create_value_list_nvmeの単体テスト
        """
        
        files = util.get_nvme_json_paths()
        for filename in files:
            if util.is_not_test_target(filename):
                continue

            with self.subTest(filename=filename):
                with open(filename) as f:
                    jsonStr = f.read()

                detail = json.loads(jsonStr)
                discovery = {AttrKey.DEV_NAME: "dummy", AttrKey.DISK_NAME: filename}

                zabbix_smart.create_value_list_non_nvme(
                    "dummy",
                    detail["ata_smart_attributes"]
                )
                
                self.assertTrue(True)
                