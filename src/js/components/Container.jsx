import { useContext, useState } from "react"
import { ThemeContext } from "../contexts/ThemeContext"
import { Header } from "./Header"
import { Masthead } from "./Masthead"
import { Footer } from "./Footer"
import { LoginShowingContext } from "../contexts/HeaderContext"
import { LoginContainer } from "./LoginContainer"

export function Container() {
    const theme = useContext(ThemeContext)
    const [isLoginShowing, setIsLoginShowing] = useState(false);

    function toggleLoginShowing() {
        setIsLoginShowing(!isLoginShowing);
    }

    return <div className={theme + "-mode"}>
        <LoginShowingContext.Provider value={toggleLoginShowing}>
		    < Header />
        </LoginShowingContext.Provider>
		< Masthead />
        {isLoginShowing && < LoginContainer /> }
		< Footer />
    </div>
}