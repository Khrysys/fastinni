import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./components/App";
import { AccountProvider } from "./contexts/AccountContext";
import { ErrorProvider } from "./contexts/ErrorContext";
import "./css/main.css";

const rootElement = document.createElement("div");
document.body.appendChild(rootElement);


const root = createRoot(rootElement);
root.render(
	< StrictMode >
		< ErrorProvider>
			<AccountProvider >
				< App />
			</AccountProvider>
		</ErrorProvider>
	</ StrictMode >
);