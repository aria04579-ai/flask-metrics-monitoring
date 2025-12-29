#!/bin/bash


BASE_URL = "http://localhost:5000"

REQUESTS=500
CONCURRENT=10

ENDPOINTS=(
    "/",
    "/delay",
    "/error"
)


echo "Starting ......"
echo "Base Url: $BASE_URL"
echo "Requests per endpoint: $REQUESTS"
echo "Copncurrent reqeusts: $CONCURRENT"



for endpoint in "{$ENDPOINTS[@]}"; do 
    echo "Testing $endpoint..."
    hey -n $REQUESTS -c $CONCURRENT $BASE_URL$endpoint
    wait 
    echo "Completed $endpoint"
done

echo "Check metrics at: http://localhost:9090"


