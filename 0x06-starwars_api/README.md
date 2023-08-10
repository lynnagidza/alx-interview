# Star Wars API
This project focuses on making HTTP requests to the [Star Wars API](https://swapi-api.alx-tools.com/).

## Requirements
All files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)\
The code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)

[![ubuntu](https://img.shields.io/badge/ubuntu-14.04-orange)](http://releases.ubuntu.com/14.04/)
[![nodejs](https://img.shields.io/badge/node-v10.14.x-darkgreen)](https://nodejs.org/en/blog/release/v10.14.2/)
[![js-semistandard-style](https://img.shields.io/badge/code%20style-semistandard-brightgreen.svg)](https://github.com/standard/semistandard)

#### Install Node 10
```sh
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### Install semi-standard
```sh
sudo npm install semistandard --global
```

#### Install `request` module and use it
```sh
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

## Task
Write a script that prints all characters of a Star Wars movie:
* The first positional argument passed is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name per line in the same order as the “characters” list in the `/films/` endpoint
* You must use the [Star wars API](https://swapi-api.alx-tools.com/)
* You must use the `requests` module

## Usage
Run the script with the Movie ID as the first argument:\
`./0-starwars_characters.js <Movie ID>`

## Example
File name: `0-starwars_characters.js`\
Movie ID: `3`
```sh
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
```

## License
This project is licensed under the [MIT License](../LICENSE).