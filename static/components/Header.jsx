import { FaBars } from "react-icons/fa6"
import { useContext, useState } from "react"
import { ActiveContainerTab, ContainerTabTypes } from "../contexts/ActiveContainerTabContext"

import "../scss/header.scss"
import { AccountContext } from "../contexts/AccountContext"

export function Header() {
    const [isResponsive, setIsResponsive] = useState(false)

    const {tab, setTab} = useContext(ActiveContainerTab);
    //const {image, setImage} = useContext(ImageContext)
    const {state, dispatch} = useContext(AccountContext)
    var classes = "header";
    if (isResponsive) {
        classes += " responsive";
    }

    return <div className={classes}>
        <a onClick={() => setTab(ContainerTabTypes.Blog)}>Blog</a>
        <a onClick={() => setTab(ContainerTabTypes.Contact)}>Contact</a>
        {
            state.isLoggedIn ?
            <>
                <a onClick={() => setTab(ContainerTabTypes.Profile)}>Profile</a>
                <a onClick={() => setTab(ContainerTabTypes.Friends)}>Friends</a>
            </> :
            <a onClick={() => setTab(ContainerTabTypes.Login)}>Login</a>
        }

        <a className="icon" onClick={() => setIsResponsive(!isResponsive)}>
            < FaBars />
        </a>
    </div>
}