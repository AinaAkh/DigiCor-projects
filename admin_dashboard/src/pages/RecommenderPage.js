import Sidebar from '../Sidebar';
import { React, useState } from 'react';
import './RecomenderPage.css';
import { 
    Button,
    FormControl,
    InputGroup
 } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

function Recomender() {
    // React hooks 
    const [input, setInput] = useState('');
    const [bomsid, setBomsid] = useState('');
    const [apiResponse, setApiResonse] = useState('');
    const [data, setdata] = useState('')
    const [popularData, setPopular] = useState('')
    
    // API Function
    function handleSubmit(e) {
        e.preventDefault();
        setBomsid(input);
        let host = process.env.REACT_APP_LOCAL_URL;
        let API_ROUTE_TEST = '/api/recomender/name/';
        let API_ROUTE_PROD = '/api/recomender/boms/';
        let API_URL = '/api/recomender/name/';

        if(process.env.NODE_ENV === 'development'){
            host = process.env.REACT_APP_TEST_URL;
            API_URL = API_ROUTE_TEST;
        } else if (process.env.NODE_ENV === 'production') {
            host = process.env.REACT_APP_PROD_URL;
            API_URL = API_ROUTE_PROD;
        } else {
            host = process.env.REACT_APP_LOCAL_URL;
            let API_URL = '/api/recomender/boms/';
        }

        console.log(host);

        const API_ROUTE = (`${host}${API_URL}${input}`)
        console.log(API_ROUTE);
        fetch(API_ROUTE, {
            method:"POST",
            cache: "no-cache",
            body:{bom_id: input}
            }).then(response => {
                return response.json()
            }).then(json => {
                console.log(json);
                // setApiResonse(json);
                const api_result = Object.keys(json).map((key) => [key, json[key]]);
                const data_array = api_result[0][1];
                const data = data_array[0];
                setdata(data);
            }
        )
    }

    function handlePopularsubmit (e) {
        e.preventDefault();
        let host = process.env.REACT_APP_LOCAL_URL;
        let API_ROUTE_TEST = '/api/recomender/simillar';

        // if(process.env.NODE_ENV === 'development'){
        //     host = process.env.REACT_APP_TEST_URL;
        // } else if (process.env.NODE_ENV === 'production') {
        //     host = process.env.REACT_APP_PROD_URL;
        // } else {
        //     host = process.env.REACT_APP_LOCAL_URL;
        // }

        const API_ROUTE = (`${host}${API_ROUTE_TEST}`);
        console.log(API_ROUTE);
      
        fetch(API_ROUTE).then(response => {
                return response.json();
            })
            .then(json => {
                console.log(json);
                // setApiResonse(json);
                const api_result = Object.keys(json).map((key) => [key, json[key]]);
                const data_array = api_result[0][1];
                const data = data_array[0];
                setPopular(data);
            }
        )
    }
    
    // API response reformating
    const boms = Object.keys(data).map(function(d){
        return [d, data[d]];
    });

    const boms_simillar = Object.keys(popularData).map(function(d){
        return [d, popularData[d]];
    });

    // React render function
    return (
        <div className="App" id="outer-container">
            <Sidebar pageWrapId={'page-wrap'} outerContainerId={'outer-container'} />
            <div id="page-wrap">
                <grid>
                <h2>Enter Product Name:</h2>
                    <input type="text" onChange={(e) => setInput(e.target.value)}></input>
                    <Button type="submit" onClick={handleSubmit}>Enter</Button>

                {
                    data && 
                    <div>
                        <h2>Simillar Products</h2>
                        <table>
                            <thead>
                                <tr>
                                    <th>boms_id</th>
                                    <th>name</th>
                                </tr>
                            </thead>
                            <tbody>
                                {boms.map(bom => 
                                    <tr>
                                        <td>{bom[0]}</td>
                                        <td>{bom[1]}</td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                }
                </grid>
                <br></br><br></br>
                <Button type='submit' onClick={handlePopularsubmit}>check popular products</Button>
                {
                    popularData && 
                    <div>
                        <h2>Popular Products</h2>
                        <table>
                            <thead>
                                <tr>
                                    <th>boms_id</th>
                                    <th>name</th>
                                </tr>
                            </thead>
                            <tbody>
                                {boms_simillar.map(bom => 
                                    <tr>
                                        <td>{bom[0]}</td>
                                        <td>{bom[1]}</td>
                                    </tr>
                                )}
                            </tbody>
                        </table>
                    </div>
                }
                
            </div>
        </div>
        );
    }

export default Recomender;