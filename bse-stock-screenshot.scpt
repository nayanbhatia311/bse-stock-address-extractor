use framework "Foundation"
use framework "AppKit"
use scripting additions

property inputFilePath : POSIX path of "/Users/nbhatia3/Downloads/Unique_Stocks_List.csv"
property outputFolderPath : POSIX path of "/Users/nbhatia3/Downloads/SearchResults/"
property browser : "Chrome" -- Change to "Google Chrome" if preferred

on run
	set inputData to readFile(inputFilePath)
	set namesList to paragraphs of inputData
	
	-- Ensure the output folder exists
	do shell script "mkdir -p " & quoted form of outputFolderPath
	
	repeat with companyName in namesList
		if companyName is not "" then
			-- Perform Google search
			searchGoogle(companyName)
			
			-- Wait for the browser to load the page (increase the time in case of low bandwidth)
			delay 5
			
			-- Take screenshot
			set screenshotPath to outputFolderPath & companyName & ".png"
			takeScreenshot(screenshotPath)
		end if
	end repeat
end run

on searchGoogle(searchQuery)
	if browser is "Safari" then
		tell application "Safari"
			activate
			set URL of front document to "https://www.google.com/search?q=bse address " & (do shell script "echo " & quoted form of searchQuery & " | perl -MURI::Escape -ne 'print uri_escape($_)'")
		end tell
	else if browser is "Google Chrome" then
		tell application "Google Chrome"
			activate
			tell window 1 to set URL of active tab to "https://www.google.com/search?q=bse address " & (do shell script "echo " & quoted form of searchQuery & " | perl -MURI::Escape -ne 'print uri_escape($_)'")
		end tell
	end if
end searchGoogle

on takeScreenshot(savePath)
	do shell script "screencapture -x " & quoted form of savePath
end takeScreenshot

on readFile(filePath)
	set fileReference to open for access filePath
	set fileContents to read fileReference
	close access fileReference
	return fileContents
end readFile
