import React from "react";
import MainLayout from "../layouts/MainLayout";

function Users() {

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
                    User Management
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
                        <h1>45</h1>
                    </div>

                    <div style={cardStyle}>
                        <h3>Analysts</h3>
                        <h1>12</h1>
                    </div>

                    <div style={cardStyle}>
                        <h3>Viewers</h3>
                        <h1>28</h1>
                    </div>

                    <div style={cardStyle}>
                        <h3>Super Admins</h3>
                        <h1>5</h1>
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

                        <h2>User Directory</h2>

                        <table
                            style={{
                                width: "100%",
                                marginTop: "15px"
                            }}
                        >
                            <thead>
                                <tr>
                                    <th align="left">Name</th>
                                    <th align="left">Role</th>
                                    <th align="left">Status</th>
                                </tr>
                            </thead>

                            <tbody>
                                <tr>
                                    <td>Rithick</td>
                                    <td>Super Admin</td>
                                    <td>Active</td>
                                </tr>

                                <tr>
                                    <td>John</td>
                                    <td>Analyst</td>
                                    <td>Active</td>
                                </tr>

                                <tr>
                                    <td>David</td>
                                    <td>Viewer</td>
                                    <td>Active</td>
                                </tr>

                                <tr>
                                    <td>Sarah</td>
                                    <td>Analyst</td>
                                    <td>Inactive</td>
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
                            Export Users
                        </button>

                    </div>

                </div>

                <div style={cardStyle}>

                    <h2>Recent User Activity</h2>

                    <ul>
                        <li>New analyst account created</li>
                        <li>User role updated successfully</li>
                        <li>Viewer account activated</li>
                        <li>Password reset completed</li>
                        <li>Admin login detected</li>
                    </ul>

                </div>

            </div>

        </MainLayout>
    );
}

export default Users;