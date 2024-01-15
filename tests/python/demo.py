"""
This is a demo of how to use package platogaze
"""

import python.platogaze as platogaze

# setting up
platogaze.settings(api_key="12345678")  # apiKey in template file(JSON file).

"""
Case 1: Build a template in your python file.
"""

# Build a new template and upload it.
# 可以把这个变量的类型(type)称为Template

# 1/14
test_template = platogaze.create(name="test")
test_template2 = platogaze.create(name="test2")
test_template.add(test_template2, id = "")
test_template.export(path = "")  # 文件夹
new_template = platogaze.load("test_template/test_template.json")

# Define function1 (i.e. The first tool box)
function1 = {
    "type": "standard",
    "input": "需求：[0],[1]",
    "referenceList": [
        {
            "input": "",  # 结合名言说说你的看法。这句话可以在定义工具块时输入，也可以在运行时输入
            "type": "custom",
        },  # custom的input不一定在定义工具块时输入，也可以在最后run的时候放入
        {"input": "牛顿：站在巨人的肩膀上", "type": "fixed"},
    ],
}

test_template.add(function1)


function2 = {
    "type": "standard",
    "input": "结合[1]，在[0]里，提取相关文字并分析",
    "referenceList": [
        {
            "input": "",
            "type": "url",
        },  # https://news.ycombinator.com/news这句话可以在定义工具块时输入，也可以在运行时输入
        {"input": 0, "type": "functionOutput"},
    ],
}

test_template.add(function2)

test_template.run(
    ["结合名言说说你的看法", "https://news.ycombinator.com/news"],
    save_path="./template",
)  # save 表示把template抽象出来，保存到指定地址。如果不填save_path，那么就不把template保存下来。
# 注：有些参数是可选的，需要我们自己设计

# Upload the locally-defined template to www.platogaze.com
test_template.upload(
    template_name="test",
)

"""
Case 2: Run a remote template 
"""
# 未来我会给每个template一个id，让大家能在本地调用它
# results = {output:'...', function_outputs:['..',...]}
# output里面是 被放到编辑区的输出，function_outputs保存所有工具块的输出
results = platogaze.run("remote_template_id")

"""
Case 3: Download a remote template
"""
# 下面的命令会把远端的模版下载到本地的指定目录下，并把template保存到 downloaded_template 这个实例里
downloaded_template = platogaze.download(save_path="./template", template_id="21341234")
