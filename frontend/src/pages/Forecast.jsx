import MainLayout from "../layouts/MainLayout";
import {
  LineChart,
  Line,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  AreaChart,
  Area
} from "recharts";

const data = [
  {month:"Jan",sales:4000},
  {month:"Feb",sales:3000},
  {month:"Mar",sales:5000},
  {month:"Apr",sales:4500},
  {month:"May",sales:7000},
  {month:"Jun",sales:6500}
];

function Forecast() {
  return (
    <MainLayout>

      <h1 className="page-title">
        Forecast Analytics
      </h1>

      <div className="stats-grid">

        <div className="stat-card">
          <h3>Forecast Accuracy</h3>
          <h1>96%</h1>
        </div>

        <div className="stat-card">
          <h3>Expected Growth</h3>
          <h1>+24%</h1>
        </div>

        <div className="stat-card">
          <h3>Demand Category</h3>
          <h1>Electronics</h1>
        </div>

        <div className="stat-card">
          <h3>Active Models</h3>
          <h1>4</h1>
        </div>

      </div>

      <div
        style={{
          display:"grid",
          gridTemplateColumns:"2fr 1fr",
          gap:"20px"
        }}
      >

        <div className="chart-card">

          <h2>Future Sales Prediction</h2>

          <ResponsiveContainer width="100%" height={320}>

            <AreaChart data={data}>
              <XAxis dataKey="month"/>
              <YAxis/>
              <Tooltip/>

              <Area
                dataKey="sales"
                stroke="#60a5fa"
                fill="#60a5fa"
                fillOpacity={0.35}
              />
            </AreaChart>

          </ResponsiveContainer>

        </div>

        <div className="chart-card">

          <h2>AI Insights</h2>

          <ul style={{lineHeight:"2"}}>
            <li>Demand expected to increase by 24%</li>
            <li>Electronics category growing rapidly</li>
            <li>XGBoost model performing best</li>
            <li>Inventory replenishment recommended</li>
          </ul>

        </div>

      </div>

    </MainLayout>
  );
}

export default Forecast;