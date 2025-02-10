#!/bin/bash

# Define color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color
CYAN='\033[0;36m'
CHECK_MARK="\xE2\x9C\x94" # ✔
CROSS_MARK="\xE2\x9D\x8C" # ✘

# General installation check and installation function
install_tool() {
  local name=$1
  local check_command=$2
  local install_command=$3

  # Check if tool is already installed
  if eval "$check_command" &>/dev/null; then
    echo -e "${GREEN}${CHECK_MARK} $name is already installed.${NC}"
  else
    echo -e "${RED}${CROSS_MARK} $name is not installed. Installing now...${NC}"
    # Proceed with installation
    eval "$install_command"
    # Verify the installation
    if eval "$check_command" &>/dev/null; then
      echo -e "${GREEN}$name installation successful!${NC}"
    else
      echo -e "${RED}$name installation failed.${NC}"
      exit 1  # Exit if installation fails
    fi
  fi
}

# Function to handle OpenJDK symlink creation
setup_java_symlink() {
  local java_prefix
  java_prefix=$(brew --prefix openjdk@17 2>/dev/null || true)

  if [[ -n "$java_prefix" ]]; then
    local target_path="$java_prefix/libexec/openjdk.jdk"
    local symlink_path="/Library/Java/JavaVirtualMachines/openjdk.jdk"

    if [[ ! -L "$symlink_path" ]]; then
      echo -e "${YELLOW}Creating Java symlink at $symlink_path -> $target_path${NC}"
      sudo ln -sfn "$target_path" "$symlink_path"
      echo -e "${GREEN}${CHECK_MARK} Java symlink created successfully.${NC}"
    else
      echo -e "${GREEN}${CHECK_MARK} Java symlink already exists.${NC}"
    fi
  else
    echo -e "${RED}${CROSS_MARK} Failed to find OpenJDK path using Homebrew.${NC}"
    exit 1
  fi
}

# List of tools to check and install
tools=(
  "OpenJDK 17:brew list --formula | grep -q 'openjdk@17':brew install openjdk@17"
  "golangci-lint:brew list --formula | grep -q 'golangci-lint':brew install golangci-lint"
  "diffutils:brew list --formula | grep -q 'diffutils':brew install diffutils"
  "Rust:command -v rustc:curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && source \"$HOME/.cargo/env\""
  "cmake:brew list --formula | grep -q 'cmake':brew install cmake"
  "Python 3:command -v python3:brew install python3"
  "semgrep:brew list --formula | grep -q 'semgrep':brew install semgrep"
  "Node.js:command -v node:brew install node"
  "npm:command -v npm:brew install node"
  "Azurite:command -v azurite:npm install -g azurite"
  "Bazel:command -v bazel:brew install bazelisk"
)

echo -e "${CYAN}Checking installation status for the following tools and software:${NC}\n"

# Install Homebrew first
if ! command -v brew &>/dev/null; then
    echo -e "${RED}${CROSS_MARK} Homebrew is not installed. Installing now...${NC}"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    # Add Homebrew to PATH immediately after installation
    if [[ -f "/opt/homebrew/bin/brew" ]]; then
        echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> "$HOME/.zprofile"
        eval "$(/opt/homebrew/bin/brew shellenv)"
    elif [[ -f "/usr/local/bin/brew" ]]; then
        echo 'eval "$(/usr/local/bin/brew shellenv)"' >> "$HOME/.zprofile"
        eval "$(/usr/local/bin/brew shellenv)"
    fi
    
    # Verify Homebrew is now available
    if ! command -v brew &>/dev/null; then
        echo -e "${RED}${CROSS_MARK} Homebrew installation failed.${NC}"
        exit 1
    fi
    echo -e "${GREEN}${CHECK_MARK} Homebrew installed and added to PATH successfully.${NC}"
else
    echo -e "${GREEN}${CHECK_MARK} Homebrew is already installed.${NC}"
fi

# Loop through each remaining tool and check installation
for tool in "${tools[@]}"; do
  IFS=":" read -r name check_command install_command <<< "$tool"
  install_tool "$name" "$check_command" "$install_command"
done

# Handle Java symlink setup separately
echo -e "${BLUE}Setting up Java symlink...${NC}"
setup_java_symlink

# Visual Studio Code installation with prompt
echo -e "${BLUE}Would you like to install Visual Studio Code? (Y/n)${NC}"
read -r INSTALL_VSCODE

if [[ "$INSTALL_VSCODE" =~ ^[Yy]$ || -z "$INSTALL_VSCODE" ]]; then
  install_tool "Visual Studio Code" "brew list --cask | grep -q 'visual-studio-code'" "brew install --cask visual-studio-code"
else
  echo -e "${YELLOW}Skipping Visual Studio Code installation.${NC}"
fi

echo -e "${GREEN}All installations completed successfully.${NC}"
