class Unit():
    KB = 1024
    MB = 1024 * 1024
    GB = 1024 * 1024 * 1024
    TB = 1024 * 1024 * 1024 * 1024
    SI = 1000
    KiB = 1000
    MiB = 1000 * 1000
    GiB = 1000 * 1000 * 1000
    TiB = 1000 * 1000 * 1000 * 1000

class DeviceKey():
    """Zabbixのデバイスディスカバリに使うキー
    """
    KEY = 'smartmontools.discovery.device'
    KEY_NAME = '{#KEYNAME}'
    DISK_NAME = '{#DISKNAME}'

# 
TypeAll = "all"
TypeAdapter = "adp"
TypePd = "pd"  # physical disk
TypeVd = "vd"  # virtual disk

# megacli adapter
AdapterKeyItem = "SAS Address"
AdapterDiscoveryKey="megacli.lld.adapter"
AdapterKeyPlaceHolder="{#SASADDR}"
AdapterKeyMap = {
    "BBU": "megacli.adapter.bbu[{#SASADDR}]",
    "Controller temperature": "megacli.adapter.controller_temp[{#SASADDR}]",
    "ROC temperature": "megacli.adapter.roc_temp[{#SASADDR}]",
    "Product Name":"megacli.adapter.name[{#SASADDR}]",
    "Disks": "megacli.adapter.disks[{#SASADDR}]", 
    "Critical Disks": "megacli.adapter.failed_disks[{#SASADDR}]",
    "Failed Disks": "megacli.adapter.failed_disks[{#SASADDR}]"    
}

# megacli pd
PdKeyItem = "WWN"
PdDiscoveryKey="megacli.lld.pd"
PdKeyPlaceHolder="{#WWN}"
PdKeyMap = {
    "Inquiry Data": "megacli.pd.inquiry[{#WWN}]",
    "Media Error Count": "megacli.pd.media_error[{#WWN}]",
    "Other Error Count": "megacli.pd.other_error[{#WWN}]",
    "Predictive Failure Count": "megacli.pd.predictive_failure[{#WWN}]",
    "Raw Size": "megacli.pd.raw_size[{#WWN}]",
    "WWN": "megacli.pd.wwn[{#WWN}]",
    "Drive's position": "megacli.pd.drive_position[{#WWN}]"
}

# megacli vd
VdKeyItem = "Name"
VdDiscoveryKey="megacli.lld.vd"
VdKeyPlaceHolder="{#NAME}"
VdKeyMap = {
    "Size": "megacli.vd.size[{#NAME}]",
    "Name": "megacli.vd.name[{#NAME}]",
    "State": "megacli.vd.state[{#NAME}]",
    "RAID Level": "megacli.vd.raid_level[{#NAME}]",
}
