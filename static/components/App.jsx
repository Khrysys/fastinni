import { AccountProvider } from "../contexts/AccountContext";
import { ThemeProvider } from "../contexts/ThemeContext";
import { Footer } from "./Footer";
import { Header } from "./Header";
import { ActiveContainerTabProvider } from "../contexts/ActiveContainerTabContext";
import Container from "./Container";

// Performance check to see how many times this page has been fully rerendered
let count = 0;

export default function App() {
    count++;
    console.log("Rerender Count: " + count);

    return <ThemeProvider>
        <AccountProvider>
            <ActiveContainerTabProvider>
                <Header />

                <Container />

                <Footer />
            </ActiveContainerTabProvider>
        </AccountProvider>
    </ThemeProvider>
}