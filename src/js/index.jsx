import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./css/styles.css";

const favicon = document.createElement("favicon");

const rootElement = document.createElement("div");
document.body.appendChild(rootElement);

import App from "./App";

const root = createRoot(rootElement);
root.render(
	<StrictMode>
		<App />
	</StrictMode>
);