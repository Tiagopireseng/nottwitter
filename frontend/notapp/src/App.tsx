import React, { useEffect, useState } from "react";
import GlobalStyles from "./styles/GlobalStyles";
import Layout from "./components/Layout";
import { UserAuth } from "./userauth";

function App() {
    const [tweets, setTweets] = useState([]);
    const [user, setUser] = useState("");
    const [token, setToken] = useState("");

    useEffect(() => {
        async function login(username: string, password: string) {
            const response = await fetch(
                //post username and password to login to localhost:8000/login
                "http://localhost:8000/login/",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    },
                    body: JSON.stringify({
                        username,
                        password,
                    }),
                }
            );
            const data = await response.json();
            console.log(data);
            setUser(data.user);
            setToken(data.token);
            return data;
        }
        login("tiago", "123");
        console.log(user)
    }, []);

    useEffect(() => {
        async function loadTweets() {
            console.log(token)
            const response = await fetch("http://localhost:8000/tweet/", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "Authorization": `Token ${token}`,
                    },
                    });
            const data = await response.json();
            setTweets(data);
            console.log(tweets);
        }
        loadTweets();
    }, [token]);

    return (
        <div className="App">
            <Layout />
            <GlobalStyles />
        </div>
    );
}

export default App;
