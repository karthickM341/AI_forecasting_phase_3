import Sidebar from "../components/Sidebar";

function MainLayout({ children }) {
  return (
    <div className="main-layout">
      <Sidebar />

      <div className="main-content">
        {children}
      </div>
    </div>
  );
}

export default MainLayout;