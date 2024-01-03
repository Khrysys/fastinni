
import { Footer } from "./Footer";
import { Header } from "./Header";
import { ActiveContainerTabProvider } from "../contexts/ActiveContainerTabContext";
import Container from "./Container";
import { useContext, useEffect } from "react";
import { AccountContext } from "../contexts/AccountContext";

// Performance check to see how many times this page has been fully rerendered
let count = 0

export default function App() {
    count++
    console.log("Rerender Count: " + count)

    const {state, dispatch} = useContext(AccountContext)

    useEffect(() => {
        if(window.location.search !== "") {
            // We have a login code
            var code = new URL(location.href).searchParams.get('google_code')
            console.log(code)

            if(code != null) {
                dispatch({type: 'have_google_code'})
            }
        }
    }, [])
    // If we don't, proceed as if normal

    return <ActiveContainerTabProvider>
        <Header />

        <Container />

        <Footer />
    </ActiveContainerTabProvider>
}