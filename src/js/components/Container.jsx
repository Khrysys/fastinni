import { ajax } from "jquery"
import { useContext, useEffect, useState } from "react"
import { BlogPostsShowingContext, ContactFormShowingContext, LoginShowingContext, ProfileShowingContext } from "../contexts/HeaderContext"
import { ThemeContext } from "../contexts/ThemeContext"
import { Footer } from "./Footer"
import { Header } from "./Header"
import { Masthead } from "./Masthead"
import { LoginContainer } from "./account/LoginContainer"
import { ProfileContainer } from "./account/ProfileContainer"
import { BlogContainer } from "./blog/BlogContainer"
import { ContactContainer } from "./contact/ContactContainer"
import { ImageDispatchContext, LoginDispatchContext } from "../contexts/AccountContext"

export function Container() {
    const theme = useContext(ThemeContext)
    const [isLoginShowing, setIsLoginShowing] = useState(false);
    const [isContactShowing, setIsContactShowing] = useState(false);
    const [isBlogShowing, setIsBlogShowing] = useState(true);
    const [isProfileShowing, setIsProfileShowing] = useState(false);
	const setLogin = useContext(LoginDispatchContext)
    const setImage = useContext(ImageDispatchContext)

    function toggleLoginShowing() {
        setIsLoginShowing(!isLoginShowing);
        setIsContactShowing(false);
        setIsBlogShowing(false);
        setIsProfileShowing(false);
    }

    function toggleContactShowing() {
        setIsLoginShowing(false);
        setIsContactShowing(!isContactShowing);
        setIsBlogShowing(false);
        setIsProfileShowing(false);
    }

    function toggleBlogShowing() {
        setIsLoginShowing(false);
        setIsContactShowing(false);
        setIsBlogShowing(!isBlogShowing);
        setIsProfileShowing(false);
    }

    function toggleProfileShowing() {
        setIsLoginShowing(false);
        setIsContactShowing(false);
        setIsBlogShowing(false);
        setIsProfileShowing(!isProfileShowing);
    }

    useEffect(() => {
        ajax(process.env.NPM_API_URL + 'account/get-data').done(function(data) {
            setLogin(true)
            setImage(data.image)
        }).fail(function() {
            setLogin(false)
        })
    }, [])

    return <div className={theme + "-mode"}>
        <LoginShowingContext.Provider value={toggleLoginShowing}>
            <ContactFormShowingContext.Provider value={toggleContactShowing}>
                <BlogPostsShowingContext.Provider value={toggleBlogShowing}>
                    <ProfileShowingContext.Provider value={toggleProfileShowing}>
		                < Header />
                    </ProfileShowingContext.Provider>
                </BlogPostsShowingContext.Provider>
            </ContactFormShowingContext.Provider>
        </LoginShowingContext.Provider>
		< Masthead />
        {isLoginShowing && < LoginContainer /> }
        {isContactShowing && < ContactContainer />}
        {isBlogShowing && < BlogContainer />}
        {isProfileShowing && < ProfileContainer />}
		< Footer />
    </div>
}