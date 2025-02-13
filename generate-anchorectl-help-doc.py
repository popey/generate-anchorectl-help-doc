#!/usr/bin/env python3
import subprocess
import re
import sys
from datetime import datetime
from pathlib import Path

class AnchorectlDocGenerator:
    def __init__(self, binary_path="anchorectl"):
        self.binary_path = binary_path
        self.version_info = self.get_version_info()
        self.output = []
        
    def get_version_info(self):
        """Get version information from anchorectl"""
        try:
            result = subprocess.run([self.binary_path, "version"], 
                                  capture_output=True, 
                                  text=True, 
                                  check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error getting version info: {e}", file=sys.stderr)
            sys.exit(1)

    def get_help_output(self, command_parts):
        """Get help output for a command"""
        try:
            cmd = [self.binary_path] + command_parts + ["--help"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to get help for command {' '.join(command_parts)}: {e}", 
                  file=sys.stderr)
            return None

    def parse_subcommands(self, help_text):
        """Parse subcommands from help output"""
        if not help_text:
            return []
        
        match = re.search(r"Available Commands:\n((?:  \w+\s+.*\n)*)", help_text)
        if not match:
            return []
            
        commands_text = match.group(1)
        commands = []
        for line in commands_text.split('\n'):
            if line.strip():
                cmd = line.strip().split()[0]
                commands.append(cmd)
        return commands

    def process_command(self, command_parts, level=1):
        """Recursively process a command and its subcommands"""
        command_str = " ".join(command_parts)
        heading = "#" * (level + 1)
        self.output.append(f"\n{heading} anchorectl {command_str}")
        
        help_output = self.get_help_output(command_parts)
        if help_output:
            self.output.append("\n```text")
            self.output.append(help_output)
            self.output.append("```\n")
            
            subcommands = self.parse_subcommands(help_output)
            for subcmd in subcommands:
                if subcmd not in ['help', 'completion']:  # Skip certain commands
                    self.process_command(command_parts + [subcmd], level + 1)

    def generate_docs(self):
        """Generate complete documentation"""
        # Add header with version info
        self.output.append("# AnchoreCTL Command Line Reference")
        self.output.append(f"\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.output.append("\n## Version Information")
        self.output.append("\n```")
        self.output.append(self.version_info)
        self.output.append("```\n")

        # Get top-level commands
        help_output = self.get_help_output([])
        if help_output:
            top_level_commands = self.parse_subcommands(help_output)
            
            # Process each top-level command
            for cmd in top_level_commands:
                if cmd not in ['help', 'completion']:  # Skip certain commands
                    self.process_command([cmd])

    def save_docs(self, output_dir="."):
        """Save documentation to a file"""
        version_match = re.search(r"Version:\s+(\S+)", self.version_info)
        version = version_match.group(1) if version_match else "unknown"
        
        output_path = Path(output_dir) / f"anchorectl-{version}-help.md"
        with open(output_path, 'w') as f:
            f.write("\n".join(self.output))
        return output_path

def main():
    if len(sys.argv) > 1:
        binary_path = sys.argv[1]
    else:
        binary_path = "anchorectl"

    generator = AnchorectlDocGenerator(binary_path)
    generator.generate_docs()
    output_path = generator.save_docs()
    print(f"Documentation generated: {output_path}")

if __name__ == "__main__":
    main()
