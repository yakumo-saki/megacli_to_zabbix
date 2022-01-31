import os
import glob
import tests.const as const

def is_not_test_target(filepath):
    base = os.path.basename(filepath)
    return base.startswith("_")


def get_json_paths(dir):
    cwd = os.getcwd()
    globspec = os.path.join(cwd, dir, "*.json")
    return glob.glob(globspec)
    


def get_sata_json_paths():
    all = get_json_paths(const.EXAMPLE_DEV_SATA_DIR)
    
    ret = []
    for f in all:
        if is_not_test_target(f) == False:
            ret.append(f)
    return ret

def get_nvme_json_paths():
    all = get_json_paths(const.EXAMPLE_DEV_NVME_DIR)

    ret = []
    for f in all:
        if is_not_test_target(f) == False:
            ret.append(f)
    return ret


def get_all_json_paths():
    all = get_json_paths(const.EXAMPLE_DEVICE_DIR)

    ret = []
    for f in all:
        if is_not_test_target(f) == False:
            ret.append(f)
    return ret
