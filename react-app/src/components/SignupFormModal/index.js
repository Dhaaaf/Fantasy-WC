import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";
import { useHistory } from "react-router-dom";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();
	const history = useHistory()

	let errorsArray = []

	const handleSubmit = async (e) => {
		e.preventDefault();

		setErrors([])

		if (!email.includes("@")) {
            errorsArray.push("Please enter a valid email")
        }

		if (username.length < 4 || username.length > 20) {
            errorsArray.push("Username must be between 3 and 20 characters")
        }

		if (password.length < 4 || password.length > 50) {
            errorsArray.push("password must be between 3 and 50 characters")
        }

		if (errorsArray.length > 0) setErrors(errorsArray)

		if (errorsArray.length == 0) {
			if (password === confirmPassword) {
				const data = await dispatch(signUp(username, email, password));
				if (data) {
					setErrors(data);
				} else {
					closeModal();
					history.push(`/leagues`)
				}
			} else {
				setErrors([
					"Confirm Password field must be the same as the Password field",
				]);
			}
		}



	};

	return (
		<>
		<div className="form-div">
			<div className="title">
     			<div className="form-title">Sign-up</div>
    		</div>
			<form onSubmit={handleSubmit}>
				<ul className="errors">
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>
				<div className="entries">
        			<div className="form-label">
        				<label htmlFor="email" className="email">Email</label>
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
						<label htmlFor="username" className="username">Username</label>
					</div>
					<input
						type="text"
						value={username}
						onChange={(e) => setUsername(e.target.value)}
						required
						id="username-input"
					/>
				</div>
				<div className="entries">
					<div className="form-label">
						<label htmlFor="password" className="password">Password</label>
					</div>
					<input
						type="password"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
						id="password-input"
					/>
				</div>
				<div className="entries">
					<div className="form-label">
						<label htmlFor="confirmpassword" className="confirmpassword">Confirm Password</label>
					</div>
					<input
						type="password"
						alue={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
						id="confirm-password-input"
					/>
				</div>
				<div className="form-button">
					<button type="submit" className="submit-button" id="signup-button">Sign Up</button>
				</div>
			</form>
		</div>
		</>
	);
}

export default SignupFormModal;
