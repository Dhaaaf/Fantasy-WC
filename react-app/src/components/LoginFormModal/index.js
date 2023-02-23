import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";
import { useHistory } from "react-router-dom";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const history = useHistory();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
        closeModal()
        history.push(`/leagues`)
    }
  };

  return (
    <>
    <div className="form-div">
      <div className="title">
      <div className="form-title">Log In</div>
      </div>
      <form onSubmit={handleSubmit} className='form'>
        <ul className="errors">
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <div className="entries">
          <div className="form-label">
        <label htmlFor="email" className="email">
          Email
         </label>
          </div>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            id='email-input'
          />
        </div>
          <div className="entries">
            <div className="form-label">
        <label htmlFor="password" className="password">
          Password
          </label>
            </div>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            id="password-input"
          />
          </div>
          <div className="form-button">
            <button type="submit" className="submit-button" id="login-button">Log In</button>
          </div>
      </form>
    </div>
    </>
  );
}

export default LoginFormModal;
