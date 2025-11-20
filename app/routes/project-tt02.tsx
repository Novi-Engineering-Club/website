import type { Route } from "./+types/project-tt02";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Project TT-02" },
    { name: "description", content: "Details about Project TT-02" },
  ];
}

export default function ProjectTT02() {
  return (
    <div className="project-tt02-page">
      <h1 className="text-4xl font-bold mb-4">Project TT-02</h1>
      <p>This page will contain details about Project TT-02. Stay tuned for updates!</p>
    </div>
  );
}