import React from 'react';
// import { slide as Menu } from 'react-burger-menu';
// import { bubble as Menu } from 'react-burger-menu';
import { elastic as Menu } from 'react-burger-menu';
import './Sidebar.css';

import { Link } from "react-router-dom";

export default props => {
  return (
    <div>
    <Menu>
      <h1>DiGiCOR Admin</h1>
      <Link to="/Dashboard">
        Home
      </Link>
      <Link to="/Crawler">
        Crawler
      </Link>
      <Link to="/Recommender">
        Recommender
      </Link>
    </Menu>
    </div>
  );
};