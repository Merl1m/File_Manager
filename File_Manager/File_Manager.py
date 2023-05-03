import os
import time

USER = os.getlogin()

Catagories = {
    r"C:\Users\{0}\Pictures".format(USER):(".jpg", ".png", ".jpeg"),
    r"C:\Users\{0}\Videos".format(USER):(".mp4",".mov"),
    r"C:\Users\{0}\Documents".format(USER):(".txt", ".dat"),
    }

Run_Loc = r"C:\Users\{0}\Downloads".format(USER)
Running = True

"""
def execute(location):
    for file in os.listdir(location):
        for new_location, extensions in Catagories.items():
            case = False
            for extension in extensions:
                if file.endswith(extension):
                    case = True
                    path = os.path.join(location, file)
                    os.system("move \"{0}\" {1}".format(path, new_location))
                    break
            if case:
                break
""" # Slower

def exec1(location):
    for new_location, extensions in Catagories.items():
        for file in os.listdir(location):
            case = False
            for extension in extensions:
                if file.endswith(extension):
                    case = True
                    path = os.path.join(location, file)
                    os.system("move \"{0}\" {1}".format(path, new_location))
                    break

            if case:
                break

"""
start = time.time()
exec1(Run_Loc)
print(time.time() - start)
""" # Testing 

while Running:
    try:
        exec1(Run_Loc)
        time.sleep(875)
    except KeyboardInterrupt:
        print("Quiting...")
        Running = False