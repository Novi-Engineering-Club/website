import type { MetaFunction, LoaderFunctionArgs } from "react-router";
import { useLoaderData, useParams } from "react-router";
import { MDXProvider, useMDXComponents } from "@mdx-js/react";
import remarkGfm from "remark-gfm";

export async function loader({ params }: LoaderFunctionArgs) {
  const projectName = params.projectName;
  if (!projectName) {
    throw new Response("Not Found", { status: 404 });
  }

  try {
    const mdxModule = await import(`/Users/smitpatil/Projects/website/app/routes/projects/${projectName}/${projectName}.mdx`);
    return {
      mdxContent: mdxModule.default,
      title: `Project ${projectName.toUpperCase()}`,
    };
  } catch (error) {
    console.error(`Failed to load MDX for project ${projectName}:`, error);
    throw new Response("Not Found", { status: 404 });
  }
}

export const meta: MetaFunction<typeof loader> = ({ data }) => {
  return [{ title: data?.title || "Project Not Found" }];
};

const components = {
  img: (props: any) => <img {...props} className="w-full h-auto" />,
};

export default function ProjectPage() {
  const { mdxContent: MDXContent } = useLoaderData<typeof loader>();
  const mdxComponents = useMDXComponents(components);

  return (
    <div className="project-page p-8">
      <MDXProvider components={mdxComponents}>
        <MDXContent />
      </MDXProvider>
    </div>
  );
}
