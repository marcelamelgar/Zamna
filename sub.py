import subprocess
#...
def cmd(commando):
    subprocess.Popen(commando, shell=True)

cmd("python app.py")