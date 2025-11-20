import type { Route } from "./+types/project-fly";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Project Fly" },
    { name: "description", content: "Details about Project Fly" },
  ];
}

export default function ProjectFly() {
  return (
    <div className="project-fly-page">
      <h1 className="text-4xl font-bold mb-4">Project Fly</h1>
      <p>This page will contain details about Project Fly. Stay tuned for updates!</p>
    </div>
  );
}