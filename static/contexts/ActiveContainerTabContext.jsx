import { createContext, useEffect, useState } from "react";

export const ActiveContainerTab = createContext({activeTab: "", setTab: function() {}});

export const ContainerTabTypes = {
    Blog: "blog",
    Contact: "contact",
    Friends: "friends",
    Login: "login",
    Profile: "profile",
}

export function ActiveContainerTabProvider(props) {
    const [activeTab, setActiveTab] = useState(ContainerTabTypes.Blog);

    useEffect(() => {
        var hash = window.location.hash;
        switch(hash) {
            case "#blog":
                setTab(ContainerTabTypes.Blog)
                break
            case "#profile":
                setTab(ContainerTabTypes.Profile)
                break
            case "#contact":
                setTab(ContainerTabTypes.Contact)
                break
            case "#friends":
                setTab(ContainerTabTypes.Friends)
                break
            case "#login":
                setTab(ContainerTabTypes.Login)
                break
            default:
                setTab(ContainerTabTypes.Blog)
        }
    }, [])

    function setTab(val) {
        window.location.hash = val
        setActiveTab(val)
    }

    return <ActiveContainerTab.Provider value={{activeTab, setTab }}>
        {props.children}
    </ActiveContainerTab.Provider>
}