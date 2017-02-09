"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        downHost = self.addHost( 'h3' )
        upSwitch = self.addSwitch( 's1' )
        downSwitch = self.addSwitch( 's2' )

        # Add links
        self.addLink( leftHost, upSwitch ,bw=1,delay='1ms',loss=1)
        self.addLink( upSwitch, rightHost ,bw=1,delay='1ms',loss=2)
        self.addLink( upSwitch, downSwitch ,bw=1,delay='1ms',loss=2)
        self.addLink( downSwitch, downHost ,bw=1,delay='1ms',loss=1)


topos = { 'mytopo': ( lambda: MyTopo() ) }
