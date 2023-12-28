import { createContext, useEffect, useState } from "react";

export const ActiveContainerTab = createContext();
export const ActiveContainerTabDispatch = createContext();

export const ContainerTabs = {
    Blog: "blog",
    Profile: "profile",
    Contact: "contact",
    Friends: "friends",
    Login: "login"
}

export function ActiveContainerTabProvider(props) {
    const [activeTab, setActiveTab] = useState(ContainerTabs.Blog);

    useEffect(()=> {
        var hash = window.location.hash;
        switch(hash) {
            case "#blog":
                setTab(ContainerTabs.Blog)
                break
            case "#profile":
                setTab(ContainerTabs.Profile)
                break
            case "#contact":
                setTab(ContainerTabs.Contact)
                break
            case "#friends":
                setTab(ContainerTabs.Friends)
                break
            case "#login":
                setTab(ContainerTabs.Login)
                break
            case _:
                setTab(ContainerTabs.Blog)
        }
    }, [])

    function setTab(val) {
        window.location.hash = val
        console.log(val)
        setActiveTab(val)
    }

    return <ActiveContainerTab.Provider value={activeTab}>
        <ActiveContainerTabDispatch.Provider value={setTab}>
            {props.children}
        </ActiveContainerTabDispatch.Provider>
    </ActiveContainerTab.Provider>
}