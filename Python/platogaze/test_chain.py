from chain import Chain

chain1 = {
    "type": "standard",
    "prompt": "Write a [0] hundred word essay about [1]",
    "referenceList": [
        {
            "prompt": "500",
            "type": "custom",
        },
        {
            "prompt": "Battlefield 5",
            "type": "fixed",
        },
    ],
}

testChain1 = Chain(chain1)
testChain1.save_to_json("constructed_chain.json")
