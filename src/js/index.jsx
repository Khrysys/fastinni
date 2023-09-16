import { createRoot } from "react-dom/client";
import { Provider } from "react-redux";
import "./css/styles.css";
import App from "./components/App";
import { Store } from "./Store";

const rootElement = document.createElement("div");
document.body.appendChild(rootElement);


const root = createRoot(rootElement);
root.render(
	< Provider store={Store}>
		< App />
	</ Provider>
);