$(document).ready(function () {
    // Sample data for incidents (In practice, this should be fetched from your backend)
    let incidents = [
        { id: 1, title: "Incident 1", severity: "high", status: "open", description: "Description for Incident 1" },
        { id: 2, title: "Incident 2", severity: "medium", status: "closed", description: "Description for Incident 2" },
        // Add more incidents as needed
    ];

    // Sample featured incidents
    const featuredIncidents = [
        { id: 1, description: "Data breach at Company A", severity: "Critical" },
        { id: 2, description: "Phishing attempt detected", severity: "High" },
        // Add more featured incidents as needed
    ];

    // Sample activities
    const activities = [
        { time: "2024-10-06 12:30", user: "User1", action: "Logged in" },
        { time: "2024-10-06 12:35", user: "User1", action: "Viewed incident #1" },
        // Add more activities as needed
    ];

    // Function to display incidents in the dashboard
    function displayIncidents() {
        $('#incidentList').empty(); // Clear existing incidents
        incidents.forEach(incident => {
            $('#incidentList').append(`
                <div class="incident border p-2 mb-2 rounded" data-id="${incident.id}">
                    <h6 class="font-bold">${incident.title}</h6>
                    <p>Status: <span class="text-${incident.status === 'open' ? 'danger' : 'success'}">${incident.status}</span></p>
                    <p>Severity: ${incident.severity}</p>
                    <button class="btn btn-info view-details" data-toggle="modal" data-target="#incidentModal" data-id="${incident.id}">View Details</button>
                </div>
            `);
        });
    }

    // Function to load incident details
    function loadIncidentDetails(id) {
        const incident = incidents.find(i => i.id === id);
        if (incident) {
            $('#incidentDetails').text(incident.description);
        } else {
            $('#incidentDetails').text("No details available.");
        }
    }

    // Event listener for incident details button
    $(document).on('click', '.view-details', function () {
        const incidentId = $(this).data('id');
        loadIncidentDetails(incidentId);
    });

    // Implement search functionality
    $('#searchButton').on('click', function () {
        const status = $('#statusFilter').val();
        const severity = $('#severityFilter').val();
        const location = $('#locationSearch').val();

        // Implement your filtering logic here based on selected filters
        // For simplicity, this example does not filter; just refresh the display
        displayIncidents();
    });

    // Initial load of incidents
    displayIncidents();

    // Function to load featured incidents
    function loadFeaturedIncidents() {
        const container = $('#featuredIncidents');
        container.empty(); // Clear existing featured incidents
        featuredIncidents.forEach(incident => {
            const incidentDiv = $(`
                <div class="incident-item border p-2 mb-2 rounded">
                    <h5>${incident.description}</h5>
                    <p>Severity: ${incident.severity}</p>
                </div>
            `);
            container.append(incidentDiv);
        });
    }

    // Call the function to load featured incidents on page load
    loadFeaturedIncidents();

    // Function to load activity log
    function loadActivityLog() {
        const container = $('#activityLog');
        container.empty(); // Clear existing activity log
        activities.forEach(activity => {
            const activityDiv = $(`
                <div class="activity-item">
                    <p><strong>${activity.time}</strong> - ${activity.user}: ${activity.action}</p>
                </div>
            `);
            container.append(activityDiv);
        });
    }

    // Call the function to load activity log on page load
    loadActivityLog();

    // Initialize analytics chart
    const ctxAnalytics = $('#analyticsChart')[0].getContext('2d');
    const analyticsData = {
        labels: ['Critical', 'High', 'Medium', 'Low'],
        datasets: [{
            label: 'Number of Incidents',
            data: [10, 15, 25, 5], // Sample data, replace with real data
            backgroundColor: ['#f87171', '#fbbf24', '#93c5fd', '#34d399'],
            borderColor: ['#b91c1c', '#d7a60a', '#1e3a8a', '#065f46'],
            borderWidth: 1
        }]
    };

    const analyticsChart = new Chart(ctxAnalytics, {
        type: 'bar',
        data: analyticsData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Initialize incident status chart
    const ctxIncidents = $('#incidentChart')[0].getContext('2d');
    const incidentChart = new Chart(ctxIncidents, {
        type: 'bar',
        data: {
            labels: ['Open', 'Closed'],
            datasets: [{
                label: 'Incidents',
                data: [2, 1], // Replace with actual data
                backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
                borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Real-time data updates using WebSocket or AJAX can be implemented here
});
