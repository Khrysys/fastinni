import { FaMoon, FaBars, FaSun } from "react-icons/fa6"
import { useContext, useState } from "react"
import { ActiveContainerTabDispatch, BlogPostsShowingContext, ContactFormShowingContext, ContainerTabs, LoginShowingContext, ProfileShowingContext } from "../contexts/ActiveContainerTabContext"

import "../css/header.css"
import { isLoginContext } from "../contexts/AccountContext"

export function Header() {
    const [isResponsive, setIsResponsive] = useState(false)

    const setTab = useContext(ActiveContainerTabDispatch);

    const isLogin = useContext(isLoginContext)
    //const image = useContext(ImageContext)
    //const login = useContext(LoginContext)
    //const setLogin = useContext(LoginDispatchContext)

    var classes = "header";
    if (isResponsive) {
        classes += " responsive";
    }

    return <div className={classes}>
        <a onClick={() => setTab(ContainerTabs.Blog)}>Blog</a>
        <a onClick={() => setTab(ContainerTabs.Contact)}>Contact</a>
        {
            isLogin ?
            <>
                <a onClick={() => setTab(ContainerTabs.Profile)}>Profile</a>
                <a onClick={() => setTab(ContainerTabs.Friends)}>Friends</a>
            </> :
            <a onClick={() => setTab(ContainerTabs.Login)}>Login</a>
        }

        <a className="icon" onClick={() => setIsResponsive(!isResponsive)}>
            < FaBars />
        </a>
    </div>
}