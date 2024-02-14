export const ActiveSidebarTab = createContext();

export const SidebarTabTypes = {
    Dashboard: "dashboard",
    UserCounts: "usercounts",
    Database: "database"
}

export function ActiveSidebarTabProvider(props) {
    const [activeTab, setActiveTab] = useState(SidebarTabTypes.Dashboard);

    useEffect(() => {
        var hash = window.location.hash;
        switch(hash) {
            case "#dashboard":
                setTab(SidebarTabTypes.Dashboard)
                break
            case "#usercounts":
                setTab(SidebarTabTypes.UserCounts)
                break
            case "#database":
                setTab(SidebarTabTypes.Database)
                break
            default:
                setTab(SidebarTabTypes.Dashboard)
        }
    }, [])

    function setTab(val) {
        window.location.hash = val
        setActiveTab(val)
    }

    return <ActiveSidebarTab.Provider value={{activeTab, setTab }}>
        {props.children}
    </ActiveSidebarTab.Provider>
}