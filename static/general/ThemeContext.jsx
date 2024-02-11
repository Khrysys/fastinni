import { createContext, useState } from "react";

export const ThemeContext = createContext()

export function ThemeProvider(props) {
    const [ theme, setTheme ] = useState("theme-dark")

    return <div className={theme}>
        <ThemeContext.Provider value={{theme, setTheme}}>
            {props.children}
        </ThemeContext.Provider>
    </div>
}