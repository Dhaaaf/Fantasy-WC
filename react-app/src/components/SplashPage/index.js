import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css"
import argentinaWin from "../../assets/argentina-2022.jpeg"
import iniesta from "../../assets/iniesta-2010.jpeg"
import germanyBrazil from "../../assets/germany-vs-brazil.jpeg"
import zidane from "../../assets/zidane.jpeg"
import brazil2002 from "../../assets/brazil-2002.jpeg"
import griezmann from "../../assets/griezmann-2018.jpeg"

import "./SplashPage.css"


export function SplashPage() {
    return (
        <>
        <div className="splash-page-outer-div">
            <div className="carousel-div">
            <div className="welcome-div">
                <h2 className="welcome-title">Welcome to Fantasy WC</h2>
                <h3 className="welcome-text">Live out your dreams as you manage world cup heroes of past and present. Login or Sign-up to play!</h3>
            </div>
            <Carousel
                interval={4000}
                transitionTime={1000}
                showArrows={true}
                showStatus={false}
                infiniteLoop
                showThumbs={false}
                autoPlay
                stopOnHover={false}
                showIndicators={false}
            >
                <img src={argentinaWin} />
                <img src={iniesta} />
                <img src={germanyBrazil} />
                <img src={zidane} />
                <img src={brazil2002} />
                <img src={griezmann} />
            </Carousel>
            </div>
        </div>

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
