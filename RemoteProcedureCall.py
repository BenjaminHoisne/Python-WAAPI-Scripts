from waapi import WaapiClient

#Connect to WAAPI
with WaapiClient() as client:
    print("Connected to WAAPI server")

    query = {
            "from": { "ofType": ["Event"] },
            "options": { "return": ["name", "id", "path"] }
        }
    
    result = client.call("ak.wwise.core.object.get", query)

    for item in result["return"]: 
        client.call("ak.wwise.core.object.setProperty",
                    {
                        "object": item["id"],
                        "property": "Inclusion",
                        "value": "false"})
        print(item["name"], item["path"])



