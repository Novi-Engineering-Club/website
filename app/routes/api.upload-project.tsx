import type { ActionFunction } from "react-router";

export const action: ActionFunction = async ({ request }) => {
  if (request.method !== "POST") {
    return Response.json({ error: "Method not allowed" }, { status: 405 });
  }

  // Validate admin password if set
  const adminPassword = process.env.ADMIN_PASSWORD;
  if (adminPassword) {
    const authHeader = request.headers.get("Authorization");

    if (!authHeader?.startsWith("Bearer ")) {
      return Response.json(
        { error: "Admin token required" },
        { status: 401 }
      );
    }

    const token = authHeader.substring(7);
    if (token !== adminPassword) {
      return Response.json(
        { error: "Invalid admin token" },
        { status: 403 }
      );
    }
  }

  try {
    const formData = await request.formData();
    const file = formData.get("file") as File;

    if (!file) {
      return Response.json({ error: "No file provided" }, { status: 400 });
    }

    if (!file.name.endsWith(".zip")) {
      return Response.json({ error: "File must be a .zip" }, { status: 400 });
    }

    const buffer = await file.arrayBuffer();
    const uint8Array = new Uint8Array(buffer);

    // Extract project name from filename (strip .zip)
    const projectName = file.name.replace(".zip", "").toLowerCase();

    if (!projectName || projectName.length === 0) {
      return Response.json(
        { error: "Invalid project name" },
        { status: 400 }
      );
    }

    // Dispatch workflow
    const dispatchPayload = {
      event_type: "upload_project",
      client_payload: {
        projectName: projectName,
        zipContent: Buffer.from(uint8Array).toString("base64"),
      },
    };

    // Send to GitHub API to trigger workflow
    const githubResponse = await fetch(
      `https://api.github.com/repos/Novi-Engineering-Club/website/dispatches`,
      {
        method: "POST",
        headers: {
          Authorization: `token ${process.env.GITHUB_TOKEN}`,
          "Content-Type": "application/json",
          Accept: "application/vnd.github.v3+raw",
        },
        body: JSON.stringify(dispatchPayload),
      }
    );

    if (!githubResponse.ok) {
      const errorText = await githubResponse.text();
      console.error("GitHub dispatch failed:", errorText);
      return Response.json(
        { error: "Failed to trigger workflow" },
        { status: 500 }
      );
    }

    return Response.json({
      success: true,
      message: "Project uploaded successfully! Workflow processing...",
      projectName: projectName,
    });
  } catch (error) {
    console.error("Upload error:", error);
    return Response.json(
      { error: error instanceof Error ? error.message : "Unknown error" },
      { status: 500 }
    );
  }
};
