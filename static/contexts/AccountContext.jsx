import { createContext, useState } from "react";

export const isLoginContext = createContext()
export const isSignupForm = createContext()

export function isSignupProvider(props) {
    const [isSignup, setIsSignup] = useState(false)

    return <isSignupForm.Provider value={{isSignup, setIsSignup}}>
        {props.children}
    </isSignupForm.Provider>
}

export function AccountProvider(props) {
    const [isLogin, isLoginDispatch] = useState(false);

    return <isLoginContext.Provider value={{isLogin, isLoginDispatch}}>
        {props.children}
    </isLoginContext.Provider>
}