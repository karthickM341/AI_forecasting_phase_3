import {
    BrowserRouter,
    Routes,
    Route,
    Navigate
}
from "react-router-dom";

/* PAGES */
import Admin from "../pages/Admin";
import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import Forecast from "../pages/Forecast";
import Inventory from "../pages/Inventory";
import Monitoring from "../pages/Monitoring";
import Reports from "../pages/Reports";
import Notifications from "../pages/Notifications";
import Upload from "../pages/Upload";
import Analytics from "../pages/Analytics";
import Optimization from "../pages/Optimization";

/* PROTECTED ROUTE */

function ProtectedRoute({ children }) {

    const token =
        localStorage.getItem("token");

    return token
        ? children
        : <Navigate to="/" />;
}


/* ROUTES */

function AppRoutes() {

    return (

        <BrowserRouter>

            <Routes>

                {/* LOGIN */}

                <Route
                    path="/"
                    element={<Login />}
                />


                {/* DASHBOARD */}

                <Route
                    path="/dashboard"
                    element={
                        <ProtectedRoute>

                            <Dashboard />

                        </ProtectedRoute>
                    }
                />


                {/* UPLOAD */}

                <Route
                    path="/upload"
                    element={
                        <ProtectedRoute>

                            <Upload />

                        </ProtectedRoute>
                    }
                />


                {/* FORECAST */}

                <Route
                    path="/forecast"
                    element={
                        <ProtectedRoute>

                            <Forecast />

                        </ProtectedRoute>
                    }
                />


                {/* REPORTS */}

                <Route
                    path="/reports"
                    element={
                        <ProtectedRoute>

                            <Reports />

                        </ProtectedRoute>
                    }
                />


                {/* NOTIFICATIONS */}

                <Route
                    path="/notifications"
                    element={
                        <ProtectedRoute>

                            <Notifications />

                        </ProtectedRoute>
                    }
                />


                {/* ADMIN */}

                <Route
                    path="/admin"
                    element={
                        <ProtectedRoute>

                            <Admin />

                        </ProtectedRoute>
                    }
                />


                {/* SETTINGS */}

                <Route
                    path="/settings"
                    element={
                        <ProtectedRoute>

                            <div
                                style={{
                                    color: "white",
                                    padding: "40px"
                                }}
                            >
                                Settings Page
                            </div>

                        </ProtectedRoute>
                    }
                />

                <Route
                        path="/analytics"
                             element={
                                <ProtectedRoute>
                 
                                    <Analytics />
                 
                                 </ProtectedRoute>
                    }
                />

                <Route
                        path="/optimization"
                             element={
                                 <ProtectedRoute>
                                
                                    <Optimization />
                                    
                                </ProtectedRoute>
                    }
                />

                <Route
                        path="/monitoring"
                            element={
                                 <ProtectedRoute>
                 
                                      <Monitoring />
                 
                                 </ProtectedRoute>
                    }
                />

                <Route
                        path="/inventory"
                            element={
                                  <ProtectedRoute>
                 
                                        <Inventory />
                 
                                  </ProtectedRoute>
                    }
                />


                {/* DEFAULT */}

                <Route
                    path="*"
                    element={
                        <Navigate
                            to="/dashboard"
                        />
                    }
                />

            </Routes>

        </BrowserRouter>
    );
}

export default AppRoutes;