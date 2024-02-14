import { lazy, useContext, Suspense } from 'react';
import { ActiveSidebarTab } from '../contexts/ActiveSidebarTabContext';

const DashboardContainer = lazy(() => import('./DashboardContainer'));

export function Container() {
    const {activeTab, setTab} = useContext(ActiveSidebarTab);
}