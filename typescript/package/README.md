# {{package-title}}

> @{{namespace}}/{{package-name}}

{{package-description}}
A starter project for a Typescript package.

## Getting started

Replace the following with your own values:

- `{{namespace}}`: the namespace of your package, e.g. `my-org`
- `{{package-name}}`: the name of your package, e.g. `my-package`
- `{{package-title}}`: a human-friendly title for your package, e.g. `My Package`
- `{{package-description}}`: a short description of your package, e.g. `A starter project for a Typescript package.`
- `{{package-version}}`: the version of your package, e.g. `0.0.1`
- `{{license}}`: the license of your package, e.g. `MIT` or `UNLICENSED`
- `{{author-name}}`: the name of the author of your package, e.g. `John Doe`
- `{{author-email}}`: the email of the author of your package, e.g. `john.doe@example.com`
- `{{repository-url}}`: the URL of your package's repository, e.g. `https://github.com/my-org/my-package`

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
