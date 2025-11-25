import type { MetaFunction, LoaderFunctionArgs } from "react-router";
import { useLoaderData } from "react-router";
import { MDXProvider, useMDXComponents } from "@mdx-js/react";
import FlyProject from "./projects/fly/fly.mdx";
import TT02Project from "./projects/tt02/tt02.mdx";

const projectMap = {
  fly: FlyProject,
  tt02: TT02Project,
};

export async function loader({ params }: LoaderFunctionArgs) {
  const projectName = params.projectName;
  if (!projectName || !(projectName in projectMap)) {
    throw new Response("Not Found", { status: 404 });
  }

  return {
    projectName,
    title: `Project ${projectName.toUpperCase()}`,
  };
}

export const meta: MetaFunction<typeof loader> = ({ data }) => {
  return [{ title: data?.title || "Project Not Found" }];
};

const components = {
  img: (props: any) => <img {...props} className="w-full h-auto" />,
};

export default function ProjectPage() {
  const { projectName } = useLoaderData<typeof loader>();
  const MDXContent = projectMap[projectName as keyof typeof projectMap];
  const mdxComponents = useMDXComponents(components);

  return (
    <div className="project-page p-8 mdx-content">
      <MDXProvider components={mdxComponents}>
        <MDXContent />
      </MDXProvider>
    </div>
  );
}
