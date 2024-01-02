import { useContext, lazy, Suspense } from "react";
import { ActiveContainerTab, ContainerTabTypes } from "../contexts/ActiveContainerTabContext";
import { LoadingContainer } from "./LoadingContainer";

const BlogContainer = lazy(() => import('./BlogContainer'));
const ContactContainer = lazy(() => import('./ContactContainer'));
const FriendsContainer = lazy(() => import('./FriendsContainer'));
const LoginContainer = lazy(() => import('./LoginContainer'));
const ProfileContainer = lazy(() => import('./ProfileContainer'));

export default function Container() {
    const {activeTab, setTab} = useContext(ActiveContainerTab);
    
    if(activeTab == ContainerTabTypes.Blog) {
        console.log("Rendering Blog")
        return <Suspense fallback={<LoadingContainer />}>
            <BlogContainer/>
        </Suspense>
    } else if(activeTab == ContainerTabTypes.Contact) {
        console.log("Rendering Contact")
        return <Suspense fallback={<LoadingContainer/>}>
            <ContactContainer />
        </Suspense>
    } else if(activeTab == ContainerTabTypes.Friends) {
        console.log("Rendering Friends")
        return <Suspense fallback={<LoadingContainer/>}>
            <FriendsContainer />
        </Suspense>
    } else if(activeTab == ContainerTabTypes.Login) {
        console.log("Rendering Login")
        return <Suspense fallback={<LoadingContainer/>}>
            <LoginContainer />
        </Suspense>
    } else if(activeTab == ContainerTabTypes.Profile) {
        console.log("Rendering Profile")
        return <Suspense fallback={<LoadingContainer/>}>
            <ProfileContainer />
        </Suspense>
    } else {
        console.log("Rendering Loading")
        return <LoadingContainer/>
    }
}