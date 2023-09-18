import { createContext, useState } from "react";

export const UsernameContext = createContext();
export const UsernameDispatchContext = createContext();

function LoginProvider(props) {
    const [login, setLogin] = useState();

    return <UsernameContext.Provider value={login}>
        <UsernameDispatchContext.Provider value={setLogin}>
            {props.children}
        </UsernameDispatchContext.Provider>
    </UsernameContext.Provider>
}

export function AccountProvider(props) {
    return <LoginProvider>
        {props.children}
    </LoginProvider>
}