# macaddress.io sample module

This CLI (and package) let you query macaddress.io from the command line or from python.

Because access to macaddress.io requires an API key (and I'm not allowed to give you one), you will have to set this up
as follows.

## Use installed on a workstation

```shell
pip install .

macaddress-io-client --help  # print some pretty help messages
macaddress-io-client doctor  # should tell you you need to save your API key in the keyring`
macaddress-io-client save-api-key  # now follow the prompts to store the value in your local keyring`
macaddress-io-client doctor  # no more message. Win!`
macaddress-io-client get  # oops, need to provide a MAC address. Right.`
macaddress-io-client get 44:38:39:ff:ef:57 # Should return a company name`
macaddress-io-client get bob  # this should probably complain some.`
macaddress-io-client get 36:94:2e:9a:8b:40  # This gets an empty response. A warning is included.
```

## Use from a docker image

### Build the docker container

To run it inside a docker container, first build the package and then container:

```shell
# install poetry
which poetry || pip install poetry
# build the package
poetry build .
# build the image which installs the package
docker build . -t macaddress_client_image
```

### Using your API key inside the built docker container

Then send your API key to the docker environment. There are multiple options (this is a typical docker flow):

```shell
# on your workstation
export MACADDRESS_IO_KEY=I_AM_SO_NOT_PUTTING_THAT_IN_A_README
docker run -e MACADDRESS_IO_KEY macaddress_client_image get 44:38:39:ff:ef:57
```

This pattern would let you use any password manager you want, as you only leave your API key exposed as an environment
variable. 

```shell
pip install keyring  # should be usable immediately on a typical workstation
keyring set macaddress.io my_username  # yes, you can use "my_username" safely
docker run -e MACADDRESS_IO_KEY=$(keyring get macaddress.io my_username) macaddress_client_image doctor
docker run -e MACADDRESS_IO_KEY=$(keyring get macaddress.io my_username) macaddress_client_image get 44:38:39:ff:ef:57
```

### Interactive Use inside a docker container

`keyring` is in fact installed in the image for secured storage, 
if you prefer to launch the image interactively and use it:

```shell
docker run -it --entrypoint /bin/bash macaddress_client_image
root@e2880ac08c24:~# macaddress-io-client save-api-key
Enter your API key for macaddress.io:  # I pasted here, but you can't see it.
root@e2880ac08c24:~# macaddress-io-client doctor  
root@e2880ac08c24:~# # no output means it is ready to try
root@e2880ac08c24:~# macaddress-io-client get 44:38:39:ff:ef:57
Cumulus Networks, Inc
root@e2880ac08c24:~# 
```
