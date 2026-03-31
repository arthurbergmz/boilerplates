# {{package-title}}

> @{{namespace}}/{{package-name}}

A starter project for a Typescript package.

## Getting started

Install dependencies by running:

```bash
npm install
```

Unit tests must be placed in the same folder as the source code in `/src`, and must be suffixed by `.test.ts`.
The purpose of `/tests` folder is to validate how two or more functions or modules work together, focusing on behavior across boundaries inside the package.

Run tests with:

```bash
# runs tests in watch mode, re-running when files change
npm run test:watch

# runs tests once and exits
npm run test
```

You may build the package with:

```bash
npm run build
```
