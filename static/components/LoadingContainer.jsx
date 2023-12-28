import "../css/loading.css";

export default function LoadingContainer() {
    return <div className="loading">
        <img src={require("../img/loading.gif")} alt={"Loading GIF"} />
    </div>
}