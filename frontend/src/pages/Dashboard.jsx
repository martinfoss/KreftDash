
import React from 'react';
import FilterPanel from '../components/FilterPanel';
import ChartView from '../components/ChartView';
import DataTable from '../components/DataTable';

function Dashboard() {
  return (
    <div className="dashboard">
      <FilterPanel />
      <ChartView />
      <DataTable />
    </div>
  );
}

export default Dashboard;
