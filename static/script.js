function getPunishment() {
    let level = document.getElementById("level").value;

    fetch("/get_punishment", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ level: level })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = 
"你的随机惩罚是：<br><strong>" + data.punishment + "</strong>";
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
