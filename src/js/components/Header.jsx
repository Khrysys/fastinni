import { icon } from '@fortawesome/fontawesome-svg-core/import.macro';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { useState, useContext } from "react";
import { ThemeContext, ThemeDispachContext } from '../contexts/ThemeContext';
import { setCookie } from '../cookies';
import "../css/header.css"
import { BlogPostsShowingContext, ContactFormShowingContext, LoginShowingContext } from '../contexts/HeaderContext';

export function Header() {
    const [isResponsive, setIsResponsive] = useState(false)

    const theme = useContext(ThemeContext)
    const setTheme = useContext(ThemeDispachContext)
    const toggleLoginShowing = useContext(LoginShowingContext)
    const toggleContactShowing = useContext(ContactFormShowingContext)
    const toggleBlogShowing = useContext(BlogPostsShowingContext)
    var classes = "topnav-" + theme;
    if (isResponsive) {
        classes += " responsive";
    }

    var isLight = theme == 'light'

    return <div className={classes}>
        <a onClick={() => {}}></a>
        <a onClick={() => toggleBlogShowing()}>Blog</a>
        <a onClick={() => toggleContactShowing()}>Contact</a>
        <a onClick={() => toggleLoginShowing()}>Login</a>
        <a className="theme-toggle" onClick={() => { setTheme(isLight ? "dark" : "light") }}>
            <FontAwesomeIcon icon={isLight ? icon({ name: "moon" }) : icon({name: "sun"})} />
        </a>
        <a className="icon" onClick={() => setIsResponsive(!isResponsive)}>
            <FontAwesomeIcon icon={icon({ name: "bars" })} />
        </a>
    </div>
}
