import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleLogin = () => {

        if (!email || !password) {
            setError("Please enter email and password");
            return;
        }

        localStorage.setItem(
            "token",
            "demo-token"
        );

        navigate("/dashboard");
    };

    return (

        <div
            style={{
                display: "flex",
                minHeight: "100vh",
                background: "#0b0620",
                color: "white"
            }}
        >

            {/* LEFT SIDE */}

            <div
                style={{
                    flex: 1,
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    padding: "40px"
                }}
            >

                <div>

                    <h1
                        style={{
                            fontSize: "52px",
                            marginBottom: "20px"
                        }}
                    >
                        AI Demand Forecasting
                    </h1>

                    <p
                        style={{
                            fontSize: "18px",
                            color: "#cbd5e1"
                        }}
                    >
                        Smart forecasting platform powered by
                        AI analytics, inventory intelligence,
                        and demand prediction systems.
                    </p>

                </div>

            </div>

            {/* RIGHT SIDE */}

            <div
                style={{
                    flex: 1,
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center"
                }}
            >

                <div
                    style={{
                        width: "400px",
                        background: "#151530",
                        padding: "40px",
                        borderRadius: "20px",
                        boxShadow: "0 4px 20px rgba(0,0,0,0.4)"
                    }}
                >

                    <h2>Welcome Back</h2>

                    <p
                        style={{
                            color: "#94a3b8",
                            marginBottom: "20px"
                        }}
                    >
                        Login to continue
                    </p>

                    {error && (
                        <p
                            style={{
                                color: "#ef4444",
                                marginBottom: "15px"
                            }}
                        >
                            {error}
                        </p>
                    )}

                    <input
                        type="email"
                        placeholder="Enter your email"
                        value={email}
                        onChange={(e) =>
                            setEmail(e.target.value)
                        }
                        style={{
                            width: "100%",
                            padding: "12px",
                            marginBottom: "15px",
                            borderRadius: "8px",
                            border: "none"
                        }}
                    />

                    <input
                        type="password"
                        placeholder="Enter your password"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                        style={{
                            width: "100%",
                            padding: "12px",
                            marginBottom: "20px",
                            borderRadius: "8px",
                            border: "none"
                        }}
                    />

                    <button
                        onClick={handleLogin}
                        style={{
                            width: "100%",
                            padding: "12px",
                            border: "none",
                            borderRadius: "8px",
                            background: "#6366f1",
                            color: "white",
                            fontSize: "16px",
                            cursor: "pointer"
                        }}
                    >
                        Login
                    </button>

                </div>

            </div>

        </div>
    );
}

export default Login;