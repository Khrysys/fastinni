import { ajax } from "jquery"
import { useContext, useEffect, useState } from 'react'
import { ErrorContext, ErrorDispachContext } from "../contexts/ErrorContext"
import { ThemeProvider } from "../contexts/ThemeContext"
import "../css/loading.css"
import { Container } from "./Container"
import { Loading } from "./Loading"

export default function App() {
	const error = useContext(ErrorContext)
	const setError = useContext(ErrorDispachContext)
	const [ isLoaded, setIsLoaded ] = useState(false)
	const [ serverBuild, setServerBuild ] = useState("")

	useEffect(() => {
		ajax(process.env.NPM_API_URL + 'csrf/').done(function() { 
			setIsLoaded(true)
		})
	})
	

	if(!isLoaded) {
		return <div className="loading">
			{error != "" && <p className="error">{error}</p>}
			< Loading />
		</div>
	}

	return < ThemeProvider >
		{error != "" && <p className="error">{error}</p>}
		<Container/>
	</ ThemeProvider >
}