export function Header() {
    return <div className={classes}>
        <a onClick={() => setTab(ContainerTabTypes.Blog)}>Blog</a>
        <a onClick={() => setTab(ContainerTabTypes.Contact)}>Contact</a>

        <a className="icon" onClick={() => setIsResponsive(!isResponsive)}>
            < FaBars />
        </a>
    </div>
}