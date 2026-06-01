import MainLayout from "../layouts/MainLayout";
import {
  FaChartLine,
  FaBoxes,
  FaDollarSign,
  FaBell
} from "react-icons/fa";

import {
  LineChart,
  Line,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";

const forecastData = [
  { month: "Jan", sales: 4200 },
  { month: "Feb", sales: 3800 },
  { month: "Mar", sales: 5000 },
  { month: "Apr", sales: 4500 },
  { month: "May", sales: 7000 },
  { month: "Jun", sales: 6500 }
];

const revenueData = [
  { month: "Jan", revenue: 45000 },
  { month: "Feb", revenue: 52000 },
  { month: "Mar", revenue: 61000 },
  { month: "Apr", revenue: 70000 },
  { month: "May", revenue: 85000 },
  { month: "Jun", revenue: 92500 }
];

function Dashboard() {
  return (
    <MainLayout>

      <h1 className="page-title">
        AI Demand Forecasting Dashboard
      </h1>

      {/* KPI CARDS */}

      <div className="stats-grid">

        <div className="stat-card">
          <FaChartLine size={35} />
          <h3>Total Forecasts</h3>
          <h1>1,245</h1>
          <p>Forecasts Generated</p>
        </div>

        <div className="stat-card">
          <FaBoxes size={35} />
          <h3>Inventory Items</h3>
          <h1>3,820</h1>
          <p>Products Managed</p>
        </div>

        <div className="stat-card">
          <FaDollarSign size={35} />
          <h3>Total Revenue</h3>
          <h1>$92.5K</h1>
          <p>Current Month</p>
        </div>

        <div className="stat-card">
          <FaBell size={35} />
          <h3>Alerts</h3>
          <h1>12</h1>
          <p>Pending Notifications</p>
        </div>

      </div>

      {/* MAIN GRID */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "2fr 1fr",
          gap: "20px",
          marginBottom: "20px"
        }}
      >

        {/* FORECAST CHART */}

        <div className="chart-card">

          <h2>
            Demand Forecast Overview
          </h2>

          <ResponsiveContainer
            width="100%"
            height={320}
          >

            <AreaChart data={forecastData}>

              <XAxis dataKey="month" />

              <YAxis />

              <Tooltip />

              <Area
                type="monotone"
                dataKey="sales"
                stroke="#8b5cf6"
                fill="#8b5cf6"
                fillOpacity={0.3}
              />

            </AreaChart>

          </ResponsiveContainer>

        </div>

        {/* AI INSIGHTS */}

        <div className="chart-card">

          <h2>
            AI Insights
          </h2>

          <ul
            style={{
              lineHeight: "2"
            }}
          >
            <li>Demand increasing by 15%</li>
            <li>Revenue growth remains positive</li>
            <li>Inventory stable this week</li>
            <li>Forecast accuracy reached 96%</li>
            <li>Retraining recommended in 3 days</li>
          </ul>

        </div>

      </div>

      {/* SECOND GRID */}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "20px"
        }}
      >

        <div className="chart-card">

          <h2>
            Revenue Trend
          </h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <LineChart data={revenueData}>

              <XAxis dataKey="month" />

              <YAxis />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="revenue"
                stroke="#ec4899"
                strokeWidth={4}
              />

            </LineChart>

          </ResponsiveContainer>

        </div>

        <div className="chart-card">

          <h2>
            Recent Activities
          </h2>

          <div
            style={{
              display: "flex",
              flexDirection: "column",
              gap: "15px"
            }}
          >

            <div className="glass-card">
              Dataset uploaded successfully
            </div>

            <div className="glass-card">
              Forecast model retrained
            </div>

            <div className="glass-card">
              Inventory optimization completed
            </div>

            <div className="glass-card">
              Revenue report generated
            </div>

          </div>

        </div>

      </div>

    </MainLayout>
  );
}

export default Dashboard;