import { ajax } from "jquery";
import { setState, Component} from 'react';

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

	componentDidMount() {
		ajax( "../api/latest" ).done(function() {
			//alert( ".done() ran" );
			this.setState({'loading': false})
		}.bind(this)).fail(function() {
			alert( ".fail() ran" );
		}).always(function() {
			//alert(".always() ran");
		});
		
	}

	render() {
		if(this.state.loading) {
			return <>
				< Header />
				< Loading />
				< Footer />
			</>
		}

		return <>
			< Header />
			< Masthead />
			< Footer />
		</>
	}
}