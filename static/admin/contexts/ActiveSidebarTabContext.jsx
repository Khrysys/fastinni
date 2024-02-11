export const ActiveSidebarTab = createContext();

export const SidebarTabTypes = {
    Admin: "admin"
}

export function ActiveSidebarTabProvider(props) {
    const [activeTab, setActiveTab] = useState(SidebarTabTypes.Blog);

    useEffect(() => {
        var hash = window.location.hash;
        switch(hash) {
            case "#blog":
                setTab(SidebarTabTypes.Blog)
                break
            case "#profile":
                setTab(SidebarTabTypes.Profile)
                break
            case "#contact":
                setTab(SidebarTabTypes.Contact)
                break
            case "#friends":
                setTab(SidebarTabTypes.Friends)
                break
            case "#login":
                setTab(SidebarTabTypes.Login)
                break
            default:
                setTab(SidebarTabTypes.Blog)
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