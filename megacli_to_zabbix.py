import json
import logging
from select import select
import subprocess
from pprint import pprint

import config as cfg

import modules.const as const
import modules.parser as txtparser
import modules.zabbix_send as zbxsend

logger = logging.getLogger(__name__)


# smartctl --scan を実行して結果を返す
#
def exec_smartctl_scan():

    cmd = None

    import platform
    platform = platform.system()
    if platform == 'Windows':
        cmd = cfg.WIN_SMARTCTL_SCAN_CMD.copy()
    else:
        cmd = cfg.LINUX_SMARTCTL_SCAN_CMD.copy()

    if cmd[0] == 'sudo':
        logger.info("Asking your password by sudo")

    scan = subprocess.run(cmd, stdout=subprocess.PIPE)

    # logger.debug(scan.stdout)
    result = json.loads(scan.stdout)
    # logger.debug(result)
    return result


def get_smartctl_device_info_cmd():
    import platform
    platform = platform.system()
    cmd = None
    if platform == 'Windows':
        cmd = cfg.WIN_SMARTCTL_DETAIL_CMD.copy()
    else:
        cmd = cfg.LINUX_SMARTCTL_DETAIL_CMD.copy()

    return cmd


def exec_megacli(type):

    result = ""
    retcode = 999

    # call smartctl without any option
    if True:
        cmd = ""
        if type == const.TypeAdapter:
            cmd = cfg.MEGACLI_ADP_CMD.split(" ")
        elif type == const.TypePd:
            cmd = cfg.MEGACLI_PD_CMD.split(" ")
        elif type == const.TypeVd:
            cmd = cfg.MEGACLI_VD_CMD.split(" ")

        logger.debug(cmd)

        proc_info = subprocess.run(cmd, stdout=subprocess.PIPE)
        result = proc_info.stdout
        retcode = proc_info.returncode
        if (retcode > 4):  # 0 = ok , 1 = maybe USB , 2 = megaraid
            raise RuntimeError(f"smartctl return code = {retcode}. cmd = {cmd}")

    result = result.decode(encoding='utf-8')
    logger.info(f"exec command result is {retcode}")
    logger.debug(result)

    return result


def read_file(filepath):
    with open(filepath) as f:
        ret = f.read()

    return ret


if __name__ == '__main__':

    fmt = "%(asctime)s %(levelname)s %(name)s %(message)s"

    if (cfg.LOG_LEVEL.upper() == "ERROR"):
        logging.basicConfig(level=logging.ERROR, format=fmt)
    elif (cfg.LOG_LEVEL.upper() == "WARN"):
        logging.basicConfig(level=logging.WARN, format=fmt)
    elif (cfg.LOG_LEVEL.upper() == "INFO"):
        logging.basicConfig(level=logging.INFO, format=fmt)
    else:
        logging.basicConfig(level=logging.DEBUG, format=fmt)


    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("type", default="all", nargs="?", help="Optional. [all|adp|vd|pd] type of information.")
    parser.add_argument("filename", default="", nargs="?", help="Optional. Filepath. Use file as MegaCli output. If not specified. We call MegaCli")
    args = parser.parse_args()

    logger.info("START")

    types = [const.TypeAdapter, const.TypeVd, const.TypePd]

    for type in types:
        if (args.type != type and args.type != "all"):
            continue

        logger.info(f"Processing {type}")

        output_txt = ""
        if args.filename != "":
            output_txt = read_file(args.filename)
        else:
            output_txt = exec_megacli(type)

        # print(output_txt)

        rough_result = txtparser.rough_parse(output_txt)
        result = {}
        if type == const.TypeAdapter:
            result = txtparser.parse(rough_result, const.AdapterKeyItem, const.AdapterKeyPlaceHolder ,const.AdapterKeyMap)
            zbxsend.send_device_discovery(result, const.AdapterDiscoveryKey, const.AdapterKeyPlaceHolder)
        elif type == const.TypeVd:
            result = txtparser.parse(rough_result, const.VdKeyItem, const.VdKeyPlaceHolder ,const.VdKeyMap)
            zbxsend.send_device_discovery(result, const.VdDiscoveryKey, const.VdKeyPlaceHolder)
        elif type == const.TypePd:
            result = txtparser.parse(rough_result, const.PdKeyItem, const.PdKeyPlaceHolder ,const.PdKeyMap)
            zbxsend.send_device_discovery(result, const.PdDiscoveryKey, const.PdKeyPlaceHolder)

        # send values
        zbxsend.send_data(result)

        logger.info(f"Processing {type} done.")

    logger.info("END")
