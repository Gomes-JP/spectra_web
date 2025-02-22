let tableData = null;

// Load CSV file
document.getElementById('csv-upload').addEventListener('change', function (e) {
    Papa.parse(e.target.files[0], {
        header: true,
        dynamicTyping: true,
        complete: function (results) {
            tableData = results.data;
            renderTable(tableData);
            toastNotification("File uploaded successfully!");
        },
    });
});

// Render table using Tabulator
function renderTable(data) {
    new Tabulator('#table-area', {
        data: data,
        layout: 'fitColumns',
        columns: Object.keys(data[0]).map((field) => ({ title: field, field })),
    });
}

// Plot HR Diagram
function plotHRD(teff, logL, modelData) {
    const traces = [
        {
            x: modelData.teff,
            y: modelData.logL,
            mode: 'lines',
            name: 'Model',
        },
        {
            x: teff,
            y: logL,
            mode: 'markers',
            name: 'Observed',
        },
    ];
    Plotly.newPlot('plot-area', traces, { title: 'HR Diagram' });
}

// Load isochrone model data
async function loadIsochrone(modelName) {
    const response = await fetch(`models/${modelName}.json`);
    return await response.json();
}

// Example: Isochrone Fitting
document.querySelector('.tab[data-tab="isochrone"]').addEventListener('click', async () => {
    if (!tableData) {
        toastNotification("Please upload a CSV file first!");
        return;
    }

    const modelName = 'siess_evol'; // Example model
    const modelData = await loadIsochrone(modelName);

    const teff = tableData.map((row) => row.Teff);
    const logL = tableData.map((row) => row.logL);

    plotHRD(teff, logL, modelData);
});

// Toast notification
function toastNotification(message) {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

// static/js/widgets.js
class WebSessionManager {
    static saveSession(data) {
        localStorage.setItem('spectra_session', JSON.stringify(data));
    }

    static loadSession() {
        return JSON.parse(localStorage.getItem('spectra_session')) || {};
    }
}

class WebAbout {
    static show() {
        const content = `
            <div class="modal fade" id="aboutModal">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">About SPECTRA</h5>
                        </div>
                        <div class="modal-body">
                            <!-- Add about content here -->
                        </div>
                    </div>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', content);
        new bootstrap.Modal(document.getElementById('aboutModal')).show();
    }
}