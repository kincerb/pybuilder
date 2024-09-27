#!/bin/bash

APPIMAGE_DIR="${1:-${PWD}}"
APP_DIR=/opt/mwautomation/lifecycle-checkins
APP_BINS=("pip" "pip3" "python" "python3")
APP_BINS+=("wheel")

convert_for_docker() {
  if [ -z "${1}"]; then
    echo "Provide path to AppImage"
    return 1
  fi
  local appimage="${1}"
  if [ ! -e "${appimage}" ];
    echo "Could not find: ${appimage}"
    return 2
  fi
  sed -i 's|AI\x02|\x00\x00\x00|' "${appimage}"
}

fix_manylinux_cflags() {
  if [ -z "${1}"]; then
    echo "Provide path to AppDir"
    return 1
  fi
  local appdir="${1}"
  if [ ! -e "${appdir}/AppRun" ];
    echo "Could not find AppRun inside: ${appdir}"
    return 2
  fi
  sed -i '/^export.*CFLAGS/ s|/python3.11d|/python3.11|' "${appdir}/AppRun"
}

link_app_bins() {
  pushd "${APP_DIR}"/bin
  for _link in ${APP_BINS[@]}; do
    ln -s python "${_link}"
  done
  popd &>/dev/null
}

# clear $DIRSTACK
dirs -c

pushd "${APPIMAGE_DIR}"

for _x in $(find ./usr/local/bin -type f -printf "%p "); do
	if [[ "$(file --brief --no-dereference ${_x})" =~ ^[Pp]ython.*script ]]; then
		sed -i '1s|^[#][!]/.*|#!/bin/env python|' "${_x}"
	fi
done

popd &>/dev/null

arch=x86_64 appimagetool "${APPIMAGE_DIR}" "${APP_DIR}/bin/python"
link_app_bins

# return to original directory
while popd &>/dev/null; do :; done
