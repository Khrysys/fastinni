import { useContext, useState } from "react"
import { BlogPostsShowingContext, ContactFormShowingContext, LoginShowingContext } from "../contexts/HeaderContext"
import { ThemeContext } from "../contexts/ThemeContext"
import { Footer } from "./Footer"
import { Header } from "./Header"
import { Masthead } from "./Masthead"
import { BlogContainer } from "./blog/BlogContainer"
import { ContactContainer } from "./contact/ContactContainer"
import { LoginContainer } from "./account/LoginContainer"

export function Container() {
    const theme = useContext(ThemeContext)
    const [isLoginShowing, setIsLoginShowing] = useState(false);
    const [isContactShowing, setIsContactShowing] = useState(false);
    const [isBlogShowing, setIsBlogShowing] = useState(true);

    function toggleLoginShowing() {
        setIsLoginShowing(!isLoginShowing);
        setIsContactShowing(false);
        setIsBlogShowing(false);
    }

    function toggleContactShowing() {
        setIsLoginShowing(false);
        setIsContactShowing(!isContactShowing);
        setIsBlogShowing(false);
    }

    function toggleBlogShowing() {
        setIsLoginShowing(false);
        setIsContactShowing(false);
        setIsBlogShowing(!isBlogShowing);
    }

    return <div className={theme + "-mode"}>
        <LoginShowingContext.Provider value={toggleLoginShowing}>
            <ContactFormShowingContext.Provider value={toggleContactShowing}>
                <BlogPostsShowingContext.Provider value={toggleBlogShowing}>
		            < Header />
                </BlogPostsShowingContext.Provider>
            </ContactFormShowingContext.Provider>
        </LoginShowingContext.Provider>
		< Masthead />
        {isLoginShowing && < LoginContainer /> }
        {isContactShowing && < ContactContainer />}
        {isBlogShowing && < BlogContainer />}
		< Footer />
    </div>
}