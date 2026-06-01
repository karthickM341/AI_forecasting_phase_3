import { Link } from "react-router-dom";
import {
  FaTachometerAlt,
  FaUpload,
  FaChartLine,
  FaChartBar,
  FaRobot,
  FaBoxes,
  FaDesktop,
  FaFileAlt,
  FaBell,
  FaUserShield,
  FaCog
} from "react-icons/fa";

function Sidebar() {
  return (
    <div
      style={{
        width: "280px",
        minHeight: "100vh",
        background: "#0d0527",
        padding: "25px",
        borderRight: "1px solid #24114d"
      }}
    >
      <h1
        style={{
          color: "#b85cff",
          marginBottom: "40px",
          fontSize: "42px"
        }}
      >
        AI Forecast
      </h1>

      <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>

        <Link to="/dashboard" style={linkStyle}>
          <FaTachometerAlt /> Dashboard
        </Link>

        <Link to="/upload" style={linkStyle}>
          <FaUpload /> Upload Dataset
        </Link>

        <Link to="/forecast" style={linkStyle}>
          <FaChartLine /> Forecast
        </Link>

        <Link to="/analytics" style={linkStyle}>
          <FaChartBar /> Analytics
        </Link>

        <Link to="/optimization" style={linkStyle}>
          <FaRobot /> AI Optimization
        </Link>

        <Link to="/inventory" style={linkStyle}>
          <FaBoxes /> Inventory
        </Link>

        <Link to="/monitoring" style={linkStyle}>
          <FaDesktop /> Monitoring
        </Link>

        <Link to="/reports" style={linkStyle}>
          <FaFileAlt /> Reports
        </Link>

        <Link to="/notifications" style={linkStyle}>
          <FaBell /> Notifications
        </Link>

        <Link to="/admin" style={linkStyle}>
          <FaUserShield /> Admin
        </Link>

        <Link to="/settings" style={linkStyle}>
          <FaCog /> Settings
        </Link>

      </div>
    </div>
  );
}

const linkStyle = {
  color: "white",
  textDecoration: "none",
  padding: "14px",
  borderRadius: "10px",
  display: "flex",
  alignItems: "center",
  gap: "10px",
  background: "#1a103d"
};

export default Sidebar;