import './App.css';
import Sidebar from './Sidebar';
import Dashboard from './pages/DashboardPage';
import Crawler from './pages/CrawlerPage';
import Recommender from './pages/RecommenderPage';
import {React} from 'react';
import { Switch, Route } from "react-router-dom";

function App() {

  return (
      <div className="App" id="outer-container">
          <Sidebar pageWrapId={'page-wrap'} outerContainerId={'outer-container'} />
          <div id="page-wrap">
            <Switch>
              <Route path="/Dashboard">
                <Dashboard/>
              </Route>
              <Route path="/Crawler">
                <Crawler/>
              </Route>
              <Route path="/Filters">
              </Route>
              <Route path="/Recommender">
                <Recommender/>
              </Route>
            </Switch>
        </div>
      </div>
  );
}

export default App;