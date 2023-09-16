export function ImageContainer({image}, {alt}) {
	return <img src={require(image)} alt={alt} />;
}