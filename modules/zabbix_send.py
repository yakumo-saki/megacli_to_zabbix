import json
import logging
import config as cfg

from modules.zabbix_sender import send_to_zabbix

logger = logging.getLogger(__name__)


"""zabbixにDevice LLDデータを送信します。
result = {"/dev/sda": {"model": EXAMPLE SSD 250, "POWER_CYCLE": 123 ...}}

@param result 送信するデータ
@param discoveryKey zabbix discovery key. ex) megacli.lld.adapter
@param discoveryPHName discovery placeholder for values ex) SASADDR
"""
def send_device_discovery(result, discoveryKey, discoveryPHName):

  logger.info("Sending device discovery to zabbix")

  discovery_result = []
  for key in result:
    discovery_result.append({discoveryPHName: key})

  data = {"request": "sender data", "data":[]}
  valueStr = json.dumps({"data": discovery_result})
  one_data = {"host": cfg.ZABBIX_HOST, "key": discoveryKey, "value": f"{valueStr}"}
  data["data"].append(one_data)

  result = send_to_zabbix(data)
  logger.info(result)

  return None


"""interpriterで解釈出来たデータを送信する。
smartctlが解釈してくれたもの＋独自に解釈したデータ
data = {
    "host1": {
        "item1": 1234,
        "item2": "value"
    },
    "host2": {
        "item1": 5678,
        "item2": "value"
    }
}
"""
def send_data(data):
  logger.info("Send data to zabbix")

  results = []
  for mainkey in data:
    detail = data[mainkey]  # discovery key
    
    for key in detail:
      results.append({
        "host": cfg.ZABBIX_HOST,
        "key": key,
        "value": detail[key],
      })

  sender_data = {"request": "sender data", "data": results}

  result = send_to_zabbix(sender_data)

  logger.info(result)

  return None
