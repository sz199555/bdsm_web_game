from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# BDSM 惩罚任务
punishments = {
    "轻度": [
        "轻轻拍打屁股 10 次",
        "捆绑双手 5 分钟",
        "轻微蜡烛滴落（安全温度）",
        "在房间里裸露 2 分钟",
        "用羽毛在敏感部位撩拨 3 分钟"
    ],
    "中度": [
        "用皮带轻拍屁股 20 次",
        "跪在地板上 5 分钟",
        "戴上眼罩并听从 10 分钟的命令",
        "用冰块刺激敏感部位 2 分钟",
        "被绑住手脚 10 分钟"
    ],
    "重度": [
        "鞭打 30 次（掌握力度）",
        "被拘束在椅子上 15 分钟",
        "温热蜡滴落 5 次",
        "使用口球 10 分钟",
        "被捆绑并进行言语调教 10 分钟"
    ]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_punishment", methods=["POST"])
def get_punishment():
    data = request.get_json()
    level = data.get("level")

    if level in punishments:
        punishment = random.choice(punishments[level])
        return jsonify({"punishment": punishment})
    else:
        return jsonify({"punishment": "请选择一个有效的惩罚等级。"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # 通过环境变量获取端口，默认10000
    app.run(host="0.0.0.0", port=port)  # 设置为可以被所有外部请求访问
    
