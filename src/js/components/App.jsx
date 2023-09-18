import { ajax } from "jquery"
import { useContext, useEffect, useState } from 'react'

import { Header } from './Header'
import { Loading } from "./Loading"
import { Masthead } from "./Masthead"
import { Footer } from "./Footer"
import { ThemeProvider } from "../contexts/ThemeContext"

import "../css/loading.css"
import { Container } from "./Container"
import { ErrorContext, ErrorDispachContext } from "../contexts/ErrorContext"
import { AccountProvider } from "../contexts/AccountContext"

export default function App() {
	const error = useContext(ErrorContext)
	const setError = useContext(ErrorDispachContext)
	const [ isLoaded, setIsLoaded ] = useState(false)
	const [ serverBuild, setServerBuild ] = useState("")

	useEffect(() =>{
		ajax(process.env.NPM_API_URL).done(function(data) {
			setIsLoaded(true)
			setServerBuild(data[Object.keys(data)[0]])
		}).fail(function() {
			setError(process.env.NPM_API_URL + " failed")
		})
	})

	if(!isLoaded) {
		return <div className="loading">
			<p className="error">{error}</p>
			< Loading />
		</div>
	}

	return < ThemeProvider >
		<AccountProvider >
			< Container />
		</AccountProvider>
	</ ThemeProvider >
}