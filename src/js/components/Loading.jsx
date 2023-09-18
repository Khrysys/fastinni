import { ImageContainer } from "./blocks/ImageContainer";

export function Loading() {
	return <ImageContainer image={require("../img/loading.gif")} alt={"Loading GIF"} />;
}