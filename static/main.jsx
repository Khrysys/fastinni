import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

const rootElement = document.createElement("div");
document.body.appendChild(rootElement);

const root = createRoot(rootElement);

root.render(
    < StrictMode >
        < App/>
    </StrictMode>
);