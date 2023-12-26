import { createContext, useState } from "react";

export const ErrorContext = createContext()
export const ErrorDispachContext = createContext()

export function ErrorProvider(props) {
    const [error, setError] = useState("")

    return <ErrorContext.Provider value={error}>
        <ErrorDispachContext.Provider value={setError}>
            {props.children}
        </ErrorDispachContext.Provider>
    </ErrorContext.Provider>
}