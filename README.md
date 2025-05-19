# app-service

## Instructions for creating a new release

To check the current version of the app run:

```zsh
bumpver show
```

We use `-alpha` to tag a pre-release instead of `-pre`.

Incrementing from alpha-release to stable is a conscious decision, so to make a stable release remove `-alpha`
from the version, e.g. is the current version is `1.0.14-alpha` you can run

```zsh
bumpver update --set-version "1.0.14" --dry  # Remove --dry to execute
```

After this is done, you can create a matching git tag by prefixing the version with `v`,
e.g.

```zsh
git tag v1.0.14
```

Then push the tag to origin and this will trigger a release workflow and update `main` to the next alpha release.

