import { createContext, useCallback, useState } from "react";

export const ThemeContext = createContext(null);
export const ThemeDispachContext = createContext(null);

export function ThemeProvider(props) {
    const [ theme, setTheme ] = useState("dark")

    return <ThemeContext.Provider value={theme}>
        <ThemeDispachContext.Provider value={setTheme}>
            {props.children}
        </ThemeDispachContext.Provider>
    </ThemeContext.Provider>
}