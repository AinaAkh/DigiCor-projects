import axios from 'axios';

const request = async function (options) {
    try {
        const { data, params, method = "GET", url } = options;
        const headers = {
        "Content-Type": "application/json",
        };
        const response = await axios({
        method,
        url,
        data,
        headers,
        params,
        });
        const parsedData = JSON.parse(response.data);
        console.log("response", parsedData);
        return parsedData;
    } catch (error) {
        //console.log("error", error.toJson());
        return error.response || null;
    }
};

export default request;
