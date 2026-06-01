import MainLayout from "../layouts/MainLayout";

function Monitoring() {
  return (
    <MainLayout>

      <h1 className="page-title">
        System Monitoring
      </h1>

      {/* KPI CARDS */}

      <div className="stats-grid">

        <div className="stat-card">
          <h3>CPU Usage</h3>
          <h1>42%</h1>
        </div>

        <div className="stat-card">
          <h3>Memory Usage</h3>
          <h1>68%</h1>
        </div>

        <div className="stat-card">
          <h3>API Requests</h3>
          <h1>247K</h1>
        </div>

        <div className="stat-card">
          <h3>System Uptime</h3>
          <h1>99.8%</h1>
        </div>

      </div>

      {/* CHART SECTION */}

      <div className="chart-grid">

        <div className="chart-card">

          <h2>
            Server Performance
          </h2>

          <img
            src="https://quickchart.io/chart?c={type:'line',data:{labels:['Mon','Tue','Wed','Thu','Fri','Sat','Sun'],datasets:[{label:'CPU',data:[40,38,55,48,60,45,42]},{label:'Memory',data:[62,64,66,65,69,70,68]}]}}"
            width="100%"
          />

        </div>

        <div className="chart-card">

          <h2>
            Service Health
          </h2>

          <ul>

            <li>✅ Forecast API Running</li>
            <li>✅ Database Connected</li>
            <li>✅ Redis Cache Active</li>
            <li>✅ Scheduler Running</li>
            <li>⚠ 2 Warning Logs</li>

          </ul>

        </div>

      </div>

      {/* SERVER TABLE */}

      <div
        className="table-card"
        style={{ marginTop: "25px" }}
      >

        <h2
          style={{
            marginBottom: "20px"
          }}
        >
          Active Services
        </h2>

        <table>

          <thead>

            <tr>
              <th>Service</th>
              <th>Status</th>
              <th>Response Time</th>
              <th>Availability</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Forecast API</td>
              <td>Running</td>
              <td>120 ms</td>
              <td>99.9%</td>
            </tr>

            <tr>
              <td>Database</td>
              <td>Running</td>
              <td>35 ms</td>
              <td>100%</td>
            </tr>

            <tr>
              <td>Redis Cache</td>
              <td>Running</td>
              <td>12 ms</td>
              <td>99.8%</td>
            </tr>

            <tr>
              <td>Background Jobs</td>
              <td>Running</td>
              <td>80 ms</td>
              <td>99.7%</td>
            </tr>

          </tbody>

        </table>

      </div>

    </MainLayout>
  );
}

export default Monitoring;