import { ajax } from "jquery";
import { useState, Component} from 'react';

import { Header } from "./Header";
import { Loading } from "./Loading";
import { Masthead } from "./Masthead";
import { Footer } from "./Footer";

export default class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			loading: true
		};
	}

	/*
	componentDidMount() {
		ajax( "api/data" ).done(function() {
			alert( ".done() ran" );
			this.state = {
				loading: false
			}
		}).fail(function() {
			alert( ".fail() ran" );
		}).always(function() {
			alert(".always() ran");
		});
	}
	*/

	render() {
		/*
		if(this.state['loading']) {
			return <Loading />
		}
		*/
		return <>
			<Header />
			<Masthead />
			<Footer />
		</>
	}
}