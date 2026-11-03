import { parse } from 'yaml';
import profileRaw from './profile.yaml?raw';
import previewsRaw from './previews.yaml?raw';
import publicationsRaw from './publications.yaml?raw';
import projectsRaw from './projects.yaml?raw';
import cvRaw from './cv.yaml?raw';
import musicRaw from './music.yaml?raw';
import notesRaw from './notes.yaml?raw';

export const profile = parse(profileRaw);
export const previews: Record<string, { title: string; sub: string; body: string; url: string }> = parse(previewsRaw);
export const publications = parse(publicationsRaw).filter((p: any) => !p.hidden);
export const projects = parse(projectsRaw);
export const cv = parse(cvRaw);
export const music = parse(musicRaw);
export const notes = parse(notesRaw) ?? {};

const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
/** Turn [[key|text]] into a link that opens a hover preview, and __text__ into an underlined emphasis. */
export function withPreviews(text: string): string {
  return esc(text).replace(/__(.+?)__/g, '<span class="mark">$1</span>').replace(/\[\[([\w-]+)\|([^\]]+)\]\]/g, (_, key, label) => {
    const p = previews[key];
    if (!p) return label;
    return `<a class="pv" href="${p.url}" data-preview="${key}">${label}</a>`;
  });
}
