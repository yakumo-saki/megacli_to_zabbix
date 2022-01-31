import os
import load_dotenv

load_dotenv.load_env_from_file()

# 環境変数を読む。 
ZABBIX_SERVER = os.environ.get('ZABBIX_SERVER', None)
ZABBIX_PORT = int(os.environ.get('ZABBIX_PORT', "10051"))
ZABBIX_HOST = os.environ.get('ZABBIX_HOST', None)
LOG_LEVEL = os.environ.get('LOG_LEVEL', "DEBUG")

MEGACLI_ADP_CMD=os.environ.get('MEGACLI_ADP_CMD', "/opt/MegaRAID/MegaCli/MegaCli64 -Adpallinfo -Aall")
MEGACLI_PD_CMD=os.environ.get('MEGACLI_PD_CMD', "/opt/MegaRAID/MegaCli/MegaCli64  -Pdlist -Aall")
MEGACLI_VD_CMD=os.environ.get('MEGACLI_VD_CMD', "/opt/MegaRAID/MegaCli/MegaCli64 -Ldinfo -Lall -Aall")

