import { Link, useLocation } from "react-router-dom";
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

  const location = useLocation();

  const menuItems = [
    { name: "Dashboard", icon: <FaTachometerAlt />, path: "/dashboard" },
    { name: "Upload Dataset", icon: <FaUpload />, path: "/upload" },
    { name: "Forecast", icon: <FaChartLine />, path: "/forecast" },
    { name: "Analytics", icon: <FaChartBar />, path: "/analytics" },
    { name: "AI Optimization", icon: <FaRobot />, path: "/optimization" },
    { name: "Inventory", icon: <FaBoxes />, path: "/inventory" },
    { name: "Monitoring", icon: <FaDesktop />, path: "/monitoring" },
    { name: "Reports", icon: <FaFileAlt />, path: "/reports" },
    { name: "Notifications", icon: <FaBell />, path: "/notifications" },
    { name: "Admin", icon: <FaUserShield />, path: "/admin" },
    { name: "Settings", icon: <FaCog />, path: "/settings" }
  ];

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
          fontSize: "48px",
          fontWeight: "bold"
        }}
      >
        AI Forecast
      </h1>

      {menuItems.map((item) => (

        <Link
          key={item.path}
          to={item.path}
          style={{
            display: "flex",
            alignItems: "center",
            gap: "12px",
            textDecoration: "none",
            color: "white",
            padding: "15px",
            borderRadius: "12px",
            marginBottom: "10px",
            background:
              location.pathname === item.path
                ? "linear-gradient(90deg,#8b5cf6,#ec4899)"
                : "transparent",
            transition: "0.3s"
          }}
        >
          {item.icon}
          {item.name}
        </Link>

      ))}
    </div>
  );
}

export default Sidebar;