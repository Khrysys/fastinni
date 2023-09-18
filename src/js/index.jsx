import "./css/fonts.css";
import { createRoot } from "react-dom/client";
import "./css/main.css";
import App from "./components/App";
import { StrictMode } from "react";
import { ErrorProvider } from "./contexts/ErrorContext";

const rootElement = document.createElement("div");
document.body.appendChild(rootElement);


const root = createRoot(rootElement);
root.render(
	< StrictMode >
		< ErrorProvider>
			< App />
		</ErrorProvider>
	</ StrictMode >
);