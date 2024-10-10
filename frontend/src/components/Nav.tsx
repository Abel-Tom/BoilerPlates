
import { Link, useNavigate, } from "react-router-dom";

import AuthService from "../services/auth.service";



interface Props {
  refresh: string | null;
}


const Nav = (props: Props) => {
  const nav = useNavigate();
  const logOut = () => {
    AuthService.logOut();
    console.log('going to login page')
    nav('/login');

  };

  return (
    <nav className="navbar navbar-expand navbar-dark bg-dark">
      <div className="navbar-nav mr-auto">
        <li className="nav-item">
          <Link to={"/home"} className="nav-link">
            Home
          </Link>
        </li>



      </div>

      {props.refresh ? (
        <div className="navbar-nav ml-auto">
          <li className="nav-item">
            <Link to={"/login"} className="nav-link" onClick={logOut}>
              Logout
            </Link>
          </li>
        </div>
      ) : (
        <div className="navbar-nav ml-auto">
          <li className="nav-item">
            <Link to={"/register"} className="nav-link">
              Sign Up
            </Link>
          </li>
        </div>
      )}
    </nav>
  )
}

export default Nav




