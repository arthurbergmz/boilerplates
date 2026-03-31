import { defineConfig } from 'oxfmt'

export default defineConfig({
  printWidth: 120,
  trailingComma: 'all',
  semi: false,
  singleQuote: true,
  tabWidth: 2,
  arrowParens: 'always',
  endOfLine: 'lf',
  bracketSpacing: true,
  quoteProps: 'as-needed',
  singleAttributePerLine: true,
  insertFinalNewline: true,
  sortImports: true,
  sortPackageJson: true,
  ignorePatterns: ['node_modules', 'dist', 'build', '**.config.**', '**.test.**'],
  // "experimentalTernaries": true,
  // "experimentalOperatorPosition": "start",
})
