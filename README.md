## Intercom

A daemon and it's minions used for managing you Home. They communicate using ZeroMQ and are built in Python 3.

## Components

Intercom is made out of five different kinds of components :
* broker : central communication node, relays messages between other components
* minions : execute instructions
* controllers : send instructions from user interactions
* monitors : read sensors and publish their values
* logic nodes : transform information into instructions

## Installation

All you need Python 3.2 or greater, ZeroMQ and PyZMQ.

```
pip install intercom
```

## Running

### Setup your network

By default, minions will expect the broker to be available on the host `intercom`.
Edit your DNS settings or the `hosts` file of the systems on which you will run minions
to resolve to the machine running the broker.

### Start the broker

```
python -m intercom.broker
```

You may want to run the broker in a `screen` session or using _supervisord_.

### Start a minion

```
python myminion.py
```

You will find example of minions in `Intercom/intercom/minions/`.

## Writing a Minion

The following Minion will just print a text on the terminal:

```python
from intercom.minion2 import Minion

minion = Minion('minion.pc')

@minion.register('do:test.print')
def test_print(topic, msg):
    print('This is some text:')
    print(msg.get('text', ''))

if __name__ == '__main__':
    minion.run()
```
