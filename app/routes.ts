import { type RouteConfig } from "@react-router/dev/routes";

export default [
  { path: "/", file: "routes/home.tsx" },
  { path: "/meetings", file: "routes/meetings.tsx" },
  { path: "/project-fly", file: "routes/project-fly.tsx" },
  { path: "/project-tt02", file: "routes/project-tt02.tsx" },
] satisfies RouteConfig;

