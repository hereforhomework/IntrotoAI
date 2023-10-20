@echo off
rem Check if pip (Python package manager) is available
where pip > nul 2>&1
if %errorlevel% equ 1 (
    echo Error: Pip is not available on this system.
    pause
    exit /b 1
)

rem Prompt the user for input
set /p map_name="Enter map name(RobotNav-test.txt): "
set /p search_method="Enter search method(dfs, bfs, gbfs, a*, ucs, bestfs): "

rem Run the Python script with user input
python main.py %map_name% %search_method%

pause

