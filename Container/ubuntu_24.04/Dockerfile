# Dockerfile
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Dependencias base y para compilación
RUN apt update && apt install -y \
    sudo python3 python3-pip python3-dev \
    gdb git curl wget unzip \
    build-essential cmake pkg-config \
    libglib2.0-dev libpixman-1-dev \
    patchelf \
    libssl-dev libffi-dev \
    libcapstone-dev \
    libz3-dev \
    socat \
    net-tools iproute2 \
    vim nano tmux \
    qemu-system qemu-utils qemu-user qemu-user-static \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario no-root con sudo sin contraseña
RUN useradd -ms /bin/bash pwner && \
    echo 'pwner ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

COPY scripts/xpl.py /opt/xpl.py
RUN chmod +x /opt/xpl.py && chown pwner:pwner /opt/xpl.py

USER pwner
WORKDIR /home/pwner

RUN export PATH="$PATH:/home/pwner/.local/bin"

# Instalar herramientas Python
RUN pip3 install --upgrade pip setuptools --break-system-packages && \
    pip3 install pwntools ropper gdbgui angr binwalk keystone-engine --break-system-packages

# Instalar pwndbg
RUN git clone https://github.com/pwndbg/pwndbg /home/pwner/pwndbg && \
    cd /home/pwner/pwndbg && ./setup.sh

# Alias y config
RUN echo "alias pwn_create='cp /opt/xpl.py .'" >> ~/.bashrc 

RUN echo "unbind C-b" >> /root/.tmux.conf && \
    echo "set-option -g prefix C-a" >> /root/.tmux.conf && \
    echo "bind C-a send-prefix" >> /root/.tmux.conf

RUN tmux source-file ~/.tmux.conf

RUN mkdir /home/pwner/challenges
VOLUME ["/home/pwner/challenges"]
EXPOSE 5000

CMD ["/bin/bash"]
