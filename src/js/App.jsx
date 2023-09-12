import { ajax } from "jquery";
import { useState, Component} from 'react';

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

	componentDidMount() {
		ajax( "get-data" )
		.done(function() {
			alert( "success" );
			this.state = {
				loading: false
			}
		})
		.fail(function() {
			alert( "error" );
		})
		.always(function() {
			alert( "complete" );
		});
	}

	render() {
		if(this.state['loading']) {
			return <Loading />
		}
		return <>
			<Masthead />
			<Footer />
		</>
	}
}