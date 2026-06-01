import MainLayout from "../layouts/MainLayout";

function Inventory() {
  return (
    <MainLayout>

      <h1 className="page-title">
        Inventory Management
      </h1>

      {/* KPI CARDS */}

      <div className="stats-grid">

        <div className="stat-card">
          <h3>Total Products</h3>
          <h1>3,820</h1>
        </div>

        <div className="stat-card">
          <h3>Low Stock</h3>
          <h1>28</h1>
        </div>

        <div className="stat-card">
          <h3>Warehouses</h3>
          <h1>12</h1>
        </div>

        <div className="stat-card">
          <h3>Inventory Health</h3>
          <h1>94%</h1>
        </div>

      </div>

      {/* ANALYTICS */}

      <div className="chart-grid">

        <div className="chart-card">

          <h2>
            Inventory Forecast
          </h2>

          <img
            src="https://quickchart.io/chart?c={type:'bar',data:{labels:['Jan','Feb','Mar','Apr','May','Jun'],datasets:[{label:'Stock',data:[4500,4300,4100,3900,3700,3820]}]}}"
            width="100%"
          />

        </div>

        <div className="chart-card">

          <h2>
            AI Recommendations
          </h2>

          <ul>
            <li>Increase Electronics stock by 15%</li>
            <li>Reduce excess Clothing inventory</li>
            <li>Reorder Product A immediately</li>
            <li>Optimize Warehouse #4</li>
            <li>Demand spike expected next month</li>
          </ul>

        </div>

      </div>

      {/* INVENTORY TABLE */}

      <div
        className="table-card"
        style={{ marginTop: "25px" }}
      >

        <h2 style={{ marginBottom: "20px" }}>
          Inventory Overview
        </h2>

        <table>

          <thead>

            <tr>
              <th>Product</th>
              <th>Category</th>
              <th>Stock</th>
              <th>Status</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Laptop Pro</td>
              <td>Electronics</td>
              <td>340</td>
              <td>Healthy</td>
            </tr>

            <tr>
              <td>Wireless Mouse</td>
              <td>Electronics</td>
              <td>45</td>
              <td>Low Stock</td>
            </tr>

            <tr>
              <td>Keyboard X</td>
              <td>Electronics</td>
              <td>18</td>
              <td>Critical</td>
            </tr>

            <tr>
              <td>Headphones</td>
              <td>Accessories</td>
              <td>290</td>
              <td>Healthy</td>
            </tr>

          </tbody>

        </table>

      </div>

    </MainLayout>
  );
}

export default Inventory;