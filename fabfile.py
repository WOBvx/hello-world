from fabric.api import local
from datetime import datetime

t = str(datetime.now())
s = str(t)[20:]

def prepare_deploy():
    local("cd /home/hello-world")
    local("git add * && git commit -m %s" % s)
    local("git push")
    local("wx385656!!")
