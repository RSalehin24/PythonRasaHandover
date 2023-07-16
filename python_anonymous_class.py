class ProgressReportSuccess():
    def __init__(self, site, *args, **kwargs):
        self.site = site
        
    def get_response_scraper(self):
        pass

    def as_response(self):
        return {
            "status_code": "200",
            "site": self.site,
            "data": self.get_response_scraper()
        }


type(
    "ScraperSuccess",  # the name
    (ProgressReportSuccess,),  # base classess
    {  # the body
        "get_response_scraper": lambda self: "helloworld"
    }
).as_response()
