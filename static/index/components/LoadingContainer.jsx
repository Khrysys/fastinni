import "../../general/scss/loading.scss";

export function LoadingContainer() {
    return <div className="loading">
        <img src={require("../img/loading.gif")} alt={"Loading GIF"} />
    </div>
}