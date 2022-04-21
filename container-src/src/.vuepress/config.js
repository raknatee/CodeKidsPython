const { description } = require('../../package')

module.exports = {
    /**
     * Ref：https://v1.vuepress.vuejs.org/config/#title
     */
    title: 'Python',
    /**
     * Ref：https://v1.vuepress.vuejs.org/config/#description
     */
    description: description,
    // base: "/html-css/",
    dest: "/home/deploy",
    /**
     * Extra tags to be injected to the page HTML `<head>`
     *
     * ref：https://v1.vuepress.vuejs.org/config/#head
     */
    head: [
        ['meta', { name: 'theme-color', content: '#3eaf7c' }],
        ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
        ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }]
    ],

    /**
     * Theme configuration, here is the default theme configuration for VuePress.
     *
     * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
     */
    themeConfig: {
        repo: '',
        editLinks: false,
        docsDir: '',
        editLinkText: '',
        lastUpdated: false,
        search: false,

    },
    markdown: {
        lineNumbers: true
    },
    /**
     * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
     */
    plugins: [
        '@vuepress/plugin-back-to-top',
        '@vuepress/plugin-medium-zoom',
        [
            'vuepress-plugin-container',   
            {
              type: 'output',
              defaultTitle: 'OUTPUT',
              before: info => `<div class="output"><p class="title">${info}</p><div class="language- "><pre class="language-text"><code>`,
              after: '</code></pre></div></div>',
            },
          ],
        [
            'vuepress-plugin-mathjax',
            {
              target: 'svg',
              macros: {
                '*': '\\times',
              },
            }
        ],
    ]
}