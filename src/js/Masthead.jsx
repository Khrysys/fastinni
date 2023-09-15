import "./css/masthead.css"

import { ImageContainer } from "./ImageContainer";

export function Masthead() {
	return <div class="masthead">
		<ImageContainer image={require("./img/loading.gif")} alt={"Masthead Image"} />
	</div>;
}