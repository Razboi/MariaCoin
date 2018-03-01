def get_other_chains():
    network_nodes = []
    other_chains = []
    # get the blockchains of the other nodes
    for node_url in network_nodes:
        block = requests.get(node_url + "/blocks").content
        # convert json to a python dictionary
        block = json.loads(block)
        # add to the list
        other_chains.append(block)

    return other_chains


def consensus(blockchain):
    # get the blockchains from the other nodes
    other_chains = get_other_chains()
    # if a chain is longer than our current blockchain, make it our new blockchain
    for chain in other_chains:
        if len(blockchain) < len(chain):
            blockchain = chain

    return blockchain
