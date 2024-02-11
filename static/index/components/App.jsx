
import { Footer } from "./Footer";
import { Header } from "./Header";
import { ActiveContainerTabProvider } from "../contexts/ActiveContainerTabContext";
import Container from "./Container";
import { useContext, useEffect } from "react";
import { AccountContext } from "../../general/AccountContext";
import { ajax } from "jquery";

// Performance check to see how many times this page has been fully rerendered
let count = 0

export default function App() {
    count++
    console.log("Rerender Count: " + count)

    const {state, dispatch} = useContext(AccountContext)

    useEffect(() => {
        ajax(
            location.origin + "/api/security/csrf", 
        ).done(function(data) {
            console.log(data)
        }).fail(function(error) {
            console.log(error)
        })
    }, [])

    return <ActiveContainerTabProvider>
        <Header />

        <Container />

        <Footer />
    </ActiveContainerTabProvider>
}