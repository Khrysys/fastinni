import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./components/App";
import "./scss/main.scss";

const rootElement = document.createElement("div");
rootElement.classList.add("root");
document.body.appendChild(rootElement);

const root = createRoot(rootElement);
root.render(
	< StrictMode >
		<App />
	</ StrictMode >
);