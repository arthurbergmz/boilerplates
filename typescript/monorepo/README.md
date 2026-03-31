# {{monorepo-name}}

## Adding a workspace dependency

You can add a package from the monorepo as a dependency to an app by running the following command from the root of the monorepo:

```bash
npm install {{package-name}} -w {{app-name}}
```

## Running dev scripts at the same time

You can run the dev scripts of all apps at the same time by running the following command from the root of the monorepo:

```bashbash
npm run dev --workspaces
```

Or you can mention specific projects:

```bashbash
npm run dev -w {{app-name-1}} -w {{app-name-2}} -w {{package-name-1}} -w {{package-name-2}}
```
