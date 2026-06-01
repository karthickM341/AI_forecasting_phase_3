import React from "react";
import MainLayout from "../layouts/MainLayout";

function Upload() {

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
                    Dataset Upload Center
                </h1>

                <div
                    style={{
                        display: "grid",
                        gridTemplateColumns: "repeat(3,1fr)",
                        gap: "20px",
                        marginBottom: "30px"
                    }}
                >

                    <div style={cardStyle}>
                        <h3>Total Datasets</h3>
                        <h1>24</h1>
                    </div>

                    <div style={cardStyle}>
                        <h3>Processed Files</h3>
                        <h1>18</h1>
                    </div>

                    <div style={cardStyle}>
                        <h3>Pending Uploads</h3>
                        <h1>6</h1>
                    </div>

                </div>

                <div style={cardStyle}>

                    <h2>Upload Dataset</h2>

                    <p>
                        Upload CSV files for demand forecasting,
                        inventory analysis, and AI model training.
                    </p>

                    <input
                        type="file"
                        accept=".csv"
                        style={{
                            width: "100%",
                            padding: "12px",
                            marginTop: "20px",
                            marginBottom: "20px",
                            background: "#222244",
                            color: "white",
                            border: "none",
                            borderRadius: "8px"
                        }}
                    />

                    <button
                        style={{
                            padding: "12px 24px",
                            border: "none",
                            borderRadius: "8px",
                            background: "#6366f1",
                            color: "white",
                            cursor: "pointer"
                        }}
                    >
                        Upload Dataset
                    </button>

                </div>

                <div
                    style={{
                        ...cardStyle,
                        marginTop: "20px"
                    }}
                >

                    <h2>Recent Uploads</h2>

                    <table
                        style={{
                            width: "100%",
                            marginTop: "15px"
                        }}
                    >
                        <thead>
                            <tr>
                                <th align="left">File Name</th>
                                <th align="left">Type</th>
                                <th align="left">Status</th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr>
                                <td>sales_data.csv</td>
                                <td>Sales</td>
                                <td>Processed</td>
                            </tr>

                            <tr>
                                <td>inventory.csv</td>
                                <td>Inventory</td>
                                <td>Processed</td>
                            </tr>

                            <tr>
                                <td>demand_forecast.csv</td>
                                <td>Forecast</td>
                                <td>Pending</td>
                            </tr>
                        </tbody>

                    </table>

                </div>

            </div>

        </MainLayout>
    );
}

export default Upload;