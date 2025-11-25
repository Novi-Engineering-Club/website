import { type RouteConfig } from "@react-router/dev/routes";

export default [
  { index: true, file: "routes/home.tsx" },
  { path: "meetings", file: "routes/meetings.tsx" },
  { path: "admin", file: "routes/admin.tsx" },
  { path: "api/upload-project", file: "routes/api.upload-project.tsx" },
  { path: "projects/:projectName", file: "routes/projects.$projectName.tsx" },
] satisfies RouteConfig;
