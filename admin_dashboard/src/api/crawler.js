import request from "./BaseApi";

// const currentServiceUrl = process.env.REACT_APP_TEST_URL_CRAWLER;
const currentServiceUrl = process.env.REACT_APP_LOCAL_URL_CRAWLER;

function startCrawler() {
  console.log({ currentServiceUrl });
  return request({
    url: `${currentServiceUrl}/api/crawler`,
    method: "get",
    data: null,
  });
}

const downloadSpecification = `${currentServiceUrl}/api/download`;

const CrawlerService = {
  startCrawler,
  downloadSpecification,
};

export default CrawlerService;
