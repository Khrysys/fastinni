import { createContext, useState } from "react";

export const isLoggedInContext = createContext({})
export const isSigningUp = createContext({})

export function SignupProvider(props) {
    const [isSignup, setIsSignup] = useState(false)

    return <isSigningUp.Provider value={{isSignup, setIsSignup}}>
        {props.children}
    </isSigningUp.Provider>
}

export function AccountProvider(props) {
    const [isLogin, isLoginDispatch] = useState(false);

    return <isLoggedInContext.Provider value={{isLogin, isLoginDispatch}}>
        {props.children}
    </isLoggedInContext.Provider>
}