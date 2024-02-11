
// Performance check to see how many times this page has been fully rerendered
let count = 0

export default function App() {
    count++
    console.log("Rerender Count: " + count)
    
    return <>
        
    </>
}