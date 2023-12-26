import { ajax } from "jquery";
import { createContext, useEffect, useState } from "react";

export const UsernameContext = createContext();
export const UsernameDispatchContext = createContext();
export const TagContext = createContext();
export const TagDispatchContext = createContext();
export const EmailContext = createContext();
export const EmailDispatchContext = createContext();
export const ImageContext = createContext();
export const ImageDispatchContext = createContext();
export const LoginContext = createContext();
export const LoginDispatchContext = createContext();

function UsernameProvider(props) {
    const [username, setUsername] = useState();

    return <UsernameContext.Provider value={username}>
        <UsernameDispatchContext.Provider value={setUsername}>
            {props.children}
        </UsernameDispatchContext.Provider>
    </UsernameContext.Provider>
}

function TagProvider(props) {
    const [tag, setTag] = useState();
    return <TagContext.Provider value={tag}>
        <TagDispatchContext.Provider value={setTag}>
            {props.children}
        </TagDispatchContext.Provider>
    </TagContext.Provider>
}

function EmailProvider(props) {
    const [email, setEmail] = useState()

    return <EmailContext.Provider value={email}>
        <EmailDispatchContext.Provider value={setEmail}>
            {props.children}
        </EmailDispatchContext.Provider>
    </EmailContext.Provider>
}

function ImageProvider(props) {
    const [image, setImage] = useState()

    return <ImageContext.Provider value={image}>
        <ImageDispatchContext.Provider value={setImage}>
            {props.children}
        </ImageDispatchContext.Provider>
    </ImageContext.Provider>
}

function LoginProvider(props) {
    const [login, setLogin] = useState(false)

    return <LoginContext.Provider value={login}>
        <LoginDispatchContext.Provider value={setLogin}>
            {props.children}
        </LoginDispatchContext.Provider>
    </LoginContext.Provider>
}

export function AccountProvider(props) {
    return <LoginProvider>
        <UsernameProvider>
            <TagProvider>
                <EmailProvider>
                    <ImageProvider>
                        {props.children}
                    </ImageProvider>
                </EmailProvider>
            </TagProvider>
        </UsernameProvider>
    </LoginProvider>
}