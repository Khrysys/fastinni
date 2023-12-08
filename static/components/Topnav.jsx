import { useState } from "react";
import { FaBars } from "react-icons/fa6";

export function Topnav() {
    const [isResponsive, setIsResponsive] = useState(false);

    return <>
        <a className="icon" onClick={() => setIsResponsive(!isResponsive)}>
            < FaBars />
        </a>
    </>
}