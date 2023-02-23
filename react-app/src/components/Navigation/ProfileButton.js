import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout, login } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { useHistory } from "react-router-dom";
import './ProfileButton.css'



function ProfileButton({ user }) {
  const history = useHistory();
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    history.push('/')
    dispatch(logout());
  };

  const demoSignIn = async (e) => {
    e.preventDefault();
    const password = "password"
    const email = "pep@aa.io"
    const data = await dispatch(login(email, password));
    
    history.push(`/leagues`)
  }

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  return (
    <div className='profile-button-container'>
        <button onClick={openMenu} className='profile-button'>
            <div className="profile-button-bars-div">
                <i className="fa-solid fa-user-tie"></i>
            </div>
        </button>
        <div className={ulClassName} ref={ulRef}>
            {user ? (

                <div className="profile-info-actions">
                    <p id="username">{user.username}</p>
                    <p id="profile-email">{user.email}</p>
                    <button onClick={handleLogout} className='fantasywc-button' id='logout-button'>Log Out</button>
                </div>

            ) : (
                <div className="dropdown-menu">
                    <div className="log-in-sign-up">
                        <div id="sign-up-modal">
                            <OpenModalButton
                                modalComponent={<SignupFormModal />}
                                buttonText="Sign Up"
                                onbuttonClick={closeMenu}
                            />
                        </div>
                        <div id="log-in-modal">
                            <OpenModalButton
                                modalComponent={<LoginFormModal />}
                                buttonText="Log In"
                                onbuttonClick={closeMenu}
                            />
                        </div>
                        <button onClick={demoSignIn} type="submit" className='fantasywc-button' id='demo-user-button'>Demo User</button>
                    </div>
                </div>
            )}
        </div>
    </div>
);

  // return (
  //   <>
  //     <button onClick={openMenu}>
  //       <i className="fas fa-user-circle" />
  //     </button>
  //     <ul className={ulClassName} ref={ulRef}>
  //       {user ? (
  //         <>
  //           <li>{user.username}</li>
  //           <li>{user.email}</li>
  //           <li>
  //             <button onClick={handleLogout}>Log Out</button>
  //           </li>
  //         </>
  //       ) : (
  //         <>
  //           <OpenModalButton
  //             buttonText="Log In"
  //             onItemClick={closeMenu}
  //             modalComponent={<LoginFormModal />}
  //           />

  //           <OpenModalButton
  //             buttonText="Sign Up"
  //             onItemClick={closeMenu}
  //             modalComponent={<SignupFormModal />}
  //           />
  //         </>
  //       )}
  //     </ul>
  //   </>
  // );
}

export default ProfileButton;
