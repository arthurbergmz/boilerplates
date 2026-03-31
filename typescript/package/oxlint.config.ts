import { defineConfig } from 'oxlint'

export default defineConfig({
  plugins: ['import'],
  options: {
    typeAware: true,
    typeCheck: true,
  },
  settings: {
    vitest: {
      typecheck: false,
    },
  },
  ignorePatterns: ['node_modules', 'dist', 'build', '**.config.**', '**.test.**'],
  rules: {
    'eqeqeq': 'warn',
    'import/no-cycle': 'error',
    'no-unused-vars': 'warn',
    'typescript/no-import-type-side-effects': 'warn',
    'typescript/no-redundant-type-constituents': 'off',
    'typescript/consistent-type-exports': [
      'warn',
      {
        'fixMixedExportsWithInlineTypeSpecifier': true,
      },
    ],
    'typescript/consistent-type-imports': [
      'warn',
      {
        'prefer': 'type-imports',
        'fixStyle': 'inline-type-imports',
      },
    ],
    'typescript/unbound-method': [
      'warn',
      {
        'ignoreStatic': true,
      },
    ],
  },
})
