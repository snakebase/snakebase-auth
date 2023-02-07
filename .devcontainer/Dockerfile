FROM archlinux

# Update the system
RUN pacman -Syyu --noconfirm

# Install Docker, Git and Poetry
RUN pacman -S --noconfirm docker git python-poetry

# Install Zsh and OhMyZsh
RUN pacman -S --noconfirm zsh
RUN echo "if [ -t 1 ]; then" >> /root/.bashrc
RUN echo "exec zsh" >> /root/.bashrc
RUN echo "fi" >> /root/.bashrc
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Install Yay
RUN pacman -S --noconfirm base-devel sudo
RUN useradd -m makepkg
RUN echo "makepkg ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER makepkg
WORKDIR /home/makepkg
RUN git clone https://aur.archlinux.org/yay.git
RUN cd yay && makepkg -si --noconfirm

# Install the Python 3.11
RUN yay -S --noconfirm python311

# Reset the user
USER root
WORKDIR /root

# Clean up
RUN userdel makepkg && rm -rf /home/makepkg && pacman -R --noconfirm base-devel sudo yay