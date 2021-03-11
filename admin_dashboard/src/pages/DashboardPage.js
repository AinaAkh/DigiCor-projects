import Sidebar from '../Sidebar';

function Dashboard() {
  return (
    <div className="App" id="outer-container">
      <Sidebar pageWrapId={'page-wrap'} outerContainerId={'outer-container'} />
      <div id="page-wrap">
        <h1>Admin Dashboard</h1>
      </div>
    </div>
  );
}

export default Dashboard;