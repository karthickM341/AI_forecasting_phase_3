import MainLayout from "../layouts/MainLayout";

function Reports() {
  return (
    <MainLayout>

      <h1 className="page-title">
        Reports Center
      </h1>

      {/* KPI CARDS */}

      <div className="stats-grid">

        <div className="stat-card">
          <h3>Total Reports</h3>
          <h1>128</h1>
        </div>

        <div className="stat-card">
          <h3>Generated Today</h3>
          <h1>12</h1>
        </div>

        <div className="stat-card">
          <h3>Downloads</h3>
          <h1>1,542</h1>
        </div>

        <div className="stat-card">
          <h3>Forecast Reports</h3>
          <h1>56</h1>
        </div>

      </div>

      {/* REPORT ANALYTICS */}

      <div className="chart-grid">

        <div className="chart-card">

          <h2>
            Report Generation Trend
          </h2>

          <img
            src="https://quickchart.io/chart?c={type:'line',data:{labels:['Jan','Feb','Mar','Apr','May','Jun'],datasets:[{label:'Reports',data:[45,60,72,88,110,128]}]}}"
            width="100%"
          />

        </div>

        <div className="chart-card">

          <h2>
            Quick Actions
          </h2>

          <button className="primary-btn">
            Export PDF
          </button>

          <br /><br />

          <button className="primary-btn">
            Export Excel
          </button>

          <br /><br />

          <button className="primary-btn">
            Schedule Report
          </button>

        </div>

      </div>

      {/* REPORT TABLE */}

      <div
        className="table-card"
        style={{ marginTop: "25px" }}
      >

        <h2
          style={{
            marginBottom: "20px"
          }}
        >
          Recent Reports
        </h2>

        <table>

          <thead>

            <tr>
              <th>Report Name</th>
              <th>Category</th>
              <th>Date</th>
              <th>Status</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Monthly Demand Forecast</td>
              <td>Forecasting</td>
              <td>2026-05-01</td>
              <td>Completed</td>
            </tr>

            <tr>
              <td>Inventory Analysis</td>
              <td>Inventory</td>
              <td>2026-05-03</td>
              <td>Completed</td>
            </tr>

            <tr>
              <td>Revenue Summary</td>
              <td>Analytics</td>
              <td>2026-05-05</td>
              <td>Completed</td>
            </tr>

            <tr>
              <td>AI Optimization Report</td>
              <td>AI Models</td>
              <td>2026-05-08</td>
              <td>Completed</td>
            </tr>

          </tbody>

        </table>

      </div>

      {/* EXECUTIVE SUMMARY */}

      <div
        className="chart-card"
        style={{ marginTop: "25px" }}
      >

        <h2>
          Executive Summary
        </h2>

        <ul>
          <li>Revenue increased by 18% this quarter.</li>
          <li>Forecast accuracy improved to 96%.</li>
          <li>Inventory health remains above 94%.</li>
          <li>AI optimization reduced forecasting errors by 12%.</li>
          <li>System uptime maintained at 99.8%.</li>
        </ul>

      </div>

    </MainLayout>
  );
}

export default Reports;