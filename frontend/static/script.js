document.addEventListener("DOMContentLoaded", function () {
    const navItems = document.querySelectorAll(".nav-item");
    const sections = document.querySelectorAll(".content-section");

    navItems.forEach(item => {
        item.addEventListener("click", function () {
            navItems.forEach(nav => nav.classList.remove("active"));
            this.classList.add("active");

            sections.forEach(section => section.classList.add("hidden"));
            const targetSection = document.getElementById(this.dataset.target);
            if (targetSection) {
                targetSection.classList.remove("hidden");
            }
        });
    });

    fetchIncidents();  // Fetch incidents on page load
    loadGraph();       // Load graph on page load
    fetchLiveAlerts(); // Fetch live alerts
    fetchLogs();       // Fetch logs on page load
});

// 🚀 Fetch Threat Logs from API and Update UI
function fetchIncidents() {
    fetch("http://127.0.0.1:5000/api/incidents")
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("incidentTable");
            if (!tableBody) return;
            tableBody.innerHTML = ""; // Clear old data

            data.forEach(incident => {
                let row = `
                    <tr>
                        <td>${incident.id}</td>
                        <td>${incident.description}</td>
                        <td>${incident.severity}</td>
                        <td>${incident.status}</td>
                        <td>${incident.created_at}</td>
                    </tr>`;
                tableBody.innerHTML += row;
            });

            // ✅ Update Stats on Dashboard
            document.getElementById("total-incidents").innerText = data.length;
            document.getElementById("critical-threats").innerText = data.filter(i => i.severity === "Critical").length;
            document.getElementById("active-alerts").innerText = data.filter(i => i.status === "Active").length;
        })
        .catch(error => console.error("Error fetching incidents:", error));
}

// ✅ Fetch Logs from Server Log File and Display on UI
function fetchLogs() {
    fetch("http://127.0.0.1:5000/api/logs")
        .then(response => response.json())
        .then(data => {
            let logsContainer = document.getElementById("logs-container");
            if (!logsContainer) return;

            logsContainer.innerHTML = ""; // Clear previous logs
            data.logs.forEach(log => {
                let logEntry = document.createElement("p");
                logEntry.textContent = log;
                logsContainer.appendChild(logEntry);
            });
        })
        .catch(error => console.error("Error fetching logs:", error));
}

// ✅ Run fetchLogs() Every 5 Seconds for Live Log Updates
setInterval(fetchLogs, 5000);

// ✅ Run fetchIncidents() Every 5 Seconds for Live Updates
setInterval(fetchIncidents, 5000);

// 🔥 WebSocket for Live Alerts
function fetchLiveAlerts() {
    let socket = new WebSocket("ws://127.0.0.1:5000/ws/alerts");
    let alertsList = document.getElementById("alerts-list");

    socket.onmessage = function (event) {
        let alertData = JSON.parse(event.data);
        let listItem = document.createElement("li");
        listItem.innerHTML = `🚨 <strong>${alertData.type}</strong> - <b>${alertData.severity}</b> - ${alertData.source_ip} @ ${alertData.timestamp}`;
        listItem.classList.add("live-alert");
        alertsList.prepend(listItem);
    };
}

// 📊 Load Circular Graph (Smaller Size)
function loadGraph() {
    const ctx = document.getElementById("incidentChart").getContext("2d");
    new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ['Low', 'Medium', 'High', 'Critical'],
            datasets: [{
                data: [5, 10, 7, 3],  // Sample Data
                backgroundColor: ["#4caf50", "#ff9800", "#f44336", "#9c27b0"],
                hoverOffset: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: "65%", // Reduce size inside
            plugins: {
                legend: { position: "bottom" }
            }
        }
    });
}

// 🌍 Live Threat Map Update
document.addEventListener("DOMContentLoaded", function () {
    var map = L.map('map').setView([20, 0], 2);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    function fetchAttackData() {
        fetch('/get_attacks')
        .then(response => response.json())
        .then(data => {
            data.forEach(attack => {
                L.marker([attack.latitude, attack.longitude]).addTo(map)
                 .bindPopup(`<b>${attack.type}</b><br>Source: ${attack.source_ip}<br>Target: ${attack.target_ip}`);
            });
        });
    }

    fetchAttackData();
    setInterval(fetchAttackData, 5000);
});

var socket = io.connect("http://127.0.0.1:5000");

socket.on("new_alert", function (alert) {
    var alertItem = document.createElement("li");
    alertItem.classList.add("alert-item", alert.severity.toLowerCase());
    alertItem.innerHTML = `<b>${alert.type}</b> - ${alert.severity} <br> IP: ${alert.source_ip} <br> ${alert.timestamp}`;
    
    document.getElementById("alerts-list").prepend(alertItem);
});
