import { icon } from '@fortawesome/fontawesome-svg-core/import.macro';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { useState } from "react";

import "../css/header.css";

export function Header() {
    const [isResponsive, setIsResponsive] = useState(false);
    var classes = "topnav";
    if(isResponsive) {
        classes += " responsive";
    }

    return <div className={classes} id="myTopnav">
        <a href="#home" className="active">Home</a>
        <a href="#news">News</a>
        <a href="#contact">Contact</a>
        <a href="#about">About</a>
        <a className="icon" onClick={() => setIsResponsive(!isResponsive) }>
            < FontAwesomeIcon icon={icon({name:"bars"})}/>
        </a>
    </div>
}