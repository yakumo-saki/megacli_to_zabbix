import logging

logger = logging.getLogger(__name__)

def rough_parse(txt):
    """ :でスプリットしてtrimかけてとりあえずキー->valueにしてしまう

    :param string txt: 元のテキスト
    :return: list -> map[zabbix_key] = {key: value}
    """

    ret = [] # array -> partial_result

    lines = txt.splitlines()
    empty_lines = 0
    partial_result = {}  # map[zabbix_key] => value
    for line in lines:
        line = line.strip()

        if line == "":
            empty_lines = empty_lines + 1
            if empty_lines >= 2:
                # 2行以上の連続した空行は区切り
                if len(partial_result) != 0:
                    ret.append(partial_result)

                partial_result = {}
                empty_lines = 0
        else:
            empty_lines = 0 # ここまでくれば空行ではないので連続空行カウントをリセット
            if ":" in line:
                pass
            else:
                continue  # : が含まれないならそれは区切りとかヘッダなので無視

            splitted = line.split(":", 1)  # 分割は1回まで＝2個に分割
            if len(splitted) != 2:
                logger.debug(f"Len != 2: {line}")
                continue  # 変な行

            key = splitted[0].strip()
            val = splitted[1].strip()
            partial_result[key] = val

        # for

    if len(partial_result) != 0:
        ret.append(partial_result)

    return ret


def parse(rough_result, keyItemName, keyPlaceHolder, keyMap):
    """
    Args:
        keyItemName zabbixキーにするmegacliの項目名 ex) Adapter Name
        keyPlaceHolder zabbixキーに含めるプレイスホルダー表記 ex) {#SASADDR}
        keyMap map[zabbixキー] = map[zabbix項目名] = 値
    Returns:
        map[discovery_key] -> map[zbx_key] = value
    """

    ret = {}

    for oneItem in rough_result:
        values = {}

        if keyItemName not in oneItem:
            continue   # maybe "Exit Code: 0x00"

        key = oneItem[keyItemName]
        
        # megacliキーをzabbixキーに変換
        for megacliKey in keyMap:
            value = oneItem[megacliKey]
            zbxKey = keyMap[megacliKey].replace(keyPlaceHolder, key)
            values[zbxKey] = value

        ret[key] = values

    return ret
