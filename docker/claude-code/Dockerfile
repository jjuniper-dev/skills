# syntax=docker/dockerfile:1

# Small Claude Code runtime image.
#
# Mechanically, this uses Alpine because Anthropic publishes a native apk
# package for Claude Code. That avoids carrying Node/npm in the final image:
# the container is mostly Alpine + the Claude Code native binary + a small
# POSIX development surface for real repository work.
ARG ALPINE_VERSION=3.22
FROM alpine:${ALPINE_VERSION}

ARG USERNAME=claude
ARG UID=1000
ARG GID=1000

LABEL org.opencontainers.image.title="Claude Code Alpine" \
      org.opencontainers.image.description="Small Alpine-based image for running the Claude Code CLI in a container" \
      org.opencontainers.image.source="https://code.claude.com/docs/en/installation"

RUN set -eux; \
    apk add --no-cache ca-certificates; \
    apk add --no-cache --virtual .fetch-deps wget; \
    wget -O /etc/apk/keys/claude-code.rsa.pub \
      https://downloads.claude.ai/keys/claude-code.rsa.pub; \
    echo "395759c1f7449ef4cdef305a42e820f3c766d6090d142634ebdb049f113168b6  /etc/apk/keys/claude-code.rsa.pub" | sha256sum -c -; \
    echo "https://downloads.claude.ai/claude-code/apk/stable" >> /etc/apk/repositories; \
    apk add --no-cache \
      bash \
      claude-code \
      git \
      openssh-client; \
    apk del .fetch-deps; \
    addgroup -g "${GID}" "${USERNAME}"; \
    adduser -D -h "/home/${USERNAME}" -s /bin/bash -u "${UID}" -G "${USERNAME}" "${USERNAME}"; \
    mkdir -p /workspace "/home/${USERNAME}/.claude"; \
    chown -R "${USERNAME}:${USERNAME}" /workspace "/home/${USERNAME}/.claude"; \
    claude --version

USER ${USERNAME}
WORKDIR /workspace
ENV HOME=/home/${USERNAME}

VOLUME ["/workspace", "/home/claude/.claude"]
ENTRYPOINT ["claude"]
CMD ["--help"]
