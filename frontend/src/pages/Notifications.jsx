import React from "react";
import MainLayout from "../layouts/MainLayout";

function Notifications() {

  const cardStyle = {
    background: "#151530",
    padding: "25px",
    borderRadius: "15px",
    color: "white",
    boxShadow: "0 4px 15px rgba(0,0,0,0.3)"
  };

  return (
    <MainLayout>

      <div
        style={{
          padding: "30px",
          minHeight: "100vh",
          background: "#0b0620",
          color: "white"
        }}
      >

        <h1
          style={{
            fontSize: "42px",
            marginBottom: "30px"
          }}
        >
          Notifications Center
        </h1>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(4,1fr)",
            gap: "20px",
            marginBottom: "30px"
          }}
        >

          <div style={cardStyle}>
            <h3>Total Notifications</h3>
            <h1>156</h1>
          </div>

          <div style={cardStyle}>
            <h3>Unread Alerts</h3>
            <h1>12</h1>
          </div>

          <div style={cardStyle}>
            <h3>Critical Alerts</h3>
            <h1>3</h1>
          </div>

          <div style={cardStyle}>
            <h3>System Messages</h3>
            <h1>27</h1>
          </div>

        </div>

        <div style={cardStyle}>

          <h2>Recent Notifications</h2>

          <table
            style={{
              width: "100%",
              marginTop: "20px"
            }}
          >
            <thead>
              <tr>
                <th align="left">Type</th>
                <th align="left">Message</th>
                <th align="left">Status</th>
              </tr>
            </thead>

            <tbody>
              <tr>
                <td>Forecast</td>
                <td>Demand forecast generated successfully</td>
                <td>Completed</td>
              </tr>

              <tr>
                <td>Inventory</td>
                <td>Low stock detected for Product A</td>
                <td>Warning</td>
              </tr>

              <tr>
                <td>Monitoring</td>
                <td>Server health check passed</td>
                <td>Normal</td>
              </tr>

              <tr>
                <td>AI Model</td>
                <td>Model retraining completed</td>
                <td>Success</td>
              </tr>
            </tbody>
          </table>

        </div>

        <div
          style={{
            ...cardStyle,
            marginTop: "20px"
          }}
        >

          <h2>AI Insights</h2>

          <ul>
            <li>Demand expected to increase by 15% next month.</li>
            <li>Inventory optimization recommended for 8 products.</li>
            <li>No critical system failures detected.</li>
            <li>Forecast accuracy improved to 96%.</li>
          </ul>

        </div>

      </div>

    </MainLayout>
  );
}

export default Notifications;