import { useContext, lazy, Suspense } from "react";
import { ActiveContainerTab, ContainerTabs } from "../contexts/ActiveContainerTabContext";
import LoadingContainer from "./LoadingContainer";

const ProfileContainer = lazy(() => import('./ProfileContainer'));
const LoginContainer = lazy(() => import('./LoginContainer'));
const FriendsContainer = lazy(() => import('./FriendsContainer'));
const ContactContainer = lazy(() => import('./ContactContainer'));
const BlogContainer = lazy(() => import('./BlogContainer'));

export default function Container() {
    const activeContainerTab = useContext(ActiveContainerTab);

    switch(activeContainerTab) {
        case ContainerTabs.Blog:
            return <Suspense fallback={<LoadingContainer />}>
                <BlogContainer/>
            </Suspense>
        case ContainerTabs.Contact:
            return <Suspense fallback={<LoadingContainer/>}>
                <ContactContainer />
            </Suspense>
        case ContainerTabs.Friends:
            return <Suspense fallback={<LoadingContainer/>}>
                <FriendsContainer />
            </Suspense>
        case ContainerTabs.Login:
            return <Suspense fallback={<LoadingContainer/>}>
                <LoginContainer />
            </Suspense>
        case ContainerTabs.Profile:
            return <Suspense fallback={<LoadingContainer/>}>
                <ProfileContainer />
            </Suspense>
    }
}