import React, {useState} from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import worldCupTrophy from "../../assets/wcLogo.png"
import OpenModalButton from '../OpenModalButton';
import Rules from '../Rules';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
    const [showMenu, setShowMenu] = useState(false);


  const closeMenu = () => setShowMenu(false);

	return (
        <div className='navigation-bar'>
            <div className='nav-innerdiv'>
                <div className='left-nav-div'>
					<div className='main-logo'>
                    	<NavLink exact to="/" className="home-link">
							<img className="world-cup-trophy" src={worldCupTrophy} alt={worldCupTrophy}></img>
						</NavLink>
					</div>
					<div className='fantasy-text'>
						<h1>Fantasy World Cup</h1>
					</div>
                </div>
                {isLoaded && (
                    <div className='right-nav-div'>
                        <div className='right-nav-rules-div'>
                            <OpenModalButton
                                modalComponent={<Rules />}
                                buttonText="Rules"
                                onbuttonClick={closeMenu}
                            />
                        </div>
                        <div className='profile-button'>
                            <ProfileButton user={sessionUser} />
                        </div>
                        <div className='rules-div'>
                        </div>
                    </div>
                )}
            </div>
        </div >
    );
}


export default Navigation;
