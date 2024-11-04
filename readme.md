# User Documentation: Peer-to-Peer Network using Python Socket Programming

## Overview

This project provides a framework for creating a decentralized P2P network where nodes can connect, exchange data, and participate in achieving consensus.

## Resilient Features

In our peer-to-peer network, we leverage socket programming to establish direct communication channels between nodes. Socket programming allows us to create connections over a network, enabling data exchange between devices.

With sockets, each node acts as both a client and a server, capable of initiating connections and accepting incoming connections. This bidirectional capability is essential for decentralized networks where all nodes have equal standing.

By utilizing sockets, we tap into the underlying infrastructure of the internet, leveraging its robustness and scalability. This approach enables us to build a network that can span across different devices and platforms, facilitating seamless communication regardless of the underlying technology stack.

In essence, socket programming serves as the backbone of our peer-to-peer network, enabling nodes to connect, communicate, and collaborate effectively in a decentralized manner.

This is a completely decentralized, peer to peer network and offers the following additional functionalities :

- Network Propogation and Broadcasting: Messages are efficiently broadcasted through the network without the need of establishing direct links between any two nodes.
- Spam Protection : Ensures that a node doesn't broadcast the same message repeatedly thereby flooding the network unnecesarily.

## Dolev-Strong Protocol Implementation

Our network module is fortified with the robust **Dolev-Strong** protocol, ensuring seamless consensus among interconnected nodes within the peer-to-peer network. Spearheaded by the miner, this protocol orchestrates the dissemination of blocks while achieving unanimity among the network nodes.

The implementation employs a **bitmasking** technique to track the status of signatures associated with each message. In this approach, each node is authorized to set its corresponding bit to 1 upon integrating a message into its pool. Subsequently, the node appends its signature to the message and propagates the message across the network.

Following a series of k rounds, if a solitary block emerges within the message pool of a node, it is deemed as the accepted block, signaling successful consensus attainment.

## How to Run

After cloning the repository in your local machine, navigate to the corresponding directory and run the following command :

- python p2pnetwork.py

Simply follow the instructions on the terminal to choose your node.
Your machine's IP address will be fetched automatically and then you will be asked to select the port number for the node. Follow the instructions displayed in the console to interact with the node.
