import MainLayout from "../layouts/MainLayout";

function Analytics() {
  return (
    <MainLayout>

      <h1 className="page-title">
        Reports & Analytics
      </h1>

      {/* KPI CARDS */}

      <div className="stats-grid">

        <div className="stat-card">
          <h3>Total Sales</h3>
          <h1>₹33.3L</h1>
        </div>

        <div className="stat-card">
          <h3>Total Profit</h3>
          <h1>₹10L</h1>
        </div>

        <div className="stat-card">
          <h3>Growth Rate</h3>
          <h1>8.8%</h1>
        </div>

        <div className="stat-card">
          <h3>Forecast Accuracy</h3>
          <h1>96%</h1>
        </div>

      </div>

      {/* CHART + REPORTS */}

      <div className="chart-grid">

        <div className="chart-card">

          <h2>Monthly Sales Forecast</h2>

          <img
            src="https://quickchart.io/chart?c={type:'bar',data:{labels:['Jan','Feb','Mar','Apr','May','Jun'],datasets:[{label:'Sales',data:[420,380,520,610,680,720]},{label:'Forecast',data:[450,430,580,670,730,760]}]}}"
            width="100%"
          />

        </div>

        <div className="chart-card">

          <h2>Saved Reports</h2>

          <ul>
            <li>Q1 Sales Report</li>
            <li>Electronics Forecast Q2</li>
            <li>Revenue Insights</li>
            <li>Inventory Analysis</li>
          </ul>

        </div>

      </div>

      {/* TABLE */}

      <div
        className="table-card"
        style={{ marginTop: "25px" }}
      >

        <h2
          style={{
            marginBottom: "20px"
          }}
        >
          Detailed Forecast Report
        </h2>

        <table>

          <thead>

            <tr>
              <th>Month</th>
              <th>Sales</th>
              <th>Forecast</th>
              <th>Growth</th>
              <th>Profit</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>January</td>
              <td>₹420K</td>
              <td>₹450K</td>
              <td>8%</td>
              <td>₹126K</td>
            </tr>

            <tr>
              <td>February</td>
              <td>₹380K</td>
              <td>₹430K</td>
              <td>13%</td>
              <td>₹114K</td>
            </tr>

            <tr>
              <td>March</td>
              <td>₹520K</td>
              <td>₹580K</td>
              <td>11%</td>
              <td>₹156K</td>
            </tr>

            <tr>
              <td>April</td>
              <td>₹610K</td>
              <td>₹670K</td>
              <td>9%</td>
              <td>₹183K</td>
            </tr>

          </tbody>

        </table>

      </div>

    </MainLayout>
  );
}

export default Analytics;