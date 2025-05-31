FROM ubuntu:22.04

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
    qemu qemu-user qemu-user-static \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario no-root con sudo sin contraseña
RUN useradd -ms /bin/bash pwner && \
    echo 'pwner ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Copiar script y permisos (como root)
COPY scripts/xpl.py /opt/xpl.py
RUN chmod +x /opt/xpl.py && chown pwner:pwner /opt/xpl.py

# Cambiar a usuario pwner
USER pwner
WORKDIR /home/pwner

RUN export PATH="$PATH:/home/pwner/.local/bin"

# Instalar herramientas Python
RUN pip3 install --upgrade pip setuptools && \
    pip3 install pwntools ropper gdbgui angr binwalk

# Instalar pwndbg
RUN git clone https://github.com/pwndbg/pwndbg /home/pwner/pwndbg && \
    cd /home/pwner/pwndbg && ./setup.sh


RUN pip3 install keystone-engine




# Alias para copiar script
RUN echo "alias pwn_create='cp /opt/xpl.py .'" >> /home/pwner/.bashrc

RUN echo "source /home/pwner/pwndbg/gdbinit.py"  > ~/.gdbinit

RUN echo "unbind C-b" >> /root/.tmux.conf && \
    echo "set-option -g prefix C-a" >> /root/.tmux.conf && \
    echo "bind C-a send-prefix" >> /root/.tmux.conf

RUN tmux source-file ~/.tmux.conf

# Crear carpeta para retos y volumen
RUN mkdir /home/pwner/challenges
VOLUME ["/home/pwner/challenges"]

# Exponer puerto para gdbgui
EXPOSE 5000

CMD ["/bin/bash"]
