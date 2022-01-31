import os
from os.path import join, dirname

# load_dotenv相当の処理
def load_env_from_file():
    envfile = join(dirname(__file__), '.env')
    # print(envfile)
    if os.path.exists(envfile):
        with open(envfile) as f:
            l = f.readlines()
            for s in l:
                line = s.strip()
                if line == "":
                    continue
                elif line[0] == "#":
                    continue
                elif line[0] == ";":
                    continue
                
                # variable
                env = line.split("=", 1)
                set_os_variable(env[0].strip(), env[1].strip())

def set_os_variable(name, value):
    v = os.environ.get(name, None)
    if v == None:
        # print("[.env] set", name, "=", value)
        os.environ[name] = value


if __name__ == "__main__":
    print("Test load_env")
    load_env_from_file()
