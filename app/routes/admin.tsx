import { useState } from "react";
import type { MetaFunction, LoaderFunctionArgs } from "react-router";
import { useLoaderData, useNavigate } from "react-router";

export const meta: MetaFunction = () => {
  return [{ title: "Admin - Add Project" }];
};

export async function loader({ request }: LoaderFunctionArgs) {
  // Check for basic auth header
  const authHeader = request.headers.get("Authorization");
  const adminPassword = process.env.ADMIN_PASSWORD;

  // If no password is set, allow access (for development)
  if (!adminPassword) {
    return { authenticated: true };
  }

  // Check if auth header is valid
  if (!authHeader?.startsWith("Bearer ")) {
    // Return unauthorized to trigger auth prompt
    throw new Response("Unauthorized", {
      status: 401,
      headers: {
        "WWW-Authenticate": `Bearer realm="Admin Panel"`,
      },
    });
  }

  const token = authHeader.substring(7);
  if (token !== adminPassword) {
    throw new Response("Invalid token", { status: 403 });
  }

  return { authenticated: true };
}

export default function AdminPage() {
  const data = useLoaderData<typeof loader>();
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [showTokenInput, setShowTokenInput] = useState(false);
  const [token, setToken] = useState("");
  const navigate = useNavigate();

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      if (!selectedFile.name.endsWith(".zip")) {
        setError("Please upload a .zip file");
        setFile(null);
        return;
      }
      setFile(selectedFile);
      setError("");
      setMessage("");
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) {
      setError("Please select a file");
      return;
    }

    setUploading(true);
    setError("");
    setMessage("");

    try {
      const formData = new FormData();
      formData.append("file", file);

      const headers: HeadersInit = {};
      if (token) {
        headers["Authorization"] = `Bearer ${token}`;
      }

      const response = await fetch("/api/upload-project", {
        method: "POST",
        body: formData,
        headers,
      });

      const responseData = await response.json();

      if (!response.ok) {
        if (response.status === 401 || response.status === 403) {
          setError("Invalid authentication token");
          setShowTokenInput(true);
        } else {
          setError(responseData.error || "Upload failed");
        }
      } else {
        setMessage(
          `Project uploaded successfully! A GitHub workflow will process it shortly.`
        );
        setFile(null);
        setToken("");
        if (e.currentTarget instanceof HTMLFormElement) {
          e.currentTarget.reset();
        }
      }
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "An error occurred during upload"
      );
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-md mx-auto bg-white rounded-lg shadow-md p-8">
        <h1 className="text-3xl font-bold mb-2">Add Project</h1>
        <p className="text-gray-600 mb-8">
          Upload a .zip file containing your project folder
        </p>

        {showTokenInput && (
          <div className="mb-6 p-4 bg-blue-50 border border-blue-200 rounded">
            <label className="block text-sm font-semibold mb-2">
              Admin Token Required
            </label>
            <input
              type="password"
              value={token}
              onChange={(e) => setToken(e.target.value)}
              placeholder="Enter admin token"
              className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500"
            />
            <p className="text-xs text-gray-500 mt-2">
              Contact an administrator for the token
            </p>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-blue-500 transition">
            <input
              type="file"
              accept=".zip"
              onChange={handleFileChange}
              disabled={uploading}
              className="hidden"
              id="file-input"
            />
            <label
              htmlFor="file-input"
              className="cursor-pointer block"
            >
              <div className="text-4xl mb-2">📦</div>
              <p className="font-semibold text-gray-700">
                {file ? file.name : "Click to select .zip file"}
              </p>
              <p className="text-sm text-gray-500 mt-2">
                or drag and drop
              </p>
            </label>
          </div>

          {error && (
            <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
              {error}
            </div>
          )}

          {message && (
            <div className="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded">
              {message}
            </div>
          )}

          <button
            type="submit"
            disabled={!file || uploading}
            className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-bold py-2 px-4 rounded transition"
          >
            {uploading ? "Uploading..." : "Upload Project"}
          </button>
        </form>

        <div className="mt-8 pt-8 border-t">
          <h2 className="font-bold mb-4">Project Folder Format</h2>
          <pre className="bg-gray-100 p-4 rounded text-sm overflow-auto">
{`project-name/
├── project-name.md
└── images/
    ├── image1.png
    ├── image2.jpg
    └── ...`}
          </pre>
        </div>
      </div>
    </div>
  );
}
