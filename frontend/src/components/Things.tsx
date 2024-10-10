
import { useEffect, useState } from "react";


import { AxiosResponse } from "axios";

import userService from "../services/user.service";

import { Thing, ThingPayload } from "../types/user.type";

const Things = () => {
    const [things, setThings] = useState<Thing[]>([]);
    const [loading, setLoading] = useState<boolean>(false);
    const [message, setMessage] = useState<string>('');
    

    useEffect(() => {
        const getThings = () => {
            userService.getThings().then(
                (response: AxiosResponse) => {
                    console.log('things ', response.data);
                    setThings(response.data);
                },
                (error: any) => {
                    console.log('err ', error);
                }
            );
        }
        getThings();
    }, []);

    const [username, setUsername] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        console.log(username);
        setLoading(true);
        const payload: ThingPayload = {
            name: username,
        }
        userService.createThing(payload).then(
            (response: AxiosResponse) => {
                console.log(response.data);
                setLoading(false);
                setUsername('');
            },
            (error: any) => {
                console.log(error);
                setMessage(error.message);
                setLoading(false);
            }
        )
    };

    return (
     
        <>
            <h1>Something</h1>
            <ul>
                {things.map((thing,index) => 
                    <li key={index}>{thing.name}</li>
                )}
            </ul>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="username">Username</label>
                    <input type="text" value={username} className="form-control" onChange={(event) => {setUsername(event.target.value)}} /> 
                </div>
            
                <div className="form-group">
                    <button type="submit" className="btn btn-primary btn-block" disabled={loading}>
                    {loading && (
                        <span className="spinner-border spinner-border-sm"></span>
                    )}
                    <span>Create</span>
                    </button>
                </div>
                {message && (
                    <div className="form-group">
                    <div className="alert alert-danger" role="alert">
                        {message}
                    </div>
                    </div>
                )}
            </form>
        </>
    )
}

export default Things