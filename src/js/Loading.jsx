import { ImageContainer } from "./ImageContainer";

export function Loading() {
	return <ImageContainer image={require("./img/loading.gif")} alt={"Loading GIF"} />;
}