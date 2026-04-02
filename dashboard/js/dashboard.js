async function load() {
    try {
        const res = await fetch("http://localhost:5000/metrics");
        const data = await res.json();

        document.getElementById("status").innerText =
            "Métricas coletadas: " + data.length;
    } catch (e) {
        console.error(e);
        document.getElementById("status").innerText = "Erro na API";
    }
}

setInterval(load, 2000);