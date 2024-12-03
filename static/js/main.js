const dropdown = document.getElementById("dropdown");

const data = await fetchSecurityLevel();
dropdown.value = data.level;

dropdown.addEventListener("change", function () {
    const levelOption = this.value;
    localStorage.setItem("level", levelOption);
    if (levelOption) {
        window.location.href = levelOption;
    }
});

function logsWindow() {
    url = window.location.href;
    chunks = url.split('/');
    chunks[chunks.length - 1];
    window.open(`/api/logs?vuln=${chunks[chunks.length - 1]}`, "", "width=600,height=400");
}

async function fetchSecurityLevel() {
    return await fetch(`/api/security_level`, {
        method: "GET",
    })
        .then((response) => {
            if (!response.ok) {
                return null;
            }
            return response?.json();
        })
        .then((data) => {
            return data;
        })
        .catch((error) => {
            console.error("Error:", error);
        });
}