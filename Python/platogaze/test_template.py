from template import Template
from chain import Chain



# file_path = "Python/platogaze/my_template.json"
# with open(file_path, "r") as f:
#     data = json.load(f)

chain1 = Chain(
    {
        "type": "standard",
        "display": False,
        "prompt": [
            "Write a [0] word essay about [1]"
        ],
        "reference_list": [
            {
                "prompt": "500",
                "type": "custom"
            },
            {
                "prompt": "Battlefield 5",
                "type": "fixed"
            }
        ]
    })

chain2 = Chain({
    "type": "standard",
    "display": True,
    "prompt": [
        "Based on [1] find relative words in [0] and analyze them"
    ],
    "reference_list": [
        {
            "prompt": 0,
            "type": "chainOutput"
        },
        {
            "prompt": "https://news.ycombinator.com/news",
            "type": "url"
        }
    ]
})

test_template = Template()
test_template.add_chain(chain1)
test_template.add_chain(chain2)
test_template.save_to_json("saved_template.json")
