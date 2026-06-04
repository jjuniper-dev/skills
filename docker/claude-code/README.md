# Claude Code Docker Image

This directory contains a small Alpine-based Docker image for running the
Claude Code CLI inside a container.

One way to think about the image is: Alpine is the thin operating-system layer,
the Claude Code native installer provides the agent binary, and `/workspace` is
the mounted working memory where the agent sees your repository.

## Why Alpine + native installer

Anthropic documents two practical Claude Code install paths:

- `npm install -g @anthropic-ai/claude-code`
- the native installer: `curl -fsSL https://claude.ai/install.sh | bash`

For a small container, the native installer is the better primitive because the
final image does not need a Node/npm runtime. Alpine needs `libgcc`, `libstdc++`,
and `ripgrep` for the native build, so the Dockerfile installs those explicitly
and sets `USE_BUILTIN_RIPGREP=0`. `curl` is installed only as a temporary build
dependency and removed after Claude Code is installed.

## Build

From the repository root:

```bash
docker build -t claude-code:alpine docker/claude-code
```

To pin a specific Claude Code version:

```bash
docker build \
  --build-arg CLAUDE_CODE_VERSION=1.0.58 \
  -t claude-code:1.0.58 \
  docker/claude-code
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

## Run with Compose

```bash
WORKSPACE="$PWD" docker compose -f docker/claude-code/compose.yaml run --rm claude-code
```

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

The image intentionally includes only the small set of packages Claude Code
usually needs to operate on a repository:

- `claude-code`, installed by the native installer
- `bash`
- `git`
- `openssh-client`
- `ca-certificates`
- `libgcc`, `libstdc++`, and `ripgrep`, required by the Alpine native build path

It runs as a non-root `claude` user and uses `/workspace` as the default working
directory. Auto-update is disabled by default with `DISABLE_AUTOUPDATER=1` so the
container behaves like an immutable image; rebuild the image to update Claude
Code.
