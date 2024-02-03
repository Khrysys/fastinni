import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { AccountProvider } from "./contexts/AccountContext";
import { ThemeProvider } from "./contexts/ThemeContext";
import App from "./components/App";
import "./scss/main.scss";


const rootElement = document.createElement("div");
rootElement.classList.add("root");
document.body.appendChild(rootElement);

const root = createRoot(rootElement);
root.render(
	< StrictMode >
		<ThemeProvider>
			<AccountProvider>
				<App />
			</AccountProvider>
		</ThemeProvider>
	</ StrictMode >
);