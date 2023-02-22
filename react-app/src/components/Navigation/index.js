import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import worldCupTrophy from "../../assets/wcLogo.png"

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
        <div className='navigation-bar'>
            <div className='nav-innerdiv'>
                <div className='left-nav-div'>
					<div className='main-logo'>
                    	<NavLink exact to="/" className="home-link">
							<img className="world-cup-trophy" src={worldCupTrophy}></img>
						</NavLink>
					</div>
					<div className='fantasy-text'>
						<h1>Fantasy World Cup</h1>
					</div>
                </div>
                {isLoaded && (
                    <div className='right-nav-div'>
                        <div className='profile-button'>
                            <ProfileButton user={sessionUser} />
                        </div>
                    </div>
                )}
            </div>
        </div >
    );
}


export default Navigation;
