export interface Project {
    slug: string;
    title: string;
    icon: string;
    description: string;
}

export const projects: Project[] = [
    {
        slug: 'fly',
        title: 'Project Fly',
        icon: '✈️',
        description: 'Modify and build a remote controlled car utilizing 3D printing and electronics'
    },
    {
        slug: 'tt02',
        title: 'Project TT-02',
        icon: '🏎️',
        description: 'Build and race a remote controlled car.'
    }
];
