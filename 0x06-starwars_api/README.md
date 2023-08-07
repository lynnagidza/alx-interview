# Star Wars API
This project focuses on making HTTP requests to the [Star Wars API](https://swapi-api.hbtn.io/).
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

## Task
Write a script that prints all characters of a Star Wars movie:
* The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name per line in the same order as the “characters” list in the `/films/` endpoint
* You must use the [Star wars API](https://swapi-api.hbtn.io/)
* You must use the `requests` module

## Requirements
### Install Node 10
```sh
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install semi-standard
```sh
sudo npm install semistandard --global
```

### Install `request` module and use it
```sh
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## License
This project is licensed under the [MIT License](../LICENSE).