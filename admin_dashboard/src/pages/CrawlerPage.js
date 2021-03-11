import Sidebar from "../Sidebar";
import { React, useState } from "react";
import { Button } from "react-bootstrap";
// import 'bootstrap/dist/css/bootstrap.min.css';
import CrawlerService from "../api/crawler";
import fileDownload from "js-file-download";
import "../css/Dashboard.css";
import PaginationTableComponent from "../components/table";
import "bootstrap/dist/css/bootstrap.min.css";

function Crawler() {
 
  const [response, setResponse] = useState('');
  const [nullResponse, setNullResponse] = useState('');

    function startCrawler(){
        let URL = process.env.REACT_APP_LOCAL_URL_CRAWLER;

        if(process.env.NODE_ENV === 'development') {
            URL = process.env.REACT_APP_TEST_URL_CRAWLER;
        } else {
            URL = process.env.REACT_APP_LOCAL_URL_CRAWLER;
        }

        console.log(URL);
        fetch(`${URL}/api/crawler`).then((response) => 
            response.json()).then(data => 
                {
                    console.log('Data: ',data);
                    setResponse(data.data);
                    setNullResponse(data.null);
                }
            )
        };

  return (
    <div className="App" id="outer-container">
        <Sidebar pageWrapId={"page-wrap"} outerContainerId={"outer-container"} />
        <div id="page-wrap">
        <h1>Crawler</h1>

        {   !response && (
            <div>
                <Button variant="primary" onClick={startCrawler}>
                    Start Crawler
                </Button>
            </div> )
        }        

        {
            response && 
            <div>
                <a href={CrawlerService.downloadSpecification}>
                Download Specifications.xlsx
                </a>
                <br></br>
                {/* <ModalComponent 
                    name="Show null boms"
                    data={nullResponse || {}}/> */}
                
                <br></br>
                <PaginationTableComponent
                    data={response || {}}
                />
                <br></br>

                <form action="http://192.168.15.113:5001/api/upload" method="post" enctype="multipart/form-data">
                      <input type="file" name="file"/>
                      <input type="submit" value="Upload"/>
                </form>
            </div> 
        }
      </div>
    </div>
  );
}

export default Crawler;
