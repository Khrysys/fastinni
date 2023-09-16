import "../css/masthead.css"

import { ImageContainer } from "./ImageContainer";

export function Masthead() {
	return <div class="masthead">
		<ImageContainer image={"./img/Flaskinni.png"} alt={"Masthead Image"} />
	</div>;
}