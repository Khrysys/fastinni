import { createContext, useState } from "react";

export const ActiveSettingsTab = createContext();
export const ActiveSettingsTabDispatch = createContext();

export const SettingsTabs = {
    Theme: Symbol("theme"),
    General: Symbol("general"),
}

export function ActiveSettingsTabProvider(props) {
    const [tab, setTab] = useState(SettingsTabs.General);

    return <ActiveSettingsTab.Provider value={tab}>
        <ActiveSettingsTabDispatch.Provider value={setTab}>
            {props.children}
        </ActiveSettingsTabDispatch.Provider>
    </ActiveSettingsTab.Provider>
}