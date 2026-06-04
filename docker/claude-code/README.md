# Claude Code Docker Image

This directory contains a small Alpine-based Docker image for running the
Claude Code CLI inside a container.

One way to think about the image is: Alpine is the thin operating-system layer,
`claude-code` is the native agent binary, and `/workspace` is the mounted working
memory where the agent sees your repository.

## Why Alpine

Anthropic publishes an official Alpine `apk` package for Claude Code. Using that
package avoids installing Node/npm in the final image because the current Claude
Code distribution installs a native binary. The result is smaller and simpler
than a Node base image.

## Build

From the repository root:

```bash
docker build -t claude-code:alpine docker/claude-code
```

## Run against the current directory

```bash
docker run --rm -it \
  -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
  -v "$PWD:/workspace" \
  -v claude-code-home:/home/claude/.claude \
  claude-code:alpine
```

If you authenticate interactively instead of using `ANTHROPIC_API_KEY`, keep the
named `.claude` volume so the login state survives container restarts.

## Run a one-shot prompt

```bash
docker run --rm -it \
  -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
  -v "$PWD:/workspace" \
  -v claude-code-home:/home/claude/.claude \
  claude-code:alpine \
  --print "Summarize this repository"
```

## Image contents

The image intentionally includes only the small set of tools Claude Code usually
needs to operate on a repository:

- `claude-code`
- `bash`
- `git`
- `openssh-client`
- `ca-certificates`

It runs as a non-root `claude` user and uses `/workspace` as the default working
directory.
