from invoke import task


@task
def build(c):
    c.run("poetry build")
    c.run("poetry2setup > setup.py")
    c.run("docker build . -t macaddress_client_image")
