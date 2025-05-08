document.addEventListener("DOMContentLoaded", function () {
    initNavigation();
    fetchIncidents();
    fetchLogs();
    loadGraph();
    setupPredictionForm();
    setupLiveSocket();
    loadMap();

    // Auto refresh logs and incidents
    setInterval(fetchIncidents, 5000);  // Incident data refresh every 5 seconds
    setInterval(fetchLogs, 5000);  // Log data refresh every 5 seconds
});

// 🔹 Navigation Control
function initNavigation() {
    const navItems = document.querySelectorAll(".nav-item");
    const sections = document.querySelectorAll(".content-section");

    navItems.forEach(item => {
        item.addEventListener("click", function () {
            navItems.forEach(nav => nav.classList.remove("active"));
            this.classList.add("active");

            sections.forEach(section => section.classList.add("hidden"));
            const target = document.getElementById(this.dataset.target);
            if (target) target.classList.remove("hidden");
        });
    });
}

// 🔹 Incident Fetching
function fetchIncidents() {
    fetch("http://127.0.0.1:5000/api/incidents")
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("incidentTable");
            if (!table) return;
            table.innerHTML = ""; // Clear the table before populating new data
            data.forEach(incident => {
                table.innerHTML += `
                    <tr>
                        <td>${incident.id}</td>
                        <td>${incident.description}</td>
                        <td>${incident.severity}</td>
                        <td>${incident.status}</td>
                        <td>${incident.created_at}</td>
                    </tr>`;
            });

            // Update the statistics
            updateIncidentStats(data);  // Automatically update stats when incidents are fetched
        })
        .catch(err => console.error("Error fetching incidents:", err));
}

// 🔹 Update Incident Stats (Automatically updates the statistics in the section)
function updateIncidentStats(data) {
    const totalIncidents = data.length;
    const criticalThreats = data.filter(i => i.severity === "Critical").length;
    const activeAlerts = data.filter(i => i.status === "Active").length;

    // Update stats in the HTML (for real-time updates)
    document.getElementById("total-incidents").innerText = totalIncidents;
    document.getElementById("critical-threats").innerText = criticalThreats;
    document.getElementById("active-alerts").innerText = activeAlerts;
}

// 🔹 Log Fetching (Latest on Top)
function fetchLogs() {
    fetch("http://127.0.0.1:5000/api/logs")
        .then(res => res.json())
        .then(data => {
            const container = document.getElementById("logs-container");
            if (!container) return;
            container.innerHTML = "";

            data.logs.reverse().forEach(log => {
                const p = document.createElement("p");
                p.textContent = log;
                container.appendChild(p);
            });
        })
        .catch(err => console.error("Error fetching logs:", err));
}

// 🔹 ML Prediction Form Submission
function setupPredictionForm() {
    const form = document.getElementById("predict-form");
    if (!form) return;

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Convert values
        for (let key in data) {
            if (!isNaN(data[key])) data[key] = Number(data[key]);
        }

        fetch("http://127.0.0.1:5000/api/predict-log", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(result => {
            document.getElementById("ml-prediction-result").innerText = `🧠 Predicted: ${result.prediction}`;
        })
        .catch(err => {
            console.error("ML prediction failed:", err);
            document.getElementById("ml-prediction-result").innerText = "❌ Prediction failed.";
        });
    });
}

// 🔹 Donut Graph Loader
function loadGraph() {
    const ctx = document.getElementById("incidentChart").getContext("2d");
    new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ['Low', 'Medium', 'High', 'Critical'],
            datasets: [{
                data: [5, 10, 7, 3],  // Sample data for demonstration
                backgroundColor: ["#4caf50", "#ff9800", "#f44336", "#9c27b0"],
                hoverOffset: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: "65%",
            plugins: { legend: { position: "bottom" } }
        }
    });
}

// 🔹 Socket.IO for Live Alerts
function setupLiveSocket() {
    if (typeof io === 'undefined') {
        console.error("⚠️ Socket.IO not loaded. Make sure it's included via CDN.");
        return;
    }

    const socket = io("http://127.0.0.1:5000");
    const alertsList = document.getElementById("alerts-list");

    socket.on("new_alert", function (alert) {
        const item = document.createElement("li");
        item.innerHTML = `<strong>${alert.type}</strong> - <b>${alert.severity}</b><br>IP: ${alert.source_ip}<br>${alert.timestamp}`;
        item.className = `alert-item ${alert.severity.toLowerCase()}`;
        alertsList.prepend(item);
    });
}

// 🔹 Load Cyber Attack Map
function loadMap() {
    const map = L.map('map').setView([20, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    function fetchAttackData() {
        fetch("/get_attacks")
            .then(res => res.json())
            .then(data => {
                data.forEach(attack => {
                    L.marker([attack.latitude, attack.longitude])
                        .addTo(map)
                        .bindPopup(`<b>${attack.type}</b><br>From: ${attack.source_ip}<br>To: ${attack.target_ip}`);
                });
            });
    }

    fetchAttackData();
    setInterval(fetchAttackData, 5000);
}
