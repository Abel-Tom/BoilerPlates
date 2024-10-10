import { useEffect, useState } from "react";
import { Routes, Route, } from "react-router-dom";
import { useNavigate, } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

import AuthService from "./services/auth.service";
import EventBus from "./common/EventBus";
import Nav from "./components/Nav";
import Home from "./components/Home";
import Things from "./components/Things";
import Login2 from "./components/Login";
import Register2 from "./components/Register";






const App = () => {
    const [refresh, setRefresh] = useState<string | null>(null);
    const navigate = useNavigate();


    useEffect(() => {
        const handleLogout = () => {
            navigate('/login');
        }
        const refresh = AuthService.getRefreshToken();
        if (refresh) {
            setRefresh(refresh);
        }
        EventBus.on("logout", handleLogout)
        return () => {
            EventBus.remove("logout", handleLogout);
        }
    }, [navigate]);

    return (
        <div>
            <Nav refresh={refresh} />
            <div className="container mt-3">
                <Routes>
                    <Route path="/login" element={<Login2 refresh={refresh} />} />
                    <Route path="/" element={<Home />} />
                    <Route path="/things" element={<Things />} />
                    <Route path="/register" element={<Register2 refresh={refresh} />} />
                </Routes>
            </div>

        </div>
    );

}

export default App;