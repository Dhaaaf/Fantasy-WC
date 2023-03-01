import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css"
import argentinaWin from "../../assets/argentina-2022.jpeg"
import iniesta from "../../assets/iniesta-2010.jpeg"
import germanyBrazil from "../../assets/germany-vs-brazil.jpeg"
import zidane from "../../assets/zidane.jpeg"
import brazil2002 from "../../assets/brazil-2002.jpeg"
import griezmann from "../../assets/griezmann-2018.jpeg"
import transferMarket from "../../assets/transferMarket.png"
import leaderBoard from "../../assets/leaderBoard.png"
import teamSelector from "../../assets/teamSelector.png"
import { useHistory } from "react-router-dom";
import { useSelector } from "react-redux";
import React from "react";

import "./SplashPage.css"

function FadeInSection(props) {
    const [isVisible, setVisible] = React.useState(false);
    const domRef = React.useRef();
    React.useEffect(() => {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setVisible(entry.isIntersecting);
          }
        });
      });
  
      const { current } = domRef;
      observer.observe(current);
      return () => observer.unobserve(current);
    }, []);
    return (
      <div
        className={`fade-in-section ${isVisible ? "is-visible" : ""}`}
        ref={domRef}
      >
        {props.children}
      </div>
    );
}


export function SplashPage() {
    const history = useHistory();
	const user = useSelector((state) => state.session.user);


    const handleOpenClick = () => {
        // console.log("SPLASH USER", user)
    }



    return (
        <>
        <div className="splash-container-top">
        <div className="splash-top-details-container">
          <div className="splash-top-details-text">
            <h1 className="splash-header">Welcome to WC Fantasy</h1>
            <div className="splash-top-details-subtext">
              <span>
                Where you can manage a dream team of your favorite world cup heroes of past and present. A place to compete with friends and lead your team to eternal glory.
              </span>
            </div>
          </div>
          <div className="splash-top-details-buttons">
              <button
                // onClick={() => {
                //   setHidden(true);
                //   openForm();
                // }}
                onClick={handleOpenClick}
                className="open-fantasy-button"
              >
                Click the manager button in the top right to start
              </button>
          </div>
        </div>
        <div className="background-image-container">
          {/* <img src={leaderBoard} className="bg-image-left"></img> */}
          <img src={transferMarket} className="bg-image-right"></img>
        </div>
      </div>


      <FadeInSection>
        <div className="splash-body-parent">
          <div className="splash-body-container">
            <div className="splash-body-img-container">
              <img src={teamSelector} className="body-img"></img>
            </div>
            <div className="splash-body-description">
              <h2 className="splash-page-make-team">Select a Team and Earn Points</h2>
              <div className="splash-body-description-text">
                Guide your team through seven matchdays gaining points based on that player's performance during past world cup matches
              </div>
            </div>
          </div>
        </div>
      </FadeInSection>
            <div className="splash-body-footer-parent">
                <div className="splash-body-footer-container">
                    <div className="splash-body-footer-left">
                        <h1>The Beautiful Game</h1>
                    </div>
                    <div className="splash-body-footer-techstack">
                        <h2>Tech Stack</h2>
                        <h3 className="tech-stack">Languages</h3>
                        <li className="tech-stack">Python</li>
                        <li className="tech-stack">JavaScript</li>
                        <li className="tech-stack">HTML</li>
                        <li className="tech-stack">CSS</li>
                        <h3 className="tech-stack">Backend</h3>
                        <li className="tech-stack">Flask</li>
                        <li className="tech-stack">Flask SQL Alchemy</li>
                        <li className="tech-stack">Flask Alembic</li>
                        <h3 className="tech-stack">Frontend</h3>
                        <li className="tech-stack">React</li>
                        <li className="tech-stack">React Router</li>
                        <li className="tech-stack">Redux</li>
                    </div>
                </div>
            </div>
        </>

    )
}
