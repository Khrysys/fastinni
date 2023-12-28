import { createContext, useState } from "react";

export const isLoginContext = createContext()
export const isLoginDispatchContext = createContext()

export function AccountProvider(props) {
    const [isLogin, isLoginDispatch] = useState(false);

    return <isLoginContext.Provider value={isLogin}>
        <isLoginDispatchContext.Provider value={isLoginDispatch}>
            {props.children}
        </isLoginDispatchContext.Provider>
    </isLoginContext.Provider>
}