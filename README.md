## Intercom

A daemon and it's minions used for managing you Home automation. They communicate using ZeroMQ and are built in Python 3.

## Components

Intercom is made out of five different kinds of components :
* relay : central communication node, relays messages between other components
* minions : execute instructions
* controllers : send instructions from user interactions
* monitors : read sensors and publish their values
* logic nodes : transform information into instructions

## Installation

All you need Python 3.2 or greater, ZeroMQ and PyZMQ.

```
pip install pyzmq
```

## Running

### Setup your network

By default, minions will expect the relay to be available on the host `relay.intercom`.
Edit your DNS settings or the `hosts` file of the systems on which you will run minions
to resolve to the machine running the relay.

### Start the relay

```
python relay.py
```

You may want to run the relay in a `screen` session or using _supervisord_.

### Start a minion

```
python myminion.py
```

You will find example of minions in `Intercom/intercom/minions/`.
