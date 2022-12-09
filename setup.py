# -*- coding: utf-8 -*-
from setuptools import setup

packages = ["macaddress_io_client"]

package_data = {"": ["*"]}

install_requires = [
    "click>=8.1.3,<9.0.0",
    "furl>=2.1.3,<3.0.0",
    "keyring>=23.11.0,<24.0.0",
    "onepassword>=0.4.1,<0.5.0",
    "requests>=2.28.1,<3.0.0",
]

entry_points = {
    "console_scripts": ["macaddress-io-client = macaddress_io_client.cli:root"]
}

setup_kwargs = {
    "name": "macaddress-io-client",
    "version": "0.1.0",
    "description": "",
    "long_description": "# macaddress.io sample module\n\nThis CLI (and package) let you query macaddress.io from the command line or from python.\n\nBecause access to macaddress.io requires an API key (and I'm not allowed to give you one), you will have to set this up\nas follows.\n\n## Use installed on a workstation\n\n```shell\npip install .\n\nmacaddress-io-client --help  # print some pretty help messages\nmacaddress-io-client doctor  # should tell you you need to save your API key in the keyring`\nmacaddress-io-client save-api-key  # now follow the prompts to store the value in your local keyring`\nmacaddress-io-client doctor  # no more message. Win!`\nmacaddress-io-client get  # oops, need to provide a MAC address. Right.`\nmacaddress-io-client get 44:38:39:ff:ef:57 # Should return a company name`\nmacaddress-io-client get bob  # this should probably complain some.`\nmacaddress-io-client get 36:94:2e:9a:8b:40  # This gets an empty response. A warning is included.\n```\n\n# Use from a docker image\n\n## Build the docker container\n\nTo run it inside a docker container, first build the package and then container:\n\n```shell\n# install poetry\nwhich poetry || pip install poetry\n# build the package\npoetry build .\n# build the image which installs the package\ndocker build . -t macaddress_client_image\n```\n\n## Using your API key inside the built docker container\n\nThen send your API key to the docker environment. There are multiple options (this is a typical docker flow):\n\n```shell\n# on your workstation\nexport MACADDRESS_IO_KEY=I_AM_SO_NOT_PUTTING_THAT_IN_A_README\ndocker run -e MACADDRESS_IO_KEY macaddress_client_image get 44:38:39:ff:ef:57\n```\n\nThis pattern would let you use any password manager you want, as you only leave your API key exposed as an environment\nvariable. \n\n```shell\npip install keyring  # should be usable immediately on a typical workstation\nkeyring set macaddress.io my_username  # yes, you can use \"my_username\" safely\ndocker run -e MACADDRESS_IO_KEY=$(keyring get macaddress.io my_username) macaddress_client_image doctor\ndocker run -e MACADDRESS_IO_KEY=$(keyring get macaddress.io my_username) macaddress_client_image get 44:38:39:ff:ef:57\n```\n\n## Interactive Use inside a docker container\n\n`keyring` is in fact installed in the image for secured storage, \nif you prefer to launch the image interactively and use it:\n\n```shell\ndocker run -it --entrypoint /bin/bash macaddress_client_image\nroot@e2880ac08c24:~# macaddress-io-client save-api-key\nEnter your API key for macaddress.io:  # I pasted here, but you can't see it.\nroot@e2880ac08c24:~# macaddress-io-client doctor  \nroot@e2880ac08c24:~# # no output means it is ready to try\nroot@e2880ac08c24:~# macaddress-io-client get 44:38:39:ff:ef:57\nCumulus Networks, Inc\nroot@e2880ac08c24:~# \n```\n",
    "author": "David Brown",
    "author_email": "business@smurfless.com",
    "maintainer": "None",
    "maintainer_email": "None",
    "url": "None",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "entry_points": entry_points,
    "python_requires": ">=3.10,<4.0",
}


setup(**setup_kwargs)
