def http_status(status):
    match status:
        case 200:
            return "ok"
        case 403:
            return "not found"
        case 500:
            return"internal server error"
        case _:
            return"unknown status"#usage print (http_status #output: ok print(http_status
            
            
print(http_status(500))

print(http_status(403))

print(http_status(200))

print(http_status(4))