import { createContext, useState } from "react";

export const ActiveSettingsTab = createContext();

export const SettingsTabs = {
    Theme: Symbol("theme"),
    General: Symbol("general"),
}

export function ActiveSettingsTabProvider(props) {
    const [tab, setTab] = useState(SettingsTabs.General);

    return <ActiveSettingsTab.Provider value={tab}>
        {props.children}
    </ActiveSettingsTab.Provider>
}