# url_shortner_api

1. Run api_project
2. Request to url localhost:8000/api/create
3. Request data must be json data like this { "link": "https://somelink.com" }
4. Responce will be json like this { "link: "https://somelink.com", "uuid": "u12uu" }
5. ShortUrl is "localhost:8000/[uuid]"  (for this examle it is "localhost:8000/u12uu")
