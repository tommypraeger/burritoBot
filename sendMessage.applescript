on run {targetMessage}
    tell application "Messages"
        activate --steal focus

        set targetService to id of service "SMS"
        set targetBuddy to "888222"

        set theBuddy to buddy targetBuddy of service id targetService
        send targetMessage to theBuddy
    end tell
end run