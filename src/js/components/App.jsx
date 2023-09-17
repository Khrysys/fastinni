import { ajax } from "jquery";
import { Component} from 'react';

import { Header } from "./Header";
import { Loading } from "./Loading";
import { Masthead } from "./Masthead";
import { Footer } from "./Footer";

export default class App extends Component {

	constructor(props) {
		super(props);
		this.state = {
			loading: true,
			server_build: "",
			mode: 'light'
		};
	}

	componentDidMount() {
		console.log(this.state)
		ajax( "../api/latest" ).done(function(data) {
			//alert( ".done() ran" );
			this.setState({loading: false, server_build: data[Object.keys(data)[0]]})
		}.bind(this)).fail(function() {
			alert( ".fail() ran" );
		}).always(function() {
			//alert(".always() ran");
		});
		
	}

	toggleMode() {
		this.setState({mode: this.state.mode == "light" ? "dark" : "light"})
	}

	render() {
		if(this.state.loading) {
			return < Loading />
		}

		return <div className={this.state.mode + '-mode'}>
			< Header isLight={this.state.mode == "light" ? true : false} changeMode={() => this.toggleMode().bind(this)}/>
			< Masthead />

			< Footer />
		</div>
	}
}