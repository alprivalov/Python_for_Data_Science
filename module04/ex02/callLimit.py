def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if count <= limit:
                function()
            else:
                print("Error:",function,"call too many times")
        return limit_function
    return callLimiter