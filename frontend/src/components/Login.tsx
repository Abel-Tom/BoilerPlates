
import { useNavigate } from "react-router-dom";
import { Formik, Field, Form, ErrorMessage } from "formik";
import * as Yup from "yup";

import AuthService from "../services/auth.service";
import { useEffect, useState } from "react";
import EventBus from "../common/EventBus";

interface Props {
    refresh: string | null;
}

type State = {
    redirect: string | null,
    username: string,
    password: string,
    loading: boolean,
    message: string
};

const Login2 = (props: Props) => {

    const navigate = useNavigate();
    const [state, setState] = useState<State>({
        redirect: null,
        username: "",
        password: "",
        loading: false,
        message: ""
    });
    const validationSchema = () => {
        return Yup.object().shape({
            username: Yup.string().email("This is not a valid email.").required("This field is required!"),
            password: Yup.string().required("This field is required!"),
        });
    }

    const handleLogin = (formValue: { username: string; password: string }) => {
        const { username, password } = formValue;


        setState({
            ...state,
            message: "",
            loading: true
        });
        AuthService.login(username, password).then(
            () => {
                setState({
                    ...state,
                    redirect: "/home"
                });
                navigate('/home');
            },
            error => {
                const resMessage =
                    (error.response &&
                        error.response.data &&
                        error.response.data.message) ||
                    error.message ||
                    error.toString();

                setState({
                    ...state,
                    loading: false,
                    message: resMessage
                });
            }
        );
    }
    useEffect(() => {

        const currentUser = AuthService.getCurrentUser();

        if (currentUser) {
            setState({
                ...state,
                redirect: "/home"
            });
        };

        if (props.refresh) {
            navigate('/home')
        }

        const handleLogout = () => {
            navigate('/login');
        }
        EventBus.on("logout", handleLogout)
        return () => {
            EventBus.remove("logout", handleLogout);
        }

    }, [state, navigate, props]);
    const { loading, message } = state;

    const initialValues = {
        username: "",
        password: "",
    };

    return (
        <div className="col-md-12">
            <h1>login 2</h1>
            <div className="card card-container">
                <img
                    src="//ssl.gstatic.com/accounts/ui/avatar_2x.png"
                    alt="profile-img"
                    className="profile-img-card"
                />

                <Formik
                    initialValues={initialValues}
                    validationSchema={validationSchema}
                    onSubmit={handleLogin}
                >
                    <Form>
                        <div className="form-group">
                            <label htmlFor="username">Email</label>
                            <Field name="username" type="text" className="form-control" />
                            <ErrorMessage
                                name="username"
                                component="div"
                                className="alert alert-danger"
                            />
                        </div>

                        <div className="form-group">
                            <label htmlFor="password">Password</label>
                            <Field name="password" type="password" className="form-control" />
                            <ErrorMessage
                                name="password"
                                component="div"
                                className="alert alert-danger"
                            />
                        </div>

                        <div className="form-group">
                            <button type="submit" className="btn btn-primary btn-block" disabled={loading}>
                                {loading && (
                                    <span className="spinner-border spinner-border-sm"></span>
                                )}
                                <span>Login</span>
                            </button>
                        </div>

                        {message && (
                            <div className="form-group">
                                <div className="alert alert-danger" role="alert">
                                    {message}
                                </div>
                            </div>
                        )}
                    </Form>
                </Formik>
            </div>
        </div>
    );

}

export default Login2;