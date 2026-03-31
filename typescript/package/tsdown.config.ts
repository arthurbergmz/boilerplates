import { defineConfig } from 'tsdown/config'

export default defineConfig({
  // only exports index.ts files and excludes test files
  entry: ['src/**/index.ts', '!src/**/*.test.ts'],
  dts: {
    tsgo: true,
  },
  exports: true,
  platform: 'neutral',
  format: 'esm',
  deps: {
    onlyBundle: [],
  },
  clean: true,
  // let consumers handle minification
  minify: false,
  treeshake: true,
})
