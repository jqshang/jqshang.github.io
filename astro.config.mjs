import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://jqshang.github.io',
  integrations: [sitemap()],
  // Old AcademicPages URLs keep working.
  redirects: {
    '/about': '/',
    '/publications': '/#publications',
    '/publication': '/#publications',
    '/projects': '/#projects',
    '/project': '/#projects',
    '/cv': '/#education',
    '/resume': '/#education',
  },
});
