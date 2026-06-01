import React from "react";
import MainLayout from "../layouts/MainLayout";

function Admin() {

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
                    Admin Dashboard
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
                        <h3>Total Users</h3>
                        <h1>245</h1>
                    </div>

                    <div style={cardStyle}>
                        <h3>Active Sessions</h3>
                        <h1>87</h1>
                    </div>

                    <div style={cardStyle}>
                        <h3>System Health</h3>
                        <h1>99.8%</h1>
                    </div>

                    <div style={cardStyle}>
                        <h3>API Requests</h3>
                        <h1>12.4K</h1>
                    </div>

                </div>

                <div
                    style={{
                        display: "grid",
                        gridTemplateColumns: "2fr 1fr",
                        gap: "20px",
                        marginBottom: "20px"
                    }}
                >

                    <div style={cardStyle}>

                        <h2>User Management</h2>

                        <table
                            style={{
                                width: "100%",
                                marginTop: "15px"
                            }}
                        >
                            <thead>
                                <tr>
                                    <th align="left">User</th>
                                    <th align="left">Role</th>
                                    <th align="left">Status</th>
                                </tr>
                            </thead>

                            <tbody>
                                <tr>
                                    <td>Admin</td>
                                    <td>Super Admin</td>
                                    <td>Active</td>
                                </tr>

                                <tr>
                                    <td>Manager</td>
                                    <td>Analyst</td>
                                    <td>Active</td>
                                </tr>

                                <tr>
                                    <td>Forecast User</td>
                                    <td>User</td>
                                    <td>Active</td>
                                </tr>
                            </tbody>
                        </table>

                    </div>

                    <div style={cardStyle}>

                        <h2>Quick Actions</h2>

                        <button
                            style={{
                                width: "100%",
                                padding: "12px",
                                marginTop: "10px",
                                borderRadius: "8px",
                                border: "none"
                            }}
                        >
                            Add User
                        </button>

                        <button
                            style={{
                                width: "100%",
                                padding: "12px",
                                marginTop: "10px",
                                borderRadius: "8px",
                                border: "none"
                            }}
                        >
                            Manage Roles
                        </button>

                        <button
                            style={{
                                width: "100%",
                                padding: "12px",
                                marginTop: "10px",
                                borderRadius: "8px",
                                border: "none"
                            }}
                        >
                            System Settings
                        </button>

                    </div>

                </div>

                <div style={cardStyle}>

                    <h2>System Activity</h2>

                    <ul>
                        <li>User login successful</li>
                        <li>Forecast model updated</li>
                        <li>Inventory sync completed</li>
                        <li>Database backup successful</li>
                        <li>Analytics report generated</li>
                    </ul>

                </div>

            </div>

        </MainLayout>
    );
}

export default Admin;