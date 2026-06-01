import MainLayout from "../layouts/MainLayout";

function Optimization() {
  return (
    <MainLayout>

      <h1 className="page-title">
        AI Optimization Center
      </h1>

      {/* KPI Cards */}

      <div className="stats-grid">

        <div className="stat-card">
          <h3>Model Accuracy</h3>
          <h1>96%</h1>
        </div>

        <div className="stat-card">
          <h3>Active Models</h3>
          <h1>4</h1>
        </div>

        <div className="stat-card">
          <h3>Anomalies Found</h3>
          <h1>12</h1>
        </div>

        <div className="stat-card">
          <h3>Retraining Jobs</h3>
          <h1>8</h1>
        </div>

      </div>

      {/* Main Grid */}

      <div className="chart-grid">

        <div className="chart-card">

          <h2>
            Model Performance
          </h2>

          <img
            src="https://quickchart.io/chart?c={type:'line',data:{labels:['Jan','Feb','Mar','Apr','May','Jun'],datasets:[{label:'Accuracy',data:[89,91,92,94,95,96]}]}}"
            width="100%"
          />

        </div>

        <div className="chart-card">

          <h2>
            AI Insights
          </h2>

          <ul>
            <li>Forecast accuracy improved by 5%</li>
            <li>XGBoost currently best performer</li>
            <li>Demand anomaly detected in Region A</li>
            <li>Retraining recommended this week</li>
            <li>Inventory optimization active</li>
          </ul>

        </div>

      </div>

      {/* Table */}

      <div
        className="table-card"
        style={{ marginTop: "25px" }}
      >

        <h2 style={{ marginBottom: "20px" }}>
          AI Models
        </h2>

        <table>

          <thead>

            <tr>
              <th>Model</th>
              <th>Accuracy</th>
              <th>Status</th>
              <th>Last Retrained</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>XGBoost</td>
              <td>96%</td>
              <td>Active</td>
              <td>2 Days Ago</td>
            </tr>

            <tr>
              <td>Random Forest</td>
              <td>94%</td>
              <td>Active</td>
              <td>5 Days Ago</td>
            </tr>

            <tr>
              <td>Linear Regression</td>
              <td>89%</td>
              <td>Standby</td>
              <td>7 Days Ago</td>
            </tr>

            <tr>
              <td>ARIMA</td>
              <td>91%</td>
              <td>Active</td>
              <td>3 Days Ago</td>
            </tr>

          </tbody>

        </table>

      </div>

    </MainLayout>
  );
}

export default Optimization;