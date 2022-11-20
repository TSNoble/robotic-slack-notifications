from invoke import task

@task
def build(c):
    c.run("docker build . -t ros-slackbot-dev")

@task
def shell(c):
    volumes = ["-v /tmp/.X11-unix:/tmp/.X11-unix",
               "-v ~/.aws:/home/default/.aws"]
    environment = ["-e DISPLAY=$DISPLAY"]
    devices = ["--device /dev/dri:/dev/dri"]
    network = "host"
    image = "ros-slackbot-dev"
    c.run(f"docker run -it {' '.join(volumes)} {' '.join(environment)} {' '.join(devices)} --network={network} {image}", pty=True)

@task
def start(c):
    volumes = ["-v /tmp/.X11-unix:/tmp/.X11-unix",
               "-v ~/.aws:/home/default/.aws"]
    environment = ["-e DISPLAY=$DISPLAY"]
    devices = ["--device /dev/dri:/dev/dri"]
    network = "host"
    image = "ros-slackbot-dev"
    c.run(f'docker run -it {" ".join(volumes)} {" ".join(environment)} {" ".join(devices)} --network={network} {image} /bin/bash -c "cd ros; source devel/setup.bash; roslaunch panda_moveit_config demo.launch"', pty=True)