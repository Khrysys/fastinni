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
        return <Suspense fallback={<LoadingContainer />}>
            <BlogContainer/>
        </Suspense>
    } else if(activeTab == ContainerTabTypes.Contact) {
        return <Suspense fallback={<LoadingContainer/>}>
            <ContactContainer />
        </Suspense>
    } else if(activeTab == ContainerTabTypes.Friends) {
        return <Suspense fallback={<LoadingContainer/>}>
            <FriendsContainer />
        </Suspense>
    } else if(activeTab == ContainerTabTypes.Login) {
        return <Suspense fallback={<LoadingContainer/>}>
            <LoginContainer />
        </Suspense>
    } else if(activeTab == ContainerTabTypes.Profile) {
        return <Suspense fallback={<LoadingContainer/>}>
            <ProfileContainer />
        </Suspense>
    } else {
        return <LoadingContainer/>
    }
}