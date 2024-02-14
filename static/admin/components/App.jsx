import { ActiveSidebarTabProvider } from "../contexts/ActiveSidebarTabContext"
import { Header } from "./Header"
import Sidebar from "./Sidebar"

// Performance check to see how many times this page has been fully rerendered
let count = 0

export default function App() {
    count++
    console.log("Rerender Count: " + count)
    
    return <ActiveSidebarTabProvider>
        <Header/>
        <Sidebar/>
        <Container/>
    </ActiveSidebarTabProvider>
}