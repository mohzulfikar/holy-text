# POST Installation Arch (or Arch based linux)
 * Installing GUI, see <a href=https://wiki.archlinux.org/index.php/Desktop_environment> this link </a>
 * Install LTS kernel and switch to LTS kernel, see <a href=https://wiki.archlinux.org/index.php/Kernel> this </a> or <a href="https://www.youtube.com/watch?v=b-H3jURTgqk"> this link </a> <br>
    use <code> # pacman -S linux-lts </code> to install lts kernel
 * ... (More Coming soon...)
 
## Sub section for arch-based user (Especially Manjaro)
 * Update arch linux keyring and pacman database <br>
   <code> # pacman -Syy </code> < Syncronize pacman
 * Configure your pacman-mirrors see <a href="https://wiki.manjaro.org/Pacman-mirrors">this link</a>
   - Customize your mirror pool, for new linux user i recommend to use <code> # pacman-mirrors --interactive --default </code>, then select the nearest mirror (it's recommended to select http/https over ftp).
   - Fastracking the mirror using <code> # pacman-mirrors --fasttrack [n] </code>, here you can specify the n value (use it without bracket).
   - Go to the next step.
 * Upgrade your distro <br>
   <code> # pacman -Su </code>
 * ...Or update and upgrade at once <br>
   <code> # pacman -Syyu </code>, take a note that if the upgrade process (especially on downloading package) is slow, configure your pacman-mirrors first.
 * Install recommended LTS kernel from <a href="https://wiki.manjaro.org/index.php?title=Manjaro_Kernels">mhwd-kernel</a> (Manjaro Hardware Detection)
 * Install yay for <a href="https://wiki.archlinux.org/index.php/AUR_helpers">AUR helper</a>, visit <a href=https://github.com/Jguer/yay>this link</a> (please RTFM)
 * <a href="https://www.youtube.com/watch?v=iaXQdyHRL8M">Customize your terminal</a>, use zsh or fish. Take a look at <a href="https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH">this</a> or <a href="https://github.com/ohmyzsh/ohmyzsh">this link</a>. (If you are indonesian check <a href="https://www.codepolitan.com/memasang-zsh-dan-oh-my-zsh-di-linux-ubuntu-5a8eb22e1ae13">this out for translated tutorial</a>)
 
* Learn the pacman package manager, from <a href="https://www.youtube.com/watch?v=-dEuXTMzRKs&t=765s">this</a> or <a href="https://www.youtube.com/watch?v=-UvZ4BEAXFU">this link</a>
* Learn Bash Scripting, <a href="https://www.youtube.com/watch?v=oxuRxtrO2Ag&t=2914s">this</a> or <a href="https://www.youtube.com/watch?v=v-F3YLd6oMw">this link</a>

## Sub section for installing blackarch database
 * Just Follow the steps on <a href="https://blackarch.org/downloads.html#install-repo">this site</a>
 * Don't forget to update the database after that and do the upgrade.
    <code> # pacman -Syyu </code>
