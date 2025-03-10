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

    // Fake Incident Data
    const incidentData = [
        { id: 1, type: "DDoS Attack", severity: "Critical", source: "192.168.1.10", status: "Active", timestamp: "2025-03-09 12:00" },
        { id: 2, type: "Unauthorized Access", severity: "High", source: "192.168.1.22", status: "Resolved", timestamp: "2025-03-09 11:45" }
    ];

    const tableBody = document.getElementById("incidentTable");

    incidentData.forEach(incident => {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${incident.id}</td><td>${incident.type}</td><td>${incident.severity}</td><td>${incident.source}</td><td>${incident.status}</td><td>${incident.timestamp}</td>`;
        tableBody.appendChild(row);
    });

    document.getElementById("total-incidents").innerText = incidentData.length;
    document.getElementById("critical-threats").innerText = incidentData.filter(i => i.severity === "Critical").length;
    document.getElementById("active-alerts").innerText = incidentData.filter(i => i.status === "Active").length;

    // Incident Chart
    new Chart(document.getElementById("incidentChart"), {
        type: 'pie',
        data: {
            labels: ['DDoS', 'Unauthorized Access'],
            datasets: [{
                data: [1, 1],
                backgroundColor: ['#ff4c4c', '#ffcc00']
            }]
        }
    });
});


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

document.addEventListener("DOMContentLoaded", function () {
    var socket = io.connect("http://127.0.0.1:5000");
    var alertsList = document.getElementById("alerts-list");

    socket.on("new_alert", function (alert) {
        var alertItem = document.createElement("li");
        alertItem.classList.add("alert-item", alert.severity.toLowerCase());
        alertItem.innerHTML = `<b>${alert.type}</b> - ${alert.severity} <br> IP: ${alert.source_ip} <br> ${alert.timestamp}`;
        
        alertsList.prepend(alertItem); // Add to the top
    });
});

