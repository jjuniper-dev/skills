# syntax=docker/dockerfile:1

# Small Claude Code runtime image.
#
# Mechanically, Alpine is the thin OS layer, the Claude Code native installer
# drops the agent binary into the non-root user's home directory, and /workspace
# is the mounted repository the agent operates on.
ARG ALPINE_VERSION=3.22
FROM alpine:${ALPINE_VERSION}

ARG USERNAME=claude
ARG UID=1000
ARG GID=1000
ARG CLAUDE_CODE_VERSION=stable

LABEL org.opencontainers.image.title="Claude Code Alpine" \
      org.opencontainers.image.description="Small Alpine-based image for running the Claude Code CLI in a container" \
      org.opencontainers.image.source="https://docs.anthropic.com/en/docs/claude-code/getting-started"

ENV HOME=/home/${USERNAME} \
    PATH=/home/${USERNAME}/.local/bin:/home/${USERNAME}/.claude/local:${PATH} \
    USE_BUILTIN_RIPGREP=0 \
    DISABLE_AUTOUPDATER=1

RUN set -eux; \
    apk add --no-cache \
      bash \
      ca-certificates \
      git \
      libgcc \
      libstdc++ \
      openssh-client \
      ripgrep; \
    apk add --no-cache --virtual .fetch-deps curl; \
    addgroup -g "${GID}" "${USERNAME}"; \
    adduser -D -h "${HOME}" -s /bin/bash -u "${UID}" -G "${USERNAME}" "${USERNAME}"; \
    mkdir -p /workspace "${HOME}/.claude" "${HOME}/.local/bin"; \
    chown -R "${USERNAME}:${USERNAME}" /workspace "${HOME}"; \
    su "${USERNAME}" -c "curl -fsSL https://claude.ai/install.sh | bash -s ${CLAUDE_CODE_VERSION}"; \
    su "${USERNAME}" -c "claude --version"; \
    apk del .fetch-deps

USER ${USERNAME}
WORKDIR /workspace

VOLUME ["/workspace", "/home/claude/.claude"]
ENTRYPOINT ["claude"]
CMD ["--help"]
