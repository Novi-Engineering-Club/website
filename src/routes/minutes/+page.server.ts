interface Meeting {
    date: string;
    attendees: string;
    topics: string[];
    notes: string;
}

function parseMeetingMinutes(text: string): Meeting[] {
    const results: Meeting[] = [];
    const parts = text.split("DATE:").filter((p) => p.trim());

    for (const part of parts) {
        const lines = part.split("\n");

        const meeting: Meeting = {
            date: lines[0].trim(),
            attendees: "N/A",
            topics: [],
            notes: ""
        };

        let inTopics = false;

        for (let i = 1; i < lines.length; i++) {
            const line = lines[i].trim();
            if (!line) continue;

            if (line.startsWith("ATTENDEES:")) {
                meeting.attendees = line.substring(10).trim();
            } else if (line.startsWith("TOPICS:")) {
                inTopics = true;
            } else if (line.startsWith("NOTES:")) {
                meeting.notes = line.substring(6).trim();
                inTopics = false;
            } else if (inTopics && line.startsWith("-")) {
                const topic = line.substring(1).trim();
                if (topic) meeting.topics.push(topic);
            }
        }

        results.push(meeting);
    }

    return results;
}

export async function load({ fetch }) {
    try {
        const response = await fetch("/meeting-minutes.txt");
        
        if (!response.ok) {
            return {
                meetings: [],
                error: "Failed to load meeting minutes"
            };
        }
        
        const text = await response.text();
        const meetings = parseMeetingMinutes(text);

        return {
            meetings,
            error: null
        };
    } catch (err) {
        console.error("Error loading meetings:", err);
        return {
            meetings: [],
            error: err instanceof Error ? err.message : "Failed to load meetings"
        };
    }
}
