import { parse } from 'yaml';
import profileRaw from './profile.yaml?raw';
import publicationsRaw from './publications.yaml?raw';
import projectsRaw from './projects.yaml?raw';
import cvRaw from './cv.yaml?raw';

export const profile = parse(profileRaw);
export const publications = parse(publicationsRaw);
export const projects = parse(projectsRaw);
export const cv = parse(cvRaw);
