def proof_of_work(last_proof):
    # variable for finding the next proof of work
    incrementor = last_proof + 1

    # while the incrementor isn't divisible by 9 and
    # the proof of work from the last block keep looping
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1

    return incrementor
