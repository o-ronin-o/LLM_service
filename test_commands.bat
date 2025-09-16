@echo off
echo Testing MOVE_TO commands...
echo ============================

curl "http://localhost:8000/chat?prompt=Move%20to%20coordinates%2010,%205"
echo.
curl "http://localhost:8000/chat?prompt=Go%20to%20position%20-3.5,%207.2"
echo.
curl "http://localhost:8000/chat?prompt=Navigate%20to%20coordinates%2015.5,%20-8.3"
echo.

echo Testing ROTATE commands...
echo ==========================

curl "http://localhost:8000/chat?prompt=Rotate%2090%20degrees%20clockwise"
echo.
curl "http://localhost:8000/chat?prompt=Turn%2045%20degrees%20counter-clockwise"
echo.
curl "http://localhost:8000/chat?prompt=Spin%20360%20degrees%20clockwise"
echo.

echo Testing START_PATROL commands...
echo ================================

curl "http://localhost:8000/chat?prompt=Start%20patrolling%20the%20first%20floor"
echo.
curl "http://localhost:8000/chat?prompt=Begin%20fast%20patrol%20of%20bedrooms"
echo.
curl "http://localhost:8000/chat?prompt=Patrol%20second%20floor%203%20times"
echo.

echo Testing Conversational commands...
echo ==================================

curl "http://localhost:8000/chat?prompt=Hello,%20how%20are%20you?"
echo.
curl "http://localhost:8000/chat?prompt=What%20can%20you%20do?"
echo.