## Using charmbox to build the charm

```
cd git/juju/local && mkdir -p {data,charms,interfaces,layers}
export JUJU_BASE=/home/emil/git/juju/local
export JUJU_DATA=$JUJU_BASE/data
export JUJU_REPOSITORY=$JUJU_BASE/charms
export INTERFACE_PATH=$JUJU_BASE/interfaces
export LAYER_PATH=$JUJU_BASE/layers

alias dock_juju="sudo docker run --rm --name juju_dev -t -i -v $JUJU_DATA:/home/ubuntu/.local/share/juju -v $JUJU_REPOSITORY:/home/ubuntu/charms -v $LAYER_PATH:/home/ubuntu/charms/layers -v $INTERFACE_PATH:/home/ubuntu/charms/interfaces jujusolutions/charmbox"


dock_juju
cd charms/MY_CHARM
charm build
```
