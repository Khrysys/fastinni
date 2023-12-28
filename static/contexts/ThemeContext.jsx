import { createContext, useState } from "react";

export const ThemeContext = createContext()
export const ThemeDispachContext = createContext()

export function ThemeProvider(props) {
    const [ theme, setTheme ] = useState("theme-dark")

    return <div className={theme}>
        <ThemeContext.Provider value={theme}>
            <ThemeDispachContext.Provider value={setTheme}>
                {props.children}
            </ThemeDispachContext.Provider>
        </ThemeContext.Provider>
    </div>
}