FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Dependencias base y para compilación de keystone/unicorn
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

USER pwner
WORKDIR /home/pwner

# Crear carpeta para retos
RUN mkdir /home/pwner/challenges
VOLUME ["/home/pwner/challenges"]

# Instalar herramientas Python
RUN pip3 install --upgrade pip setuptools && \
    pip3 install pwntools ropper gdbgui angr binwalk

# Instalar pwndbg
RUN git clone https://github.com/pwndbg/pwndbg /home/pwner/pwndbg && \
    cd /home/pwner/pwndbg && ./setup.sh

# Instalar radare2
RUN git clone https://github.com/radareorg/radare2 /home/pwner/radare2 && \
    /home/pwner/radare2/sys/install.sh

# Instalar Keystone desde fuente
RUN git clone https://github.com/keystone-engine/keystone.git /home/pwner/keystone && \
    cd /home/pwner/keystone && \
    mkdir build && cd build && \
    cmake .. && make -j$(nproc) && sudo make install && sudo ldconfig

# Instalar Unicorn desde fuente (usando CMake)
RUN git clone https://github.com/unicorn-engine/unicorn.git /home/pwner/unicorn && \
    cd /home/pwner/unicorn && \
    mkdir build && cd build && \
    cmake .. && make -j$(nproc) && sudo make install && sudo ldconfig

# Exponer puerto para gdbgui
EXPOSE 5000

CMD ["/bin/bash"]
