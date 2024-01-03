import { createContext, useReducer, useState } from "react";
import { ajax } from "jquery";

export const AccountContext = createContext({})
export const isSigningUp = createContext({})

export function SignupProvider(props) {
    const [isSignup, setIsSignup] = useState(false)

    return <isSigningUp.Provider value={{isSignup, setIsSignup}}>
        {props.children}
    </isSigningUp.Provider>
}

function reducer(state, action) {
    switch(action.type) {
        case "have_google_code":
            ajax(
                location.origin + '/api/latest/oauth/google/finalize',
                {
                    data: {
                        code: new URL(location.href).searchParams.get('google_code')
                    }
                }
            ).done(function(response) {
                console.log(response)
                return {
                    ...state,
                    isLoggedIn: false
                }
            })
    }
}

export function AccountProvider(props) {
    const [state, dispatch] = useReducer(reducer, {
        isLoggedIn: false, 
        id: 0, 
        public_profile: false,
        tag: "",
        phone: "",
        public_phone: false,
        email: "",
        public_email: false,
        address: "",
        public_address: false,
        profile_image: "",
        theme: 'theme-dark'
    })

    return <AccountContext.Provider value={{state, dispatch}}>
        {props.children}
    </AccountContext.Provider>
}