import { useState, useContext } from "react";
import { ThemeContext, ThemeDispachContext } from '../contexts/ThemeContext';
import "../css/header.css"
import { BlogPostsShowingContext, ContactFormShowingContext, LoginShowingContext } from '../contexts/HeaderContext';
import { FaBars, FaMoon, FaSun } from 'react-icons/fa6';

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
            { isLight ? < FaMoon /> : <FaSun />}
        </a>
        <a className="icon" onClick={() => setIsResponsive(!isResponsive)}>
            < FaBars />
        </a>
    </div>
}
